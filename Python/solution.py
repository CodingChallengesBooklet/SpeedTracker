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
answer = 3600/difference.seconds * distance
answer = round(answer, 2)


if __name__ == "__main__":
    print(f"The car was travelling {answer} mph")

