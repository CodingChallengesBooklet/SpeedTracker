import datetime
import random

alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")


def generate_test_entries(entry_count):
    while entry_count >= 0:
        number_plate = random.choice(alphabet) + \
                       random.choice(alphabet) + \
                       random.choice(alphabet) + \
                       random.choice(alphabet) + \
                       random.choice(alphabet) + \
                       random.choice(alphabet) + \
                       random.choice(alphabet)

        start_time = datetime.datetime.now()
        end_time = start_time + datetime.timedelta(
            minutes=random.randrange(120),
            seconds=random.randrange(120)
        )
        distance = random.randint(10, 300)
        yield number_plate, start_time.time(), end_time.time(), distance
        entry_count = entry_count - 1


entries = [f"{plate} | {start} | {end} | {distance}\n" for plate, start, end, distance in generate_test_entries(100)]
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
