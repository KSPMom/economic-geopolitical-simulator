year = 1946
week = 1

# Regions

# US variables
USA_pop = 141390000
USA_food = 174
USA_raw = 212
USA_oil = 40
USA_steel = 204
USA_facto = 297

# Russia variables
RUS_pop = 100000000
RUS_epop = 0
RUS_food = 55 #5
RUS_raw = 100
RUS_oil = 79
RUS_steel = 186
RUS_facto = 184

# Ukraine variables
UKR_pop = 27400000
UKR_epop = 0
UKR_food = 76 # 15
UKR_raw = 20
UKR_oil = 0
UKR_steel = 36
UKR_facto = 16




# States

# US (state) variables
s_USA_owned = [True,False,False]


s_USA_pop = 0
s_USA_food = 0
s_USA_raw = 0
s_USA_oil = 0
s_USA_steel = 0
s_USA_facto = 0

s_USA_epop = 0
s_USA_food_R = 0
s_USA_raw_M = 0
s_USA_facto_U = 0
s_USA_weap = 8000000
s_USA_army = 1400000
s_USA_tract = 1566000
s_USA_stability = 85


# Resource collective function

def add_region(state, ID):
    if state == "USA":
        if ID == 0:
            global s_USA_pop
            global s_USA_food
            global s_USA_raw
            global s_USA_oil
            global s_USA_steel
            global s_USA_facto
            s_USA_pop = 0
            s_USA_food = 0
            s_USA_raw = 0
            s_USA_oil = 0
            s_USA_steel = 0
            s_USA_facto = 0
            s_USA_pop += USA_pop
            s_USA_food += USA_food
            s_USA_raw += USA_raw
            s_USA_oil += USA_oil
            s_USA_steel += USA_steel
            s_USA_facto += USA_facto






while True:

    for i in s_USA_owned:
        if s_USA_owned[i] == True:
            add_region("USA", i)

    Input = "george orwell"
    s_USA_epop = 0
    for x in range(s_USA_army):
        if s_USA_epop < s_USA_pop:
            s_USA_epop += 1
    s_USA_facto_U = 0
    s_USA_food_R = 0
    s_USA_raw_M = 0
    s_USA_tract_B = s_USA_tract

    print("Population:", s_USA_pop)
    print("Assigned population:", s_USA_epop)
    print("Factories:", s_USA_facto)
    print("Factories in use:", s_USA_facto_U)
    print("Food:", s_USA_food)
    print("Raw materials:", s_USA_raw)



    while not Input == "step":
        Input = input("Enter command:")


        # Allocation of population/factories etc. to work

        if Input == "allo pop farming tract": # Employ farmers function (with tractors)
            for x in range(s_USA_food, 0, -1):
                if s_USA_epop < s_USA_pop:
                    s_USA_food_R += 1
                    if s_USA_tract_B > 0:
                        s_USA_epop += 90000
                        s_USA_tract_B -= 1
                    else:
                        s_USA_epop += 900000

            s_USA_tract_B = s_USA_tract

        if Input == "allo pop farming": # Employ farmers function
            for x in range(s_USA_food, 0, -1):
                if s_USA_epop < s_USA_pop:
                    s_USA_food_R += 1
                    s_USA_epop += 900000

            s_USA_tract_B = s_USA_tract

        if Input == "allo pop manu facto": # Employ consumer goods workers function (with factories)
            for x in range(s_USA_raw, 0, -1):
                if s_USA_epop < s_USA_pop:
                    s_USA_raw_M += 1
                    if s_USA_facto_U < s_USA_facto:
                        s_USA_epop += 500000
                        s_USA_facto_U += 1
                    else:
                        s_USA_epop += 5000000

        if Input == "allo pop manu": # Employ consumer goods workers function
            for x in range(s_USA_raw, 0, -1):
                if s_USA_epop < s_USA_pop:
                    s_USA_raw_M += 1
                    s_USA_epop += 5000000

        if Input == "allo factopop milit": # Employ military equipment producers
            for x in range(s_USA_steel, 0, -1):
                if s_USA_facto_U < s_USA_facto:
                    s_USA_weap += 100
                    s_USA_epop += 500000
                    s_USA_facto_U += 1

        print("Population:", s_USA_pop)
        print("Assigned population:", s_USA_epop)
        print("Factories:", s_USA_facto)
        print("Factories in use:", s_USA_facto_U)
        print("Food:", s_USA_food)
        print("Raw materials:", s_USA_raw)

    # Stability code
    if s_USA_pop > s_USA_food_R * 1000000:
        s_USA_stability += (s_USA_food_R * 1000000 - s_USA_pop) / s_USA_pop * 100
    s_USA_pop += s_USA_food_R * 1000000 - s_USA_pop

    s_USA_stability -= (3 - 1000000 * s_USA_raw_M / s_USA_pop) * 10


    # Time Update
    week += 1
    if week > 52:
        week = 1
        year += 1

