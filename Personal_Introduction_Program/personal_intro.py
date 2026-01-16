# Personal Introduction Program

# Collect user input
name = input("What is your name? ")
age = input("How old are you? ")
hobby = input("What is your favorite hobby? ")

# Display personalized welcome message using f-strings
print("\n🎉 Welcome {0}! 🎉".format(name))
print(f"You are {age} years old and love {hobby}.")