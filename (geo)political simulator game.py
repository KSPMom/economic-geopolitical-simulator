year = 1946
week = 1

# Regions

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

# US variables
USA_pop = 141390000
USA_epop = 0
USA_food = 174
USA_food_R = 0
USA_raw = 212
USA_raw_M = 0
USA_oil = 40
USA_steel = 204
USA_facto = 297
USA_facto_U = 0

# States

# US (state) variables
s_USA_weap = 8000000
s_USA_army = 1400000
s_USA_tract = 1566000
s_USA_stability = 85
#s_USA_warsup = 35



while True:

    Input = "george orwell"
    USA_epop = 0
    for x in range(s_USA_army):
        if USA_epop < USA_pop:
            USA_epop += 1
    USA_facto_U = 0
    USA_food_R = 0
    USA_raw_M = 0
    s_USA_tract_B = s_USA_tract

    print("Population:", USA_pop)
    print("Assigned population:",USA_epop)
    print("Factories:",USA_facto)
    print("Factories in use:",USA_facto_U)
    print("Food:",USA_food)
    print("Raw materials:",USA_raw)



    while not Input == "step":
        Input = input("Enter command:")


        # Allocation of population/factories etc. to work

        if Input == "allo pop farming tract": # Employ farmers function (with tractors)
            for x in range(USA_food, 0, -1):
                if USA_epop < USA_pop:
                    USA_food_R += 1
                    if s_USA_tract_B > 0:
                        USA_epop += 90000
                        s_USA_tract_B -= 1
                    else:
                        USA_epop += 900000

            s_USA_tract_B = s_USA_tract

        if Input == "allo pop farming": # Employ farmers function
            for x in range(USA_food, 0, -1):
                if USA_epop < USA_pop:
                    USA_food_R += 1
                    USA_epop += 900000

            s_USA_tract_B = s_USA_tract

        if Input == "allo pop manu facto": # Employ consumer goods workers function (with factories)
            for x in range(USA_raw, 0, -1):
                if USA_epop < USA_pop:
                    USA_raw_M += 1
                    if USA_facto_U < USA_facto:
                        USA_epop += 500000
                        USA_facto_U += 1
                    else:
                        USA_epop += 5000000

        if Input == "allo pop manu": # Employ consumer goods workers function
            for x in range(USA_raw, 0, -1):
                if USA_epop < USA_pop:
                    USA_raw_M += 1
                    USA_epop += 5000000

        if Input == "allo factopop milit": # Employ military equipment producers
            for x in range(USA_steel, 0, -1):
                if USA_facto_U < USA_facto:
                    s_USA_weap += 100
                    USA_epop += 500000
                    USA_facto_U += 1

        print("Population:", USA_pop)
        print("Assigned population:", USA_epop)
        print("Factories:", USA_facto)
        print("Factories in use:", USA_facto_U)
        print("Food:", USA_food)
        print("Raw materials:", USA_raw)

    # Stability code
    if USA_pop > USA_food_R * 1000000:
        s_USA_stability += (USA_food_R * 1000000 - USA_pop) / USA_pop * 100
    USA_pop += USA_food_R * 1000000 - USA_pop

    s_USA_stability -= (3 - 1000000*USA_raw_M/USA_pop)*10


    # Time Update
    week += 1
    if week > 52:
        week = 1
        year += 1

