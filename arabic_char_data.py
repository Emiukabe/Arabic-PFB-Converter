# arabic_char_data.py

special_cases = {'ّ','ر', 'أ', 'إ', 'ا', 'ز', 'ذ', 'و', 'د', 'ﺎ', ' ﺭ ', ' ﺮ ', ' ﺮ ', ' أ ', ' ﺃ ', ' ﺄ ', ' إ ',
                 ' ﺇ ','ؤ', 'ﺈ', 'ا', ' ﺎ ', ' ﺎ ', ' ﺯ ', 'ﺮ', 'ﺰ', 'ﺫ', 'ﺬ', 'ﺬ', 'و', 'ﻮ', ' ﻮ ',
                 ' ﺩ ', ' ﺪ ', ' ﺪ ', 'ﺪ', 'ﺯ', 'ﺮ', 'ﺭ', 'ﺎ', 'ﻵ', '\uFEF7', '\uFEF8', 'ﻶ', 'ﻷ', '\uFEF9',
                 '\uFEFA', 'ﻸ', 'ﻹ', '\uFEFB', '\uFEFC', 'ﻺ', 'ﻻ', '\uFEFB', '\uFEFC', 'ﻼ', 'ﺇ', 'ﺃ','أ','ﺄ','ﺆ',"/",'ﺮ','ً','أ','ً','ً','ُ''ً','ء','ُ'}

laam = ['\uFEDD', '\uFEDF', '\uFEE0', '\uFEDE']
alf = ['ا', 'ا', 'ا', 'ﺎ', '\uFE8E',
       'أ', 'أ', 'أ', '\uFE83', '\uFE84',
       'إ', 'إ', 'إ', '\uFE87', '\uFE88',
       'آ', 'آ', 'آ', '\uFE81', '\uFE82']

lamchar = {'آ': {'isolated': 'ﻵ', 'final': 'ﻶ'},
           'أ': {'isolated': 'ﻷ', 'final': 'ﻸ'},
           'إ': {'isolated': 'ﻹ', 'final': 'ﻺ'},
           'ا': {'isolated': 'ﻻ', 'final': 'ﻼ'}, }

forms = {
    'ا': {'isolated': 'ا', 'initial': 'ا', 'medial': 'ﺎ', 'final': 'ﺎ'},
    'أ': {'isolated': 'أ', 'initial': 'أ', 'medial': 'ﺄ', 'final': 'ﺄ'},
    'إ': {'isolated': 'إ', 'initial': 'إ', 'medial': 'ﺈ', 'final': 'ﺈ'},
    'آ': {'isolated': 'آ', 'initial': 'آ', 'medial': 'ﺂ', 'final': 'ﺂ'},
    'ب': {'isolated': 'ب', 'initial': '\uFE91', 'medial': '\uFE92', 'final': '\uFE90'},
    'ت': {'isolated': 'ت', 'initial': '\uFE97', 'medial': '\uFE98', 'final': '\uFE96'},
    'ث': {'isolated': 'ث', 'initial': '\uFE9B', 'medial': '\uFE9C', 'final': '\uFE9A'},
    'ج': {'isolated': 'ج', 'initial': '\uFE9F', 'medial': '\uFEA0', 'final': '\uFE9E'},
    'ح': {'isolated': 'ح', 'initial': '\uFEA3', 'medial': '\uFEA4', 'final': '\uFEA2'},
    'خ': {'isolated': 'خ', 'initial': '\uFEA7', 'medial': '\uFEA8', 'final': '\uFEA6'},
    'د': {'isolated': 'د', 'initial': 'د', 'medial': 'ﺪ', 'final': 'ﺪ'},
    'ذ': {'isolated': 'ذ', 'initial': 'ذ', 'medial': 'ﺬ', 'final': 'ﺬ'},
    'ر': {'isolated': 'ر', 'initial': 'ر', 'medial': 'ﺮ', 'final': 'ﺮ'},
    'ز': {'isolated': 'ز', 'initial': 'ز', 'medial': 'ﺰ', 'final': 'ﺰ'},
    'س': {'isolated': 'س', 'initial': '\uFEB3', 'medial': '\uFEB4', 'final': '\uFEB2'},
    'ش': {'isolated': 'ش', 'initial': '\uFEB7', 'medial': '\uFEB8', 'final': '\uFEB6'},
    'ص': {'isolated': 'ص', 'initial': '\uFEBB', 'medial': '\uFEBC', 'final': '\uFEBA'},
    'ض': {'isolated': 'ض', 'initial': '\uFEBF', 'medial': '\uFEC0', 'final': '\uFEBE'},
    'ط': {'isolated': 'ط', 'initial': '\uFEC3', 'medial': '\uFEC4', 'final': '\uFEC2'},
    'ظ': {'isolated': 'ظ', 'initial': '\uFEC7', 'medial': '\uFEC8', 'final': '\uFEC6'},
    'ع': {'isolated': 'ع', 'initial': '\uFECB', 'medial': 'ﻌ', 'final': '\uFECA'},
    'غ': {'isolated': 'غ', 'initial': '\uFECF', 'medial': '\uFED0', 'final': '\uFECE'},
    'ف': {'isolated': 'ف', 'initial': '\uFED3', 'medial': '\uFED4', 'final': '\uFED2'},
    'ق': {'isolated': 'ق', 'initial': '\uFED7', 'medial': '\uFED8', 'final': '\uFED6'},
    'ك': {'isolated': 'ك', 'initial': '\uFEDB', 'medial': '\uFEDC', 'final': '\uFEDA'},
    'ل': {'isolated': 'ل', 'initial': '\uFEDF', 'medial': '\uFEE0', 'final': '\uFEDE'},
    'م': {'isolated': 'م', 'initial': '\uFEE3', 'medial': '\uFEE4', 'final': '\uFEE2'},
    'ن': {'isolated': 'ن', 'initial': '\uFEE7', 'medial': '\uFEE8', 'final': '\uFEE6'},
    'ه': {'isolated': 'ه', 'initial': 'ﻫ', 'medial': '\uFEEC', 'final': 'ﻪ'},
    'ة': {'isolated': 'ة', 'initial': 'ة', 'medial': '\uFE94', 'final': '\uFE94'},
    'و': {'isolated': 'و', 'initial': 'و', 'medial': 'ﻮ', 'final': 'ﻮ'},
    'ي': {'isolated': 'ي', 'initial': 'ﻳ', 'medial': '\uFEF4', 'final': 'ﻲ'},
    'ئ': {'isolated': 'ئ', 'initial': '\uFE8B', 'medial': '\uFE8C', 'final': 'ﺊ'},
    'ى': {'isolated': 'ى', 'initial': 'ﻳ', 'medial': '\uFEF4', 'final': 'ﻰ'},
    'ؤ': {'isolated': 'ؤ', 'initial': 'ؤ', 'medial': '\uFE86', 'final': '\uFE86'},
}