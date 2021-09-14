from time import sleep
import random
from tqdm import tqdm


def random_sleep(start: int=3 , stop: int=15, desc: str='Loading...'):
    end = random.randint(start, stop)
    for _ in tqdm(range(0, end), desc=f'{desc}, {end} sec.', ascii=False):
        sleep(1)

def time_sleep(seconds: int):
    while True:
        sec = f'Remine time: {seconds} seconds. '
        print(sec, end='')
        print('\b' * len(sec), end='', flush=True)
        seconds -= 1
        sleep(1)
        if seconds == 0:
            break

