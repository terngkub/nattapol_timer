import time
from datetime import datetime, timedelta
import os
import chime
import sys
import argparse


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('duration', nargs='?', default=25, type=int)
    args = parser.parse_args()

    dur = timedelta(minutes=args.duration)
    beg = datetime.now()
    end = beg + dur
    beg_str = beg.strftime("%H:%M:%S")
    end_str = end.strftime("%H:%M:%S")

    now = datetime.now()
    while now < end:
        clear_screen()
        delta = end - now
        minutes, seconds = divmod(delta.seconds, 60)
        print(f'Session {beg_str} - {end_str}')
        print(f'Time Left: {minutes:02d}:{seconds:02d}')
        time.sleep(1)
        now = datetime.now()

    chime.theme('zelda')
    chime.success()
    time.sleep(3)


if __name__ == '__main__':
    sys.exit(main())