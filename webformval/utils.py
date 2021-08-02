import re


def type_v(v):
    test = {'email': r'^\S+@\w+.\w{2,4}$',
            'date': r'^\d\d\.\d\d\.\d{4}$',
            'phone': r'^79\s*\d{2}\s*\d{3}\s*\d{2}\s*\d{2}$',
            }
    for t, r in test.items():
        if re.fullmatch(r, v):
            return t

    return 'text'


def form_type(d):
    res = {}
    d = d.dict()
    for k, v in d.items():
        res[k] = type_v(v)
    return res