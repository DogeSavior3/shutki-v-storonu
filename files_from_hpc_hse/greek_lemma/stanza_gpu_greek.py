# coding: utf8
import os
import stanza
import time

input_folder = 'cleaned_pure'
output_folders = {
    'ancient-greek-proiel': 'lemma_gpu_stanza_ag',
    'ancient-greek-perseus': 'lemma_gpu_stanza_agp',
    'greek-1': 'lemma_gpu_stanza_g_1',
    'greek-2': 'lemma_gpu_stanza_g_2',
}

pipelines = {
    'ancient-greek-perseus': stanza.Pipeline(
        lang = 'grc',
        processors='tokenize, pos, lemma',
        model_dir = 'stanza_resources',
        download_method = None,
        use_gpu = True
    ),
    'ancient-greek-proiel': stanza.Pipeline(
        lang = 'grc', 
        processors='tokenize, pos, lemma', 
        package = 'proiel',
        model_dir = 'stanza_resources',
        download_method = None,
        use_gpu = True
    ),
    'greek-1': stanza.Pipeline(
        lang = 'el', 
        processors='tokenize, mwt, pos, lemma',
        model_dir = 'stanza_resources',
        download_method = None,
        use_gpu = True
    ),
    'greek-2': stanza.Pipeline(
        lang = 'el', 
        processors='tokenize, pos, lemma', 
        package = 'gud',
        model_dir = 'stanza_resources',
        download_method = None,
        use_gpu = True
    )
}

noun = ['με', 'μας', 'σε', 'σας', 'τον', 'τους', 'την', 'τις', 'το', 'τα', 'μου', 'μας', 'σου', 'σας', 'του', 'τους',
        'της', 'τους', 'του', 'τους', 'εγώ', 'εμείς', 'εσύ', 'εσείς', 'αυτός', 'αυτοί', 'αυτή', 'αυτές', 'αυто', 'αυτά']
numerals = [
    "ένα", "δύο", "τρία", "τέσσερα", "πέντε", "έξι", "επτά", "οκτώ", "εννέα", "δέκα", "είκοσι", "τριάντα",
    "σαράντα", "πενήντα", "εξήντα", "εβδομήντα", "ογδόντа", "ενενήντα", "εκατό", "διακόσια", "τριακόσια",
    "τετρακόσια", "πεντακόσια", "εξακόσια", "επτακόσια", "οκτακόσια", "εννιακόσια", "χίλια", "δέκα χιλιάδες",
    "εκατό χιλιάδες", "ένα εκατομμύριο"
]
words_to_remove = noun + numerals

tonos_replacements = {
        'ά': 'α',
        'έ': 'ε',
        'ή': 'η',
        'ί': 'ι',
        'ό': 'ο',
        'ύ': 'υ',
        'ώ': 'ω',
        'Ά': 'Α',
        'Έ': 'Ε',
        'Ή': 'Η',
        'Ί': 'Ι',
        'Ό': 'Ο',
        'Ύ': 'Υ',
        'Ώ': 'Ω'}

def remove_tonos_greek(text):
    result = text
    for tonos_char, plain_char in tonos_replacements.items():
        result = result.replace(tonos_char, plain_char)
    
    return result

for i in range(len(words_to_remove)):
    words_to_remove[i] = remove_tonos_greek(words_to_remove[i])
    

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
                if lemma not in words_to_remove:
                    current_result.append(lemma)
    return ' '.join(current_result)

def process_all_documents_in_batches(batch_size=100):
    batches = load_documents_in_batches(input_folder, batch_size=batch_size)
    
    for documents, filenames in batches:
        processed_results = {lang_code: [] for lang_code in pipelines.keys()}
        for lang_code, pipeline in pipelines.items():
            retry_delay = 10
            try:
                out_docs = pipeline(documents)
                processed_results[lang_code] = out_docs
            except Exception as e:
                time.sleep(retry_delay)
        save_results(processed_results, filenames, pipelines, output_folders)

def save_results(processed_results, filenames, output_folders):
    for lang_code, out_docs in processed_results.items():
        output_folder = output_folders[lang_code]

        for i, doc in enumerate(out_docs):
            processed_text = extract_lemmas(doc)
            output_path = os.path.join(output_folder, filenames[i])
            with open(output_path, 'w', encoding='utf-8') as output_file:
                output_file.write(processed_text + '\n')

process_all_documents_in_batches(batch_size = 100)
