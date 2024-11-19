import random 

lower = "abcdefghijklmnopqrstuvxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,._-***"

all = lower + upper + numbers + symbols
lenght = 15
password = "".join(random.sample(all,lenght))

print(password)
