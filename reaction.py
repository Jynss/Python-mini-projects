import time
import random

while True:
    pause_time = random.uniform(2, 5)
    start_time = time.time()
    end_time = start_time + pause_time
    print('Wait...')
    prompt_time = time.time()
    while prompt_time < end_time:
        prompt_time = time.time()
    input('Press enter!!!\n')
    click_time = time.time()
    react_time = click_time - prompt_time
    print('Your reaction time is %.4f seconds' % react_time)
    input('Press enter to play again\n')
