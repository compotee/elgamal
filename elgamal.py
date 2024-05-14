import random


# Алгоритм кодирования
def elgamal_coding(coded_text, p, y, g):
    encoded_list = []

    k = random.randint(1, p - 1) # Случайный сессионный ключ
    a = g ** k % p  # Первая часть шифротекста
    b = y ** k % p  # Вторая часть шифротекста

    # Далее каждый символ строки мы умножаем на вторую часть шифротекста
    # и получаем лист с зашифрованными символами
    for i in range(0, len(coded_text)):
        encoded_list.append(b * ord(coded_text[i]))

    return a, encoded_list


# Алгорим расшифрования
def elgamal_decoding(encoded_list, a, x, p):
    decoded_list = []

    k = a ** x % p  # Величина, на которую будем делить каждый закодированный символ

    # Проходим по всему листу и делим на найденную величину
    for i in range(0, len(encoded_list)):
        decoded_list.append(chr(int(encoded_list[i] / k)))

    return ''.join(decoded_list)


if __name__ == '__main__':
    p = random.randint(1, pow(2, 12))  # Случайное число, часть открытого ключа
    g = random.randint(1, p)  # Первообразный корень p, часть открытого ключа
    x = random.randint(1, p - 1)  # Закрытый ключ
    y = g ** x % p  # Часть открытого ключа

    input_text = input("Введите текст: ")

    a, encoded_text = elgamal_coding(input_text, p, y, g)
    decoded_text = elgamal_decoding(encoded_text, a, x, p)

    print("Закодированный текст: ", *encoded_text)
    print("Раскодированный текст:", decoded_text)
