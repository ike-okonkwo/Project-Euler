# Project Euler
#
# March 3 2010
#
#
# Problem 1
#
#  If we list all the natural numbers below 10 that are multiples 
#  of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#  Find the sum of all the multiples of 3 or 5 below 1000.




import time

start_time = time.time()

# soluton
t_sum = 0

for x in range(1, 1000):
    if x % 3 == 0 or x % 5 == 0:
        t_sum = t_sum + x
   
print(t_sum)

time_to_run =  time.time() - start_time, 'seconds'

print(time_to_run)






