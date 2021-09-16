import random
import time


if __name__ == '__main__':
    start_aft = random.randint(1800, 10800)
    print("Start \"Click 315\" after " + str(start_aft) + " second")
    time.sleep(start_aft)
