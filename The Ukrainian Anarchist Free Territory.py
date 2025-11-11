import random
import time

print("After the stalemate of both sides in the Russian Civil War and the collapse of Russia into many warlord states, one state has stood out in particular, the Ukrainian Anarchist Free Territory. Although originally two states, the people of Ukraine have decided by popular vote to unite under one anarchist pseudo-state. The territory does not have an official leader, only the General Assembly, a congress of elected leaders from communes around the federation, the People's Council, a council of seven people elected by the General Assembly responsible for managing the administrative state, and the Security Council, a government branch in charge of the military ultimately subservient to the People's Council and General Assembly. You now must guide this budding federation to freedom from the ashes of the First World War against the tyranny of capitalists, the bolsheviks, monarchists, and a vengeful Germany. Do you have what it takes to guide the people of the world to freedom?")

year = 1921
month = 1
economy = 3000
ecotype = "nationalized"
army = 17000
state_existence = 10



while True:
    print("Year:",year)
    print("Month:",month)
    print("economy =",economy)
    print("army =",army,"soldiers")
    print("strength of the state:",state_existence,"/ 10")
    if year == 1921 and month == 1:
        print("Peace has at last come to the Ukrainian Anarchist Free Territory with the collapse of both sides of the Russian Civil War. It is now a time to rebuild and prepare for the next attack from any statist force. To our north is the Union of Soviet Republics, lead by Leon Trotsky, and to our west is the Republic of West Russia. To our east is Poland and to our south-east is Romania. The economy is largely in ruin and the people's conditions are horrible. The government remains largely centralized and the state is nowhere near abolished, even disregarding the military's necessary existence, however elections are due to be held in June. ")
        print("Below are a list of commands for this game:")
        print("privatize - switches the country to a socialist market economy, still keeping workers in control, but allowing a market economy; this moves your country further from the abolition of the state but increases economic growth")
        print("nationalize - switches the country back to a command economy, moving your country further from the abolition of the state but decreasing economic growth [on by default]")
        print("war [country name] - goes to war with a country, this can only be a country you border")
        print("invest - slightly increases economic growth for a month")
        print("communalize - uses money to decrease the strength of the state; is more effective when the quality of life is high")
        print("recruitment - recruits soldiers to strengthen the army, increases the strength of the state")






    i = input("What will you do?")
    if i == "privatize":
        if ecotype == "privatized":
            print("Economy already privatized.")
            i = "0"
        else:
            print("Economy privatized")
            ecotype = "privatized"
            state_existence += 1
            i = "0"

    if i == "nationalize":
        if ecotype == "nationalized":
            print("Economy already nationalized.")
            i = "0"
        else:
            print("Economy nationalized.")
            ecotype = "nationalized"
            state_existence -= 1
            i = "0"

    #insert war code here

    if i == "invest":
        print("Invested in the economy.")
        economy *= 1.03
        i = "0"

    if i == "communalize":
        print("Communalized society.")
        i = "0"
        if economy < 4000:
            state_existence -= 1
            economy -= 1000
        else:
            state_existence -= 2
            economy -= 1000


    if i == "recruitment":
        print("Recruited soldiers into the army.")
        i = "0"
        army += 1000
        state_existence += 1


    #election code
    if month == 6:
        print()
        # elections happen

    if ecotype == "privatized":
        economy *= 1.05

    if ecotype == "nationalized":
        economy *= 1.015


    #year advancement code
    month += 1
    if month > 12:
        month = 1
        year += 1

    #checks if state strength is out of bounds
    if state_existence < 0:
        state_existence = 0

    if state_existence > 10:
        state_existence = 10