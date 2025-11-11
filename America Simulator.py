import time
import random

# money in billions
america = 1
year = 1788
food = 1.001
yGDP = 11
GDP = 11
fedbudget = 1
population = 5300000
tariff = 0
canals = 0
healthf = 0.9995
frenchwar = 0
frenchwar2 = 0
frenchland = 0
sm = -1

while america == 1:
    if frenchwar == 1 and frenchland < 3:
        print("You are currently at war with France.")
        fedbudget -= 0.5
        frenchwar2 += 1
        if year >= 1813:
           print("You are winning the war due to your industrial capabilities.")
           frenchland += 1

        if year < 1813:
            print("The war appears to be a stalemate. Gains are small on both sides.")
            frenchland += random.randint(-1,1)

        print("French war status:", frenchland)

    if frenchwar == 0:
        #print("The war with france ended.")
        frenchwar2 = 0


    population = healthf * population
    GDP = yGDP
    fedbudget += GDP/100
    population = population * food
    year += 1
    print("year:", year)
    print("population:", population)
    print("GDP", GDP)
    print("budget", fedbudget)

    if year == 1820:
        print("DISPUTE   The northern states want a tariff on imports to compete with British industry, but southern states worry it will make things too expensive. If you pass the tariff (pt), your GDP will increase but your food production will decrease. If you don't pass the tariff, your GDP will decrease. If you build canals connecting northern and southern states (nsc), the food production penalty will not apply.")

    if year == 1813:
        print("ECONOMY   Northern states begin to adopt factories. The economy is majorly boosted.")
        yGDP += 7



    i = input("What will you do?")
    if i == "pt":
        food -= 0.01
        yGDP += 2
        tariff = 1
        print("You passed the tariff.")
    elif year > 1820 and tariff == 0:
        yGDP -= 4
        print("You didn't pass the tariff.")

    if i == "nsc":
        food += 0.01
        fedbudget -= 0.5
        print("You built canals, food production increases.")


    if i == "baf":
        fedbudget -= 0.75
        print("You bought the Lousiania Territory. You now produce more food and the economy grows further.")
        frenchland = 3

    if i == "waf" and frenchland < 3:
        frenchwar = 1
        print("You went to war with France.")
    elif i == "waf" and frenchland >= 3:
        print("You can't make war on your own territory.")

    if i == "paf" or frenchwar == 3 or frenchwar == -3:
        print("You made peace with France.")
        food += 0.006 * frenchland
        yGDP += 0.3 * frenchland
        if frenchland > 0:
            print("You won the war. The economy grows and you can produce more food.")
        if frenchland < 0:
            print("You lost the war. The economy suffered and you lost territory to grow food.")
        if frenchland == 0:
            print("You made no gains in the war.")
        if frenchland == 3:
            print("You completely won the war, taking all of the territory by force.")
        if frenchland == -3:
            print("You completely lost the war. America has fallen.")
            america = 0

    if yGDP < 0 or GDP < 0 or fedbudget < 0:
        print("You ran out of money. America has fallen.")
        america = 0


    time.sleep(0.1)
    i = 0
