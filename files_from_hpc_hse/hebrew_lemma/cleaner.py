import os
import re

def clean_text(text):
    return re.sub(r'[^\u0590-\u05FF\u0030-\u0039\s\.,:!?\'"«»\(\)\[\]\-]', '', text)

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
