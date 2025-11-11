import time

x = 0
y = 0
VV = 10
HV = 0.5



while True:
    y = VV + y
    x = HV + x
    VV = VV -0.98
    print(x)
    print(y)
    time.sleep(0.1)
