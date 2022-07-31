import colorama as co

from tqdm import tqdm

import time

def generate_load_bar() -> None:
    co.init()
    green = co.Fore.GREEN
    yellow = co.Fore.YELLOW
    
    print(green + '\n\n\t\t <------TOKEN GENERATOR APP------------> \n\n')
    pbar = tqdm(total=50)
    for i in range(5):
        time.sleep(0.2)
        pbar.update(10)
    print(yellow)
    pbar.close()