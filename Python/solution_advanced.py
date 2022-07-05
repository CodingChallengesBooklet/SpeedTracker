# Does all of our calculations for us
import solution

number_plate = input("Please enter the number plate of the vehicle: ")
number_plate = number_plate.replace(" ", "")

valid = False

print(f"The car was travelling {solution.answer} mph")

if len(number_plate) != 7:
    print(f"Vehicle number plate is not correct length!")
elif number_plate[0].isalpha() and \
        number_plate[1].isalpha() and \
        number_plate[2].isdigit() and \
        number_plate[3].isdigit() and \
        number_plate[4].isalpha() and \
        number_plate[5].isalpha() and \
        number_plate[6].isalpha():
    print(f"Vehicle number plate \"{number_plate}\" is valid!")
    valid = True
else:
    print(f"Vehicle number plate \"{number_plate}\" is invalid!")



