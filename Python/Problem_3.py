# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


import time

start_time = time.time()

# solution code
def is_a_prime(i):
    for x in range(2, int(i**0.5)+1):
        if i % x == 0:
            return False
    return True

num = 600851475143
for x in range(1, num):
    if num % x == 0 and is_a_prime(x):
        print(x)
    
time_to_run = time.time() - start_time, 'seconds'

print(time_to_run)
