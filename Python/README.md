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
THe `datetime` library is an easy way to handle dates and times in our code. 
It means we don't have to handle subtracting "12:34:23" - "11:57:58" on our own, instead Python does it for us!


## Extensions
1. Speed cameras know the timings of each car going past, through number plate recognition. Valid number plates are two letters, two numbers and three letters afterwards,
for example XX77 787. Produce a part of the program that checks whether a number plate matches the given pattern. Tell the user either way
2. Create a program for creating a file of details for vehicles exceeding the speed limit set for a section of road. You will need to create a suitable file with test data, including
randomised number plates and times. You will then use the code you’ve already written to process this list to determine who is breaking the speed limit (70mph) and who
has invalid number plates.

### Extension 1


### Extension 2

