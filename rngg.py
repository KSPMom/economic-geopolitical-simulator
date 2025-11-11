import random

a = random.randint(1, 3)
g = input()
g2 = int(g)
if a == g2:
    print('win')
else:
    print('loss, it was:')
    print(a)