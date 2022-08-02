from progress_bar import generate_load_bar

from modules import menu, yellow, encrypt_operation, generate_file

from datetime import datetime as dt

import time

def main() -> None:
    generate_load_bar()
    now = str(dt.now())
    print("\t\t Date: " + now + "\n")
    option = 'P'
    
    while (option != '4'):

       option = menu()

       if option == '1':
         generate_file(encrypt_operation())

       if (option == '2'):
        encrypt_operation()
          
    
    print(yellow + '\t\t  Thanks for use this application, see ya!!')
    time.sleep(5)


if __name__ == '__main__':
    main()