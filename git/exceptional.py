def convert(s):
    DIGIT_MAP = {'zero':'0', 'one':'1', 'two':'2',}
    number = ''
    for token in s:
        number += DIGIT_MAP[token]
    x = int(number)
    return x
    
    
    
    
    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        x = int(number)
        print(f'Conversion succeeded! x = {x}')
    except (KeyError, TypeError):
        print(f'Conversion failed!')
        x = -1
    return x
DIGIT_MAP = dict(zero=0, un=1, deux=2, trois=3, quatre=4, cinq=5, six=6, sept=7, huit=8, neuf=9, ten=10)