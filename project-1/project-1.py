#!/usr/bin/env python3

def main():
    anime_isekai = [
        "re:ZERO - Starting life in another world",
        "Mushoku Tensei: Jobless Reincarnation",
        "Handyman Satou (KunoSuba)",
        "Overlord"
        ]
    anime_normal = [
        "Jujutsu Kaisen",
        "Naruto",
        "Demon Slayer",
        "Black Clover"
        ]
    games_sandbox = ["Satisfactory", "Craftopia", "Terraria", "Valheim", "7 Days to Die", "Conan Exiles", "No Man's Sky", "SCUM", "Space Engineers"]
    games_shooters = ["Call of Duty", "Halo Infinite", "Planetside 2", "PUBG", "DayZ"]
    games_survival = ["Satisfactory", "Kingdom Come: Deliverance", "Stranded: Alien Dawn", "Valheim", "7 Days to Die", "DayZ", "SCUM"]
    games_rpg = ["Skyrim", "Hogwarts Legacy", "Elex 1 or 2", "Cyberpunk 2077", "Elden Ring", "Pathfinder", "Starbound", "XCOM 2"]
    games_casual = ["Bloons TD6", "CardLife", "Terraria"]
    
    in_bored = input("Are you bored and looking to find something to do? (Yes or No) ")
    if in_bored.lower() not in ["yes", "no"]:
        in_bored = input("Please enter 'Yes' or 'No': ")
    if in_bored.lower() == "yes":
        print("yes")
        print("Would you be more interested in watching Anime or playing games? ")
    elif in_bored.lower() == "no":
        print("no")
    else:
        print("Well then you don't need me, goodbye")

if __name__ == "__main__":
    main()