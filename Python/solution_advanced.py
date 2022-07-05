# Does all of our calculations for us
import solution

# Get number plate from user and removes any spaces that may be in it
number_plate = input("Please enter the number plate of the vehicle: ")
number_plate = number_plate.replace(" ", "")

# Display car speed from solution.py
print(f"The car was travelling {solution.answer} mph")

# Validate the length of the number plate is correct
if len(number_plate) != 7:
    print(f"Vehicle number plate is not correct length!")

# Here we check if the number plate follows the pattern: 2 letters, 2 numbers, and 3 letters after.
# NOTE: isalpha() returns true if string is a letter, and isdigit() returns true if string is a number.
elif number_plate[0].isalpha() and \
        number_plate[1].isalpha() and \
        number_plate[2].isdigit() and \
        number_plate[3].isdigit() and \
        number_plate[4].isalpha() and \
        number_plate[5].isalpha() and \
        number_plate[6].isalpha():
    print(f"Vehicle number plate \"{number_plate}\" is valid!")
else:
    print(f"Vehicle number plate \"{number_plate}\" is invalid!")



