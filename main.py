from pyparsing import Word
from token_generator_module import generate_token, check_word

from datetime import datetime as dt

def main() -> None:
    print("\t\t<<-------Token Generator-------->>\n")
    now = str(dt.now())
    print("\t\t Date: " + now + "\n")


    word = ''
    while(len(word) < 6):
        word = input('Introduzca palabra o expresion (Debe contener min 6 caracteres) \n\t')

    token = generate_token(word)
    print(token)

    if (check_word(word,token)):
        print('Cifrado funciona correctamente')


if __name__ == '__main__':
    main()