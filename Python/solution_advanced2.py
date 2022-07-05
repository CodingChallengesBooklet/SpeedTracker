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


def read_entry(entry_string):
    entry = entry_string.split(" | ")
    start_time = datetime.datetime.strptime(entry[1], "%H:%M:%S.%f")
    end_time = datetime.datetime.strptime(entry[2], "%H:%M:%S.%f")
    distance = int(entry[3])
    return entry[0], start_time, end_time, distance


with open("test_data", "r") as f:
    count = 1
    for line in f.readlines():
        number_plate, start, end, distance = read_entry(line)
        difference = end - start
        speed = round(3600 / difference.seconds * distance, 2)
        valid = number_plate[0].isalpha() and \
                number_plate[1].isalpha() and \
                number_plate[2].isdigit() and \
                number_plate[3].isdigit() and \
                number_plate[4].isalpha() and \
                number_plate[5].isalpha() and \
                number_plate[6].isalpha()

        print(f"[{count}] Plate={number_plate} (valid?: {valid}), speed={speed} mph (speeding?: {speed>70})")
        count += 1
