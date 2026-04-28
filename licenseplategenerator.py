import random
import string

a = str(random.randint(0,9))

b1 = random.choice(string.ascii_uppercase)
b2 = random.choice(string.ascii_uppercase)
b3 = random.choice(string.ascii_uppercase)
b = b1+b2+b3

c1 = str(random.randint(0,9))
c2 = str(random.randint(0,9))
c3 = str(random.randint(0,9))
c = c1+c2+c3

print(a + '-' + b + '-' + c)