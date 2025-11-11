import random
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0
ten = 0
eleven = 0
pick = 0
generations = 0
loop = 1

while loop<99:
    while one==0 or two==0 or three==0 or four==0 or five==0 or six==0 or seven==0 or eight==0 or nine==0 or ten==0 or eleven==0:
        pick = random.randint(1, 11)
        if pick == 1:
            one = 1
        if pick == 2:
            two = 1
        if pick == 3:
            three = 1
        if pick == 4:
            four = 1
        if pick == 5:
            five = 1
        if pick == 6:
            six = 1
        if pick == 7:
            seven = 1
        if pick == 8:
            eight = 1
        if pick == 9:
            nine = 1
        if pick == 10:
            ten = 1
        if pick == 11:
            eleven = 1
        generations = generations + 1
    print(generations)
    loop = loop + 1
    one = 0
    two = 0
    three = 0
    four = 0
    five = 0
    six = 0
    seven = 0
    eight = 0
    nine = 0
    ten = 0
    eleven = 0
    pick = 0
    generations = 0



