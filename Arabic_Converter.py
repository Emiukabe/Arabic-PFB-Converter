from arabic_char_data import special_cases, laam, alf, lamchar, forms

def presentationformat(word, forms_dict):
    result = []
    length = len(word)

    i = 0
    while i < length:
        char = word[i]
        if i > 0:
            prev = result[i - 1] if result else None

        if char == '/':
            result.append(char)  # Append slashes unchanged
            i += 1
            continue

        if char not in forms_dict:
            result.append(char)  # Append non-Arabic characters unchanged
            i += 1
            continue

        # Start
        if i == 0 or (i > 0 and word[i - 1] == '/'):
            if char in special_cases:
                form = 'isolated'
            elif length == 1 or word[i + 1] not in forms_dict or word[i + 1] == '/':
                form = 'isolated'
            else:
                form = 'initial'
        # End
        elif i == length - 1 or (i < length - 1 and word[i + 1] == '/'):
            if prev in laam and char in alf:
                result[-1] = ''
                if len(result) > 0:
                    form = 'isolated'
                else:
                    form = 'final'
                result.append(lamchar[char][form])
                i += 1
                continue

            elif prev in special_cases:
                if char == "ل":
                    form = 'isolated'
                else:
                    form = 'isolated'
            else:
                form = 'final'
        # In between
        else:
            if prev in laam and char in alf:
                result[-1] = ''
                if len(result) > 1 and result[-2] in special_cases:
                    form = 'isolated'
                elif len(result) == 1:
                    form = 'isolated'
                else:
                    form = 'final'
                result.append(lamchar[char][form])
                i += 1
                continue
            elif prev not in special_cases:
                form = 'medial'
            else:
                form = 'initial'

        result.append(forms_dict[char][form])
        i += 1
    return ''.join(result)

# Read input from a file and process line by line
input_file = 'input.txt'
output_file = 'output.txt'

with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8') as f_out:
    for line in f_in:
        line = line.strip()
        if not line:  # Skip empty lines
            continue

        words = line.split()  # Split line into words
        processed_words = []

        for word in words:
            special_char_positions = {i: char for i, char in enumerate(word) if char in "().،:"}
            temp_word = word.replace('/', ' / ')  # Add spaces around slashes
            cleaned_word = ''.join([char for char in temp_word if char not in "().،:"])  # Remove special characters except slashes

            # Convert each segment separately
            segments = cleaned_word.split(' / ')
            converted_segments = [presentationformat(segment, forms) for segment in segments]

            # Rejoin the segments with slashes, remove extra spaces
            converted_word = '/'.join(converted_segments)

            # Reinsert the special characters
            for position, char in special_char_positions.items():
                converted_word = converted_word[:position] + char + converted_word[position:]

            processed_words.append(converted_word)

        converted_line = ' '.join(processed_words)  # Join processed words back into a line
        f_out.write(f"{converted_line}\n")

# Output a message indicating completion
print(f"Processing complete. Check the output file: {output_file}")
