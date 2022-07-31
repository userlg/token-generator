

def menu() -> str:
    option = 'P'

    while (option != '1' and option != '2' and option != '3' and option != '4'):
      print('\n\t\t<<--------MENU------------------>>\n')
      print('\n\t 1: Store token in a file ')
      print('\n\t 2: Generate token without file ')
      print('\n\t 3: View stored tokens ')
      print('\n\t 4: Exit')
      option = input('\t---->')

    return option