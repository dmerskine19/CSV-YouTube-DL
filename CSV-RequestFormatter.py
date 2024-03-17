import os

def create_category_files(categories):
    output_dir = r'D:/Code/CSV-YouTube-DL/audio_Files/category_ids'
    for category in categories:
        file_name = os.path.join(output_dir, category.replace('/', '_') + ".txt")
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        with open(file_name, "w") as file:
            file.write("")


def write_matching_ids(dataset_file, output_file, target_label):
    with open(dataset_file, 'r') as f:
        lines = f.readlines()
    matching_ids = []
    for line in lines:
        parts = line.strip().split(',')
        if target_label in parts:
            matching_ids.append(parts[0])
    with open(output_file, 'w') as f:
        for id in matching_ids:
            f.write(id + '\n')

if __name__ == "__main__":

    with open('category_ids.txt', 'r') as f:
        categories = [line.strip() for line in f.readlines()]

    create_category_files(categories)

    print("Text files created for each category.")
    
