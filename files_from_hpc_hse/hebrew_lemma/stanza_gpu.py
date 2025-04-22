# coding: utf8
import os
import stanza
import time

input_folder = 'cleaned_pure'
output_folders = {
    'ancient-hebrew': 'lemma_stanza_anc',
    'hebrew-1': 'lemma_stanza_HTB',
    'hebrew-2': 'lemma_stanza_IAHLT',
}

pipelines = {
    'ancient-hebrew': stanza.Pipeline(
        lang='hbo',
        processors='tokenize,mwt,pos,lemma',
        model_dir='stanza_resources',
        download_method=None,
        use_gpu=True
    ),
    'hebrew-1': stanza.Pipeline(
        lang='he',
        processors='tokenize,mwt,pos,lemma',
        model_dir='stanza_resources',
        download_method=None,
        use_gpu=True
    ),
    'hebrew-2': stanza.Pipeline(
        lang='he',
        processors='tokenize,mwt,pos,lemma',
        package='iahltwiki',
        model_dir='stanza_resources',
        download_method=None,
        use_gpu=True
    ),
}

label_dict = {'PROPN': 'person1', 'PRON': 'pron1', 'NUM': 'ordinal1'}
for folder in output_folders.values():
    os.makedirs(folder, exist_ok=True)

def load_documents_in_batches(input_folder, batch_size=100):
    filenames = [filename for filename in os.listdir(input_folder) if filename.endswith('.txt')]
    batches = []
    
    for i in range(0, len(filenames), batch_size):
        batch_filenames = filenames[i:i + batch_size]
        documents = []
        for filename in batch_filenames:
            input_path = os.path.join(input_folder, filename)
            with open(input_path, 'r', encoding='utf-8') as file:
                text = file.read().strip()
            documents.append(stanza.Document([], text=text))
        batches.append((documents, batch_filenames))
    
    return batches

def process_documents(documents, pipeline):
    return pipeline(documents)

def extract_lemmas(doc):
    current_result = []
    for sentence in doc.sentences:
        for word in sentence.words:
            upos = word.upos
            
            if upos is None:
                continue
            
            if upos in label_dict:
                current_result.append(label_dict[upos])
            elif upos != 'PUNCT':
                lemma = word.lemma.lower() if word.lemma else word.text.lower()
                current_result.append(lemma)
    return ' '.join(current_result)

def process_all_documents_in_batches(batch_size=100):
    batches = load_documents_in_batches(input_folder, batch_size=batch_size)
    
    for documents, filenames in batches:
        processed_results = {lang_code: [] for lang_code in pipelines.keys()}
        for lang_code, pipeline in pipelines.items():
            retry_delay = 10
            while True:
                try:
                    out_docs = process_documents(documents, pipeline)
                    processed_results[lang_code] = out_docs
                    break
                except Exception as e:
                    print(f"Error processing documents for {lang_code}: {e}. Retrying in {retry_delay} seconds...")
                    time.sleep(retry_delay)
        
        save_results(processed_results, filenames, output_folders)

def save_results(processed_results, filenames, output_folders):
    for lang_code, out_docs in processed_results.items():
        output_folder = output_folders[lang_code]

        for i, doc in enumerate(out_docs):
            processed_text = extract_lemmas(doc)
            output_path = os.path.join(output_folder, filenames[i])
            with open(output_path, 'w', encoding='utf-8') as output_file:
                output_file.write(processed_text + '\n')

process_all_documents_in_batches(batch_size=200)
