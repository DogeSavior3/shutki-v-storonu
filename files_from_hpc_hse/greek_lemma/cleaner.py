# coding: utf8
import os
import re
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

def clean_text(text):
    text = remove_tonos_greek(text)
    cleaned_text = re.sub(r'[^α-ωΑ-Ω0-9\s\.,;:!?\(\)\[\]\{\}\'"«»\-]', '', text)
    return cleaned_text

def preprocess_texts(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if not filename.endswith('.txt'):
            continue

        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        with open(input_path, 'r', encoding='utf-8') as file:
            text = file.read().strip()

        cleaned_text = clean_text(text)

        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(cleaned_text)

preprocess_texts('pure', 'cleaned_pure')
