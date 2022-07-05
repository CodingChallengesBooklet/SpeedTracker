# Speed Tracker using Python
In this code challenge we write a program to calculate the speed of a car.

## Problem
Create a program that takes a time for a car going past a speed camera, the time going past the next one and the distance between them to calculate the average speed for
the car in mph. The cameras are one mile apart.

## Solution
To easily explain how we'll calculate the speed of the car I will use an example. 
Assuming the following,
1. First speed camera sees the car at 12:00:00 
2. Second speed camera sees the car at 12:05:00
3. The speed cameras are 1 mile apart.

We would first get the difference between the two times: 12:05:00 - 12:00:00 = 00:05:00 (5 minutes).
Now we could calculate the speed using hours, minutes, and seconds but that is quite complicated.
Instead we will convert all times into seconds to simplify our process.
5:00 is 300 seconds. Now since we are calculating mph (miles per hour) we want to find the number of 5 minutes in 1 hour.
1 hour in seconds is 3600. We will then multiply the result by the number of miles between the two cameras.
```
distance between the cameras = 1 mile
5 minutes = 300 seconds
1 hour = 3600 seconds
3600/300 = 12
12 * 1 = 12 mph (miles per hour)
```

### Solving the problem
Now we have an example you should understand the processes of the calculation. We should generalise so we can use any value.
```python
# Generalised solution
3600/time_difference * miles_apart
```
It's also important to note we should round this as in most programming languages this will result in a floating point number.
The problem states the cameras are 1 mile apart but we could make our program better by getting the distance from user input which allows the distance apart to be anything.

```python
# We import datetime so we can easily convert our user input 
# into a time format like Hours:Minutes:Seconds
from datetime import datetime

# Get start time input and format it into a Python datetime object
start_time = input("Please enter a start time (Hours:Minutes:seconds, example: 9:20:45): ")
start_time = datetime.strptime(start_time, "%H:%M:%S")

# Get end time input and format it into a Python datetime object
end_time = input("Please enter a end time (Hours:Minutes:seconds, example: 13:26:45): ")
end_time = datetime.strptime(end_time, "%H:%M:%S")

# Get the distance in miles and calculate the difference between the start and end time
distance = int(input("Please enter the distance the car has travelled (in miles): "))
difference = end_time - start_time

# Calculate the answer
answer = 3600/difference.seconds * distance  # here is the equation we create above.
answer = round(answer, 2)
```
Seeing this code, you may not have encountered Python's `datetime` library before and so functions like `strptime()` are a bit confusing.
The `datetime` library is an easy way to handle dates and times in our code. 
It means we don't have to handle subtracting "12:34:23" - "11:57:58" on our own, instead Python does it for us!


## Extensions
1. Speed cameras know the timings of each car going past, through number plate recognition. Valid number plates are two letters, two numbers and three letters afterwards,
for example XX77 787. Produce a part of the program that checks whether a number plate matches the given pattern. Tell the user either way
2. Create a program for creating a file of details for vehicles exceeding the speed limit set for a section of road. You will need to create a suitable file with test data, including
randomised number plates and times. You will then use the code you’ve already written to process this list to determine who is breaking the speed limit (70mph) and who
has invalid number plates.

### Extension 1 (solution_advanced.py)
In this part, we add an extra input where the user can enter the number plate of the vehicle. 
The program will then check to ensure the number plate follows the correct pattern.
The correct pattern is: two letter, two numbers, and three letters after.
<br>

For the program below we import the code from `solution.py` so the program runs exactly the same by with additional input for the number plate as shown below.
This code is relatively simple as all we are doing is checking an input for various properties.
```python
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
# NOTE: backslash \ can be used to make a single line multiple lines -- this helps with readability
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
```

### Extension 2 (solution_advanced2.py)
In this extension, we can split into two parts. 
First we must generate a series of tests with randomised data, and second, we must process our own tests to see who is speeding.
<br>
Let's begin with generating the tests. 
For this we use a fairly advanced Python concept called a `generator`.
Essentially our `generate_test_entries` will return a unique entry everytime we loop.
The same result can be make by calling the function every on every loop through.
```python
import datetime
import random

# Constant stores all the letters and numbers for our number plate.
alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")


# This function is a generator, it produces exactly as many generated entries as we want.
# A generator is useful as we can use it in a for loop which we do below.
def generate_test_entries(entry_count):

    # entry_count is the number of entries we want out of the generator
    while entry_count >= 0:
        # We generate a random pattern by randomly choosing 8 characters from the alphabet list above.
        number_plate = "".join(random.choice(alphabet) for _ in range(0, 8))

        # The start time is the current time taken from the user's computer
        start_time = datetime.datetime.now()
        # The end time is the start time plus and random integers between 0 and 120
        end_time = start_time + datetime.timedelta(
            minutes=random.randrange(120),
            seconds=random.randrange(120)
        )
        # Generate random distance between 10 and 300
        distance = random.randint(10, 300)

        # We yield our variables, decrease the entry count, then we continue to loop and yield until entry count is 0
        yield number_plate, start_time.time(), end_time.time(), distance
        entry_count = entry_count - 1


# Here we use the generator function above to generate 100 random entries
# NOTE: you can see some generated entries in test_data!
entries = []
for plate, start, end, distance in generate_test_entries(100):
    entries.append(f"{plate} | {start} | {end} | {distance}\n")

# Finally we write this into the test_data file.
with open("test_data", "w") as f:
    f.writelines(entries)
```
