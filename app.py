import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'
special = '!@#$%&*_./+-'

strings = lower + upper + nums + special
length = 16

password = "".join(random.sample(strings, length))

print(password)
