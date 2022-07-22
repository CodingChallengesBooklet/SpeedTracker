# Speed Tracker
In this code challenge we write a program to calculate the speed of a car.

![GitHub followers](https://img.shields.io/github/followers/hrszpuk?style=social)
![Twitter Follow](https://img.shields.io/twitter/follow/hrszpuk?style=social)
<br>
![GitHub language count](https://img.shields.io/github/languages/count/CodingChallengesBooklet/SpeedTracker?style=for-the-badge)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/CodingChallengesBooklet/SpeedTracker?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/CodingChallengesBooklet/SpeedTracker?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/CodingChallengesBooklet/SpeedTracker?style=for-the-badge)
![GitHub branch checks state](https://img.shields.io/github/checks-status/CodingChallengesBooklet/SpeedTracker/main?style=for-the-badge)

## Problem
Create a program that takes a time for a car going past a speed camera, the time going past the next one and the distance between them to calculate the average speed for
the car in mph. The cameras are one mile apart.

## Solution
This problem is relatively simple. We must record the time when the car passes the first speed camera, then records the time when the car passes the second speed camera.
We can use the difference between the first speed camera time and the second speed camera time, as well as the distance between the speed cameras (stated in the problem to be one mile), 
to find the speed (in miles per hour) at which the car is going.

To simplify our process, assume the speed cameras record the time in seconds this makes getting the time difference, and getting the miles per hour easier.
Below is the equation used to calculate the miles per hour the car is moving.
```
car_speed = 3600/time_difference * miles_apart
```
Where is 3600 coming from? 3600 is the number of seconds in an hour. 
We need this to calculate the number of miles the car can travel in 60 minutes. 
In an example, say the time difference is 60. We divide 3600 by 60 to get the number of miles
the car could travel in an hour (since we are using miles per hour). This means, in our example,
the car is travelling at 60 miles per hour because 3600/60 = 60.

As the problem states, the speed cameras are one mile apart. 
This means in the equation above we will always replace `miles_apart` with 1 (
which can be negated out of the calculation anyway as it would have no effect). 
The solution to this problem is simply to use the equation in whatever programming language you are using.

```java
first_speed_camera_time = INPUT "Enter the time of the first speed camera (in seconds)"
second_speed_camera_time = INPUT "Enter the time of the second speed camera (in seconds"

time_difference = second_speed_camera_time - first_speed_camera_time
car_speed = 3600/time_difference

OUTPUT "The car was travelling at " + car_speed + " mph!"
```

## Extensions
1. Speed cameras know the timings of each car going past, through number plate recognition. Valid number plates are two letters, two numbers and three letters afterwards,
   for example XX77 787. Produce a part of the program that checks whether a number plate matches the given pattern. Tell the user either way.
    
    *NOTE: there is an error in the extension task here, the description does not match the example provided. Please ignore the example provided by OCR.*

2. Create a program for creating a file of details for vehicles exceeding the speed limit set for a section of road. You will need to create a suitable file with test data, including
   randomised number plates and times. You will then use the code you’ve already written to process this list to determine who is breaking the speed limit (70mph) and who
   has invalid number plates.

### Extension 1 Solution
Ignoring the error of the example, we will use the rules specified as in the extension,
"Valid number plates are two letters, two numbers and three letters afterwards", 
This means examples of valid number plates would be: HV90 ROK, KO88 VBG, GM45 OLD.

The solution to this is really easy, we simply take user input of the number plate, 
and then check each part of the number plate to ensure it is correct.

1. Input number plate.
2. Sanitise input, sometimes we put spaces in the middle of number plates, we remove this space to make reading the data easier and more consistent.
3. Check the length of the number plate (must have a length of 7!).
4. Check each position is correct (either letter or number).
5. Output valid or invalid

```javascript
number_plate = INPUT "Enter number plate"
REMOVE SPACE IN number_plate

valid = true 

IF number_plate LENGTH IS NOT 7 THEN valid = false

IF number_plate[0] IS NOT LETTER THEN valid = false
IF number_plate[1] IS NOT LETTER THEN valid = false
IF number_plate[2] IS NOT NUMBER THEN valid = false
IF number_plate[3] IS NOT NUMBER THEN valid = false

IF number_plate[4] IS NOT LETTER THEN valid = false
IF number_plate[5] IS NOT LETTER THEN valid = false
IF number_plate[6] IS NOT LETTER THEN valid = false

IF valid = true THEN OUTPUT "Number plate is valid!"
ELSE OUTPUT "Number plate is invalid!"
```

### Extension 2 Solution
Here our task is to generate a file containing vehicle details such as number plate and timings.
We will then read our own generated test and determine if the driver is breaking the speed limit of 70mph!

This extension is more complicated, but it can be broken down into steps...
1. Generate random number plates, speed camera 1 times, and speed camera 2 times.
2. Write 100s to 1000s of our randomly generated details from step 1 into a file
3. Read file and split into necessary information: number plate, time 1, time 2.
4. Check if plate is valid, if not add number plate to list of invalid plates.
5. Check if car is speeding, if so add number plate to list of speeders.
6. Output a list of all the number plates with who is speeding and who has an invalid number plate.

For a real code example of this, I recommend checking out the Python version of this extension.

