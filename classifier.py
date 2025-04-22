import sys
import numpy as np
import pandas as pd
import joblib
import re
from tqdm import tqdm
from collections import Counter

from natasha import Segmenter, MorphVocab, NewsNERTagger, NewsEmbedding, NewsMorphTagger, Doc
from requirements.trajectories import trajectory_from_text
from requirements.ordec import entropy_complexity

n, m = 3, 4
wdict = np.load('requirements/russian_dict_cbow.npy', allow_pickle=True).item()
wdict = {word: vec[-8:] for word, vec in wdict.items()}

def prepare_russian_text(text):
    segmenter = Segmenter()
    emb = NewsEmbedding()
    morph_tagger = NewsMorphTagger(emb)
    ner_tagger = NewsNERTagger(emb)
    morph_vocab = MorphVocab()
    label_dict = {'NUM': 'ordinal1', 'PRON': 'pron1', 'PER': 'person1'}
    next_label_num = 5

    raw_text = text.replace('\n', ' ')
    raw_text = re.sub(r'\d+', '0', raw_text)
    raw_text = ' '.join(re.findall(r'[А-яЁё]+', raw_text))

    doc = Doc(raw_text)
    doc.segment(segmenter)
    doc.tag_ner(ner_tagger)

    for span in reversed(doc.ner.spans):
        if span.type not in label_dict:
            label_dict[span.type] = str(next_label_num)
            next_label_num += 1
        raw_text = "".join((raw_text[:span.start], label_dict[span.type], raw_text[span.stop:]))

    doc = Doc(raw_text)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)

    prepared_text = ''
    prev_num = False
    for token in tqdm(doc.tokens, desc='Text preprocessing...'):
        if token.pos == 'NUM' and not token.text.isdigit():
            if not prev_num:
                prepared_text += '0 '
                prev_num = True
            continue
        prev_num = False
        if token.pos in label_dict:
            prepared_text += label_dict[token.pos] + ' '
        elif token.pos != 'PUNCT':
            try:
                token.lemmatize(morph_vocab)
                prepared_text += token.lemma.lower() + ' '
            except:
                prepared_text += token.text.lower() + ' '

    return prepared_text.strip()

def split_text_into_chunks(text, chunk_size=45):
    words = text.split()
    parts = [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
    return [part for part in parts if len(part.split()) >= 3]

def classify_text(path_to_txt, model_path='requirements/entropy_classifier_knn.joblib', threshold=0.01, n=3, m=4):
    with open(path_to_txt, 'r', encoding='utf-8') as f:
        raw_text = f.read()

    prepared_text = prepare_russian_text(raw_text)
    parts = split_text_into_chunks(prepared_text, chunk_size=25)

    model = joblib.load(model_path)
    results = []
    for i, part in enumerate(tqdm(parts, desc="Processing chunks")):
        ts = trajectory_from_text(part, wdict, m)
        if ts is not None:
            ent, comp = entropy_complexity(ts, n=n, m=m)
            results.append([ent, comp])

    if not results:
        print("Ошибка. Вероятно, текст пуст или написан на ином языке")
        return

    X_new = pd.DataFrame(results, columns=['entropy', 'complexity'])
    distances, indices = model.kneighbors(X_new)
    y_train = model._y

    predictions = []
    for dist_row, idx_row in zip(distances, indices):
        if np.all(dist_row > threshold):
            predictions.append("other")
        else:
            neighbor_labels = y_train[idx_row]
            majority = Counter(neighbor_labels).most_common(1)[0][0]
            predictions.append(majority)

    final_label = Counter(predictions).most_common(1)[0][0]
    humor_str = 'является шуткой'
    literature_str = 'является литературным произведением'
    noise_str = 'относится к иной категории текстов'
    if (final_label == 0):
    	print(f"Ваш текст {humor_str}.")
    elif (final_label == 1):
	    print(f"Ваш текст {literature_str}.")
    else:
	    print(f"Ваш текст {noise_str}.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Аргументы неверны. Попробуйте: python classifier.py path/to/text.txt")
        sys.exit(1)

    classify_text(sys.argv[1])

