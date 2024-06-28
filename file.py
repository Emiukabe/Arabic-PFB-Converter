def presentationformat(letter, forms_dict):
    result = []
    length = len(letter)
    special_cases = ['ر', 'أ', 'إ', 'ا', 'ز', 'ذ', 'و', 'د', 'ﺎ', ' ﺭ ', ' ﺮ ', ' ﺮ ', ' أ ', ' ﺃ ', ' ﺄ ', ' إ ',
                     ' ﺇ ', 'ﺈ', 'ا', ' ﺎ ', ' ﺎ ', ' ﺯ ', 'ﺮ', 'ﺰ', 'ﺫ', 'ﺬ', 'ﺬ', 'و', 'ﻮ', ' ﻮ ',
                     ' ﺩ ', ' ﺪ ', ' ﺪ ', 'ﺪ', 'ﺯ', 'ﺮ', 'ﺭ', 'ﺎ', 'ﻵ', '\uFEF7', '\uFEF8', 'ﻶ', 'ﻷ', '\uFEF9',
                     '\uFEFA', 'ﻸ', 'ﻹ', '\uFEFB', '\uFEFC', 'ﻺ', 'ﻻ', '\uFEFB', '\uFEFC', 'ﻼ']

    laam = ['\uFEDD', '\uFEDF', '\uFEE0', '\uFEDE']
    alf = ['ا', 'ا', 'ا', 'ﺎ', '\uFE8E',
           'أ', 'أ', 'أ', '\uFE83', '\uFE84',
           'إ', 'إ', 'إ', '\uFE87', '\uFE88',
           'آ', 'آ', 'آ', '\uFE81', '\uFE82']
    i = 0
    while i < length:
        char = letter[i]
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
                result[i-1] = ''
                form = 'final'
                result.append(lamchar[char][form])
                i += 1
                continue

            else:
                if prev in laam and char in alf:
                    result[i-1] = ''
                    form = 'final'
                    result.append(lamchar[char][form])
                    i += 1
                    continue

                elif prev in special_cases:
                    if char == "ل":
                        form = 'isolated'
                    elif char not in ['ه', 'ي', 'ى', 'ة']:
                        form = 'initial'
                    else:
                        form = 'isolated'
                else:
                    form = 'final'
        # in between
        else:
            if prev in laam and char in alf:
                result[i-1] = ''
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


lamchar = {'آ': {'isolated': 'ﻵ', 'initial': '\uFEF7', 'medial': '\uFEF8', 'final': 'ﻶ'},
           'أ': {'isolated': 'ﻷ', 'initial': '\uFEF9', 'medial': '\uFEFA', 'final': 'ﻸ'},
           'إ': {'isolated': 'ﻹ', 'initial': '\uFEFB', 'medial': '\uFEFC', 'final': 'ﻺ'},
           'ا': {'isolated': 'ﻻ', 'initial': '\uFEFB', 'medial': '\uFEFC', 'final': 'ﻼ'}, }

forms = {

    'ا': {'isolated': 'ا', 'initial': 'ا', 'medial': 'ﺎ', 'final': '\uFE8E'},
    'أ': {'isolated': 'أ', 'initial': 'أ', 'medial': '\uFE83', 'final': '\uFE84'},
    'إ': {'isolated': 'إ', 'initial': 'إ', 'medial': '\uFE87', 'final': '\uFE88'},
    'آ': {'isolated': 'آ', 'initial': 'آ', 'medial': '\uFE81', 'final': '\uFE82'},
    'ب': {'isolated': '\uFE8F', 'initial': '\uFE91', 'medial': '\uFE92', 'final': '\uFE90'},
    'ت': {'isolated': '\uFE95', 'initial': '\uFE97', 'medial': '\uFE98', 'final': '\uFE96'},
    'ث': {'isolated': '\uFE99', 'initial': '\uFE9B', 'medial': '\uFE9C', 'final': '\uFE9A'},
    'ج': {'isolated': '\uFE9D', 'initial': '\uFE9F', 'medial': '\uFEA0', 'final': '\uFE9E'},
    'ح': {'isolated': '\uFEA1', 'initial': '\uFEA3', 'medial': '\uFEA4', 'final': '\uFEA2'},
    'خ': {'isolated': '\uFEA5', 'initial': '\uFEA7', 'medial': '\uFEA8', 'final': '\uFEA6'},
    'د': {'isolated': '\uFEA9', 'initial': '\uFEA9', 'medial': 'ﺪ', 'final': 'ﺪ'},
    'ذ': {'isolated': '\uFEAB', 'initial': '\uFEAB', 'medial': 'ﺬ', 'final': 'ﺬ'},
    'ر': {'isolated': 'ر', 'initial': 'ر', 'medial': 'ﺮ', 'final': 'ﺮ'},
    'ز': {'isolated': '\ز', 'initial': 'ز', 'medial': 'ﺰ', 'final': 'ﺰ'},
    'س': {'isolated': '\uFEB1', 'initial': '\uFEB3', 'medial': '\uFEB4', 'final': '\uFEB2'},
    'ش': {'isolated': '\uFEB5', 'initial': '\uFEB7', 'medial': '\uFEB8', 'final': '\uFEB6'},
    'ص': {'isolated': '\uFEB9', 'initial': '\uFEBB', 'medial': '\uFEBC', 'final': '\uFEBA'},
    'ض': {'isolated': '\uFEBD', 'initial': '\uFEBF', 'medial': '\uFEC0', 'final': '\uFEBE'},
    'ط': {'isolated': '\uFEC1', 'initial': '\uFEC3', 'medial': '\uFEC4', 'final': '\uFEC2'},
    'ظ': {'isolated': '\uFEC5', 'initial': '\uFEC7', 'medial': '\uFEC8', 'final': '\uFEC6'},
    'ع': {'isolated': '\uFEC9', 'initial': '\uFECB', 'medial': 'ﻌ', 'final': '\uFECA'},
    'غ': {'isolated': '\uFECD', 'initial': '\uFECF', 'medial': '\uFED0', 'final': '\uFECE'},
    'ف': {'isolated': '\uFED1', 'initial': '\uFED3', 'medial': '\uFED4', 'final': '\uFED2'},
    'ق': {'isolated': '\uFED5', 'initial': '\uFED7', 'medial': '\uFED8', 'final': '\uFED6'},
    'ك': {'isolated': '\uFED9', 'initial': '\uFEDB', 'medial': '\uFEDC', 'final': '\uFEDA'},
    'ل': {'isolated': 'ل', 'initial': '\uFEDF', 'medial': '\uFEE0', 'final': '\uFEDE'},
    'م': {'isolated': '\uFEE1', 'initial': '\uFEE3', 'medial': '\uFEE4', 'final': '\uFEE2'},
    'ن': {'isolated': '\uFEE5', 'initial': '\uFEE7', 'medial': '\uFEE8', 'final': '\uFEE6'},
    'ه': {'isolated': 'ه', 'initial': 'ﻫ', 'medial': '\uFEEC', 'final': 'ه'},
    'ة': {'isolated': 'ة', 'initial': 'ة', 'medial': '\uFE94', 'final': '\uFE94'},
    'و': {'isolated': 'و', 'initial': 'و', 'medial': 'ﻮ', 'final': 'ﻮ'},
    'ي': {'isolated': 'ي', 'initial': 'ﻳ', 'medial': '\uFEF4', 'final': 'ﻲ'},
    'ئ': {'isolated': 'ئ', 'initial': 'ﻳ', 'medial': '\uFEF4', 'final': 'ﻲ'},
    'ى': {'isolated': 'ى', 'initial': 'ﻳ', 'medial': '\uFEF4', 'final': 'ﻰ'},
}

# Test the function with a paragraph
text = "كلال"
convtxt = ""
word_list = text.split()
for word in word_list:
    convtxt += presentationformat(word, forms)
    convtxt += " "
print(f"Original: {text}")
print(f"Converted: {convtxt}")

# Save the result to a file
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(text + "\n")
    f.write(convtxt)
