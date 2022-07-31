from pyparsing import Word
from token_generator_module import generate_token, check_word

from progress_bar import generate_load_bar

from modules import menu

from datetime import datetime as dt

import time

def main() -> None:
    generate_load_bar()
    now = str(dt.now())
    print("\t\t Date: " + now + "\n")
    option = 'P'
    
    while (option != '4'):

       option = menu()

       if (option == '2'):
          word = ''
          while(len(word) < 6):
             word = input('Introduzca palabra o expresion (Debe contener min 6 caracteres) \n\t')

          token = generate_token(word)
          print(token)

          if (check_word(word,token)):
             print('Cifrado funciona correctamente')
    
     
    print('\t\t  Thanks for use this application, see ya!!')
    time.sleep(5)


if __name__ == '__main__':
    main()