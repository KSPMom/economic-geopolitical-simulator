import time
x = 1
y = 2
z = 1
while True:
    print(x, "gold bars")
    time.sleep(1)
    z = z/y
    x += z
    y += 1