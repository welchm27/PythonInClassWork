#!/usr/bin/env python3

# You will need to install pyfiglet using:
# pip install pyfiglet

def main():
    import random
    # importing pyfiglet module
    import pyfiglet

    welcome = pyfiglet.figlet_format("WELCOME TO MY SIMPLE GAME! HOW LONG CAN YOU SURVIVE")
    print(welcome)

    player_health = 100
    enc_res = " "
    roll_res = " "
    run_fight_dec = "do you 'Run' or 'Fight'? "
    dec1 = "Do you choose to go 'North' or 'South'? "
    n_enc1 = "You come upon a bugbear, " + run_fight_dec
    n_enc2 = "You come upon a pack of wolves, " + run_fight_dec
    n_enc3 = "You come upon a troll, " + run_fight_dec

    s_enc1 = "You come upon a burning town full of monsters, you're immediately surrounded with nowhere to run"


    def rand_roll():
        roll = random.randint(1,20)
        if roll > 10:
            roll_res == "high"
        else:
            roll_res == "low"
        print("You rolled a " + str(roll))

    def enc_roll():
        roll = random.randint(1,20)
        if roll > 10:
            print(roll)
            # got away
            enc_res = "run" 
        else:
            print(roll)
            # didn't get away
            enc_res = "fight"
    
    def enc_result():
        if enc_res == "run":
            input("You made it without taking damage")
        else:
            input("You got hit in your escape")
            roll_damage()
    
    def roll_damage():
        roll = random.randint(1,20)
        if roll == 20:
            damage = random.randint(1,20) * 2
        else:
            damage = random.randint(1,20)
        
    def attacked(dmg):
        roll_damage()
        damage_taken = roll_damage()
        print("Damage taken:", damage_taken)
        dmg = damage_taken
        
    def run_fight(enc, player_health):
        if enc.lower() == "run":
            rand_roll()
            if roll_res == "high":
                input("You got away, good job")
            else:
                input("You didn't get away")
                roll_damage()
                damage_taken = roll_damage()
                print("Damage taken:", damage_taken)
                player_health -= damage_taken
        else:
            input("Fight?!?! WITH WHAT?")
            while player_health > 0:
                input("Press Enter to see how much damage you take")
                roll_damage(dmg)
                dmg = dmg
                damage_taken = dmg
                player_health -= damage_taken
                print("Damage taken:", damage_taken, "Current health: ", player_health)


    while player_health > 0:
        print("Player Health: ", player_health)
        input("Hit enter to move to the next step")
        input("You wake up in a field with a splitting headache")
        input("Looking around you see a forest to the North, and smoke rising from a town to the South")
        
        dec1 = input(dec1)
        # if North or South aren't chosen, continue asking
        while dec1.lower() not in ["north", "south"]:
            dec1 = input("Please choose 'North' or 'South': ")

        # if North is chosen...
        if dec1.lower() == "north":
            enc1 = input(n_enc1)
            # if invalid choice, keep asking
            while enc1.lower() not in ['run', 'fight']:
                enc1 = input("Please choose 'Run' or 'Fight': ")
            # if run is chosen, roll
            run_fight(enc1, player_health)
            # if enc1.lower() == "run":
            #     rand_roll()
            #     if roll_res == "high":
            #         input("You got away, good job")
            #         # add a second decision
            #     else:
            #         input("You didn't get away")
            #         roll_damage()
            #         damage_taken = roll_damage()
            #         print("Damage taken:", damage_taken)
            #         player_health -= damage_taken
            # else:
            #     input("Fight?!?! WITH WHAT?")
            #     while player_health > 0:
            #         input("Press Enter to see how much damage you take")
            #         roll_damage()
            #         damage_taken = roll_damage()
            #         player_health -= damage_taken
            #         print("Damage taken:", damage_taken, "Current health: ", player_health)
                    
                    
                

        # if South is chosen...
        else:
            input("You see a city on fire...")
            attacked()
            player_health -= damage_taken
            print("Damage taken:", damage_taken, "Current health: ", player_health)

    print("Game Over. Player defeated!")


if __name__ == "__main__":
    main()