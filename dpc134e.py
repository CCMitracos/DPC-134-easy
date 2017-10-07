# DPC 134 [E]
# N-Divisible Digits

# import math
# import random
# t = random.randrange(1,10)
# N = random.randrange(1,10)
# M = random.randrange(2,10**t)

N = int(raw_input("N >> "))
M = int(raw_input("M >> "))

x = ((10**N-1)/M)*M

if (x == 0):
  print "no solution"
else:
  print x
