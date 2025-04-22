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
    return text

def process_text_with_stanza(text, pipeline):
    processed_text = pipeline(text)
    prepared_text = []

    for sentence in processed_text.sentences:
        for word in sentence.words:
            upos = word.upos

            if upos is None:
                continue

            if upos in label_dict:
                prepared_text.append(label_dict[upos])
            elif upos != 'PUNCT':
                lemma = word.lemma.lower() if word.lemma else word.text.lower()
                prepared_text.append(lemma)

    return ' '.join(prepared_text)


def split_processed_text(processed_text, separator):
    return processed_text.split(separator)

buffer = {}
file_names = {}
buff_limit = 1024 * 1024 * 10
separator = '<<br>>'
for folder in output_folders.values():
    os.makedirs(folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith('.txt'):
        input_path = os.path.join(input_folder, filename)

        with open(input_path, 'r', encoding='utf-8') as file:
            text = file.read()

        cleaned_text = clean_text(text)

        if filename not in buffer:
            buffer[filename] = []
            file_names[filename] = []

        buffer[filename].append(cleaned_text)
        file_names[filename].append(filename)

        buffer_size = sum(len(t) for t in buffer[filename])
        if buffer_size >= buff_limit:
            combined_text = separator.join(buffer[filename])

            for lang_code, pipeline in pipelines.items():
                processed_text = process_text_with_stanza(combined_text, pipeline)

                processed_texts = split_processed_text(processed_text, separator)

                for original_filename, processed_part in zip(file_names[filename], processed_texts):
                    output_path = os.path.join(output_folders[lang_code], original_filename)
                    with open(output_path, 'w', encoding='utf-8') as output_file:
                        output_file.write(processed_part)

            buffer[filename] = []
            file_names[filename] = []

for filename, texts in buffer.items():
    if texts:
        combined_text = separator.join(texts)
        for lang_code, pipeline in pipelines.items():
            processed_text = process_text_with_stanza(combined_text, pipeline)
            processed_texts = split_processed_text(processed_text, separator)

            for original_filename, processed_part in zip(file_names[filename], processed_texts):
                output_path = os.path.join(output_folders[lang_code], original_filename)
                with open(output_path, 'w', encoding='utf-8') as output_file:
                    output_file.write(processed_part)