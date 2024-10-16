import time
import random

numbers = [0] * 70

while True:
    
    print("\r" + ' '.join(map(str, numbers)), end='', flush=True)
    
    time.sleep(random.uniform(0.002, 0.008))

    index = random.randint(0, len(numbers) - 1)

    if numbers[index] < 9:  

        numbers[index] += 1
    
        print("\r" + ' '.join(map(str, numbers)), end='', flush=True)

        time.sleep(random.uniform(0.002, 0.008))


    if all(num == 9 for num in numbers):
        break
