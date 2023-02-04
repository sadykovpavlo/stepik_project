from random import choice


def random_string():
    list_of_symbols = ['a', 'b', 'c', 'd', 'e', '1', '2', '3', '4', '5', 'F', 'N', 'U', 'O', 'N']
    pre_password = []
    password = ''

    while True:
        symbol = choice(list_of_symbols)
        pre_password.append(symbol)
        if len(pre_password) == 9:
            break

    if pre_password:
        for word in pre_password:
            password += word

    return password
