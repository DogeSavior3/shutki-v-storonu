import os
import re
import stanza

input_folder = 'pure'
output_folders = {
    'ancient-hebrew': 'lemma_stanza_anc',
    'hebrew-1': 'lemma_stanza_HTB',
    'hebrew-2': 'lemma_stanza_IAHLT',
    'all': 'lemma_stanza_all'
}

pipelines = {
    'ancient-hebrew': stanza.Pipeline(
        lang = 'hbo',
        processors = 'tokenize, mwt, pos, lemma',
        model_dir = 'stanza_resources',
        download_method = None,
        use_gpu = True
    ),
    'hebrew-1': stanza.Pipeline(
        lang = 'he',
        processors = 'tokenize, mwt, pos, lemma',
        model_dir = 'stanza_resources',
        download_method = None,
        use_gpu = True
    ),
    'hebrew-2': stanza.Pipeline(
        lang = 'he',
        processors = 'tokenize, mwt, pos, lemma',
        package = 'iahltwiki',
        model_dir = 'stanza_resources',
        download_method = None,
        use_gpu = True
    )
}

label_dict = {'PROPN': 'person1', 'PRON': 'pron1', 'NUM': 'ordinal1'}
for folder in output_folders.values():
    os.makedirs(folder, exist_ok=True)

def clean_text(text):
    cleaned_text = re.sub(r'[^\u0590-\u05FF\u0030-\u0039\s\.,:!?\'"«»\(\)\[\]\-]', '', text)
    return cleaned_text

def process_files_in_batches(input_folder, output_folders, pipelines, batch_size=8):
    texts_batch = []
    filenames_batch = []

    for filename in os.listdir(input_folder):
        if not filename.endswith('.txt'):
            continue

        input_path = os.path.join(input_folder, filename)

        with open(input_path, 'r', encoding='utf-8') as file:
            text = file.read().strip()

        cleaned_text = clean_text(text)
        texts_batch.append(cleaned_text)
        filenames_batch.append(filename)

        if len(texts_batch) >= batch_size:
            process_batch_and_save(texts_batch, filenames_batch, output_folders, pipelines)
            texts_batch.clear()
            filenames_batch.clear()

    if texts_batch:
        process_batch_and_save(texts_batch, filenames_batch, output_folders, pipelines)


def process_batch_and_save(texts_batch, filenames_batch, output_folders, pipelines):
    for lang_code, pipeline in pipelines.items():
        print(f"Processing batch for {lang_code}")
        processed_texts = process_batch(texts_batch, pipeline)

        for i, processed_text in enumerate(processed_texts):
            output_path = os.path.join(output_folders[lang_code], filenames_batch[i])
            with open(output_path, 'w', encoding='utf-8') as output_file:
                output_file.write(processed_text + '\n')


def process_batch(batch_texts, pipeline):
    combined_text = ' <<br>> '.join(batch_texts)
    processed_doc = pipeline(combined_text)

    results = []
    current_result = []

    for sentence in processed_doc.sentences:
        for word in sentence.words:
            if word.text == '<<br>>':
                results.append(' '.join(current_result))
                current_result = []
                continue

            upos = word.upos
            if upos is None:
                continue

            if upos in label_dict:
                current_result.append(label_dict[upos])
            elif upos != 'PUNCT':
                lemma = word.lemma.lower() if word.lemma else word.text.lower()
                current_result.append(lemma)

    if current_result:
        results.append(' '.join(current_result))

    return results

process_files_in_batches(input_folder, output_folders, pipelines, batch_size=100)