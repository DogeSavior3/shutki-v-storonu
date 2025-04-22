import os

def distribute_files_by_read_write(source_folder, target_base):
    target_folders = [f"{target_base}/cleaned_pure_{i}" for i in range(1, 129)]
    
    for folder in target_folders:
        if not os.path.exists(folder):
            os.makedirs(folder)

    files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]
    
    for i, file_name in enumerate(files):
        source_path = os.path.join(source_folder, file_name)
        target_folder = target_folders[i % 128]
        target_path = os.path.join(target_folder, file_name)
        
        try:
            with open(source_path, 'r', encoding='utf-8', errors='replace') as source_file:
                content = source_file.read()
            
            with open(target_path, 'w', encoding='utf-8') as target_file:
                target_file.write(content)
        
        except Exception as e:
            print(f"Error processing {file_name}: {e}")

input_folder = 'cleaned_pure'
output_base = '.'    
distribute_files_by_read_write(input_folder, output_base)
