from arabic_char_data import special_cases, laam, alf, lamchar, forms

def presentationformat(word, forms_dict):
    result = []
    length = len(word)

    i = 0
    while i < length:
        char = word[i]
        if i > 0:
            prev = result[i - 1]
        if char not in forms_dict:
            result.append(char)  # Append non-Arabic characters unchanged
            i += 1
            continue

        # Start
        if i == 0:
            if char in special_cases:
                form = 'isolated'
            elif length == 1 or word[i + 1] not in forms_dict:
                form = 'isolated'
            else:
                form = 'initial'
        # End
        elif i == length - 1:
            if prev in laam and char in alf:
                result[-1] = ''
                if len(result) > 0 and result[-1] not in special_cases:
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
        # in between
        else:
            if prev in laam and char in alf:
                result[-1] = ''
                form = 'isolated'
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
input_file = 'inpu1t.txt'
output_file = 'output.txt'

with open(input_file, 'r', encoding='utf-8') as f_in, open(output_file, 'w', encoding='utf-8') as f_out:
    for line in f_in:
        line = line.strip()
        if not line:  # Skip empty lines
            continue

        words = line.split()  # Split line into words
        converted_words = [presentationformat(word, forms) for word in words]  # Process each word
        converted_line = ' '.join(converted_words)  # Join processed words back into a line

        f_out.write(f"{converted_line}\n")

# Output a message indicating completion
print(f"Processing complete. Check the output file: {output_file}")
