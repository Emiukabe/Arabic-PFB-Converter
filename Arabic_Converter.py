import os
from arabic_char_data import special_cases, laam, alf, lamchar, forms

def presentation_format(word, forms_dict):
    result = []
    length = len(word)
    i = 0

    while i < length:
        char = word[i]
        prev = result[i - 1] if i > 0 else None

        if char == '/':
            result.append(char)
            i += 1
            continue

        if char not in forms_dict:
            result.append(char)
            i += 1
            continue

        if i == 0 or (i > 0 and word[i - 1] == '/'):
            if char in special_cases or length == 1 or word[i + 1] not in forms_dict or word[i + 1] == '/':
                form = 'isolated'
            else:
                form = 'initial'
        elif i == length - 1 or (i < length - 1 and word[i + 1] == '/'):
            if prev in laam and char in alf:
                result[-1] = ''
                form = 'isolated' if len(result) > 0 else 'final'
                result.append(lamchar[char][form])
                i += 1
                continue
            form = 'isolated' if prev in special_cases and char == "ل" else 'final'
        else:
            if prev in laam and char in alf:
                result[-1] = ''
                form = 'isolated' if len(result) > 1 and result[-2] in special_cases else 'final'
                result.append(lamchar[char][form])
                i += 1
                continue
            form = 'medial' if prev not in special_cases else 'initial'

        result.append(forms_dict[char][form])
        i += 1

    return ''.join(result)

def process_file(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f_in, open(output_path, 'w', encoding='utf-8') as f_out:
        for line in f_in:
            if not line.strip():
                f_out.write(line)
                continue

            words = line.strip().split()
            processed_words = []

            for word in words:
                special_char_positions = {i: char for i, char in enumerate(word) if char in "().،:\"?؟"}
                temp_word = word.replace('/', ' / ')
                cleaned_word = ''.join([char for char in temp_word if char not in "().،:\"'?؟"])

                segments = cleaned_word.split(' / ')
                converted_segments = [presentation_format(segment, forms) for segment in segments]

                converted_word = '/'.join(converted_segments)

                for position, char in special_char_positions.items():
                    converted_word = converted_word[:position] + char + converted_word[position:]

                processed_words.append(converted_word)

            converted_line = ' '.join(processed_words)
            f_out.write(f"{converted_line}\n")


input_directory = input("Please enter location to the directory containing the files put front slashes (/) : ")
output_directory = input("Please enter location to the directory to put the files in , with front slashes (/) : ")

if input_directory == output_directory:
    print("Input and output directories cannot be the same")
    exit()

os.makedirs(output_directory, exist_ok=True)

for filename in os.listdir(input_directory):
    input_path = os.path.join(input_directory, filename)
    output_path = os.path.join(output_directory, filename)

    if os.path.isfile(input_path):  # Ensure it's a file
        process_file(input_path, output_path)

print(f"Processing complete. Check the output directory: {output_directory}")