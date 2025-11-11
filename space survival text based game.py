import time
import random

money = 1000000000
repair_cost = 0
crewmembers = 2
C02S = 6
water = 3
food = 90
alt = 425
fuel = 100
capsule_presense = "present"
debris_strike_timer = random.randint(20,700)
launch_timer = 0
event_timer = 0
water_timer = 0
print("You are the director of the Internation Space Exploration Union's Space Station One project.")
time.sleep(0.5)
print('You have' , money , 'dollars per year to spend.')
time.sleep(0.5)
print("Your station is designed to support 2 crew members and complete science experiments. It has two docking ports and two solar panels attached to the main core.")
time.sleep(0.5)
print("A craft can dock to your station every 2 and a half months to resupply your station. Your crew's capsule is docked to the other port and can be used to return to Earth.")
time.sleep(0.5)
print('Good luck.')
time.sleep(2)
print('Status: crew:', crewmembers, '|CO2 scrubbers (1 lasts for 2 weeks) (releases oxygen):', C02S,
              '|water (in days) (recycled unless recycler breaks down):', water, '|food (in days):', food,
              '|station altitude (in kilometers):', alt, '|station fuel (in %)', fuel, '|next launch in',
              (60 - launch_timer), 'days')

while True:

    if event_timer == 5:
        event_timer = 0
        launch_timer += 1
        time.sleep(1)
        alt -= 0.1
        C02S -= (0.036*crewmembers)
        food -= (0.5*crewmembers)
        waterRbr = random.randint(1,500)
        if waterRbr == 1:
            if water>2:
                water_timer = 1
                repair_cost += 10000
                print('Your water recycler broke down! It will cost', repair_cost, 'dollars to replace and the spare will come with the next resupply craft.')
                print('You will have to evacuate your crew when you run out of water.')
        if water == 0:
            print('Your crew had to evacuate because they ran out of water. They will come back on the next resupply craft.')
            print('However, it will cost 5 million more dollars to send them on the next launch.')
            crewmembers = 0
            water_timer = 0
            water -= 1
        if water_timer == 1:
            water -= 1
        print('CO2 scrubbers:', C02S,
              '|water (in days):', water, '|food (in days):', food,
              '|station altitude (in kilometers):', alt, '|station fuel (in %)', fuel, '|next launch in',
              (60 - launch_timer), 'days |crew:', crewmembers,)

    if launch_timer == 60:
        launch_timer = 0
        print("A resupply craft arrived.")
        food += 61
        C02S += 4
        if fuel < 20:
            fuel += 50
            repair_cost += 1000000
            money -= 80000000 + repair_cost
            repair_cost = 0
            if crewmembers == 0:
                crewmembers = 2
                money -= 5000000
                water += 4



    if debris_strike_timer < 0:
        print("WARNING! A debris strike will hit your station in 10 minutes. You can move out of the way, but it will cost 5% of your station's fuel.")
        print("Otherwise you can evacuate your station. Type 'boost' to move out of the way, or type 'evacuate' to evacuate.")
        i = input('Evacuate or boost?')
        if i == 'evacuate':
            print('You evacuated. Your crewmembers have left, but the debris will still damage your station')
            crewmembers = 0
        if i == 'boost':
            if fuel >= 5:
                print('You boosted the station. This cost 5% of your fuel.')
                fuel -= 5
                debris_strike_timer = random.randint(200, 700)
            else:
                print("You don't have enough fuel, evacuating now. The debris will still damage your station.")
                crewmembers = 0
                print("The next launch will refuel your station by 50%.")

    if debris_strike_timer < -5:
        print('The debris field hit your station.')
        debris_strike_timer = random.randint(200, 700)
        repair_cost = random.randint(1000,20000000)
        print('It will cost' , repair_cost , 'extra dollars to repair your station on the next launch, which will bring new crewmembers.')

    if alt < 350:
        print("WARNING! Your station has dropped to 350 kilometers. You can boost your station, but it will cost 5% of your station's fuel.")
        print("Otherwise you can evacuate your station. Type 'boost' to move out of the way, or type 'evacuate' to evacuate.")
        i = input('Evacuate or boost?')
        if i == 'evacuate':
            print('You evacuated. Your crewmembers have left, but your station is still falling.')
            crewmembers = 0
        if i == 'boost':
            if fuel >= 5:
                print('You boosted the station. This cost 5% of your fuel.')
                fuel -= 5
                alt += 75
            else:
                print("You don't have enough fuel, evacuating now.")
                crewmembers = 0
                print("The next launch will refuel your station by 50%.")

    if alt < 130:
        print("Your station has fallen to far into the atmosphere and fell down to Earth.")
        print("Game over.")
        break


    event_timer += 1
    debris_strike_timer -= 1
    time.sleep(1)