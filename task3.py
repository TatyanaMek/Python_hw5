# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

#stroka = "aaabbbbccbbb"
#....
#stroka = "3a4b2c3b"

def coding(text):
    if len(text) < 1:
        return ''
    count = 0
    el = text[0]
    result = ''
    for elem in text:
        if elem == el:
            count += 1
        else:
            result += str(count) + el
            count = 1
            el = elem
    else:
        result += str(count) + el
    return result

def decording(text: str) -> str:
    if len(text) < 1:
        return ''
    num = ''
    result = ''
    for elem in text:
        if elem.isdigit():
            num += elem
        else:
            for i in range(int(num)):
                result += elem
            else:
                num = ''
    return result

print('Кодирование')
print(coding('aaabbbbccbbb'))
print('Декодирование')
print(decording('3a4b2c3b'))