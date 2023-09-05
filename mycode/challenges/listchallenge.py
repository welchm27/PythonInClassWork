#!/usr/bin/python3

def main():
    heroes = ["Spiderman", "Batman", "Black Panther", "Wonder Woman", "Storm"]

    # PART 1
    # Print out your favorite character from this list! The output would look something like:
    # My favorite character is Black Panther!
    print(f"My favorite character is {heroes[1]}!")

    # PART 2
    # Ask the user to pick a number between 1 and 100.
    # Convert the input into an integer.
    user_num = int(input("Pick a number between 1 and 100: \n"))


    nums= [1, -5, 56, 987, 0]

    # PART 3
    # check out https://docs.python.org/3/library/functions.html or go to Google
    # use a built-in function to find which integer in nums is the biggest.
    # then, print out that number!
    biggest_num = max(nums)
    print(f"The largest number in the nums list is: {biggest_num}")

if __name__ == "__main__":
    main()
