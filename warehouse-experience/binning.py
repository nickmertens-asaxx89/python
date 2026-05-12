locations = [
    "A-01-01", "A-01-02", "A-01-03",
    "B-01-01", "B-01-02", "B-01-03",
    "C-01-01", "C-01-02", "C-01-03"
]

part_numbers = [
    "PW423-52854",
    "PZ001-82736",
    "84930-44890",
    "UW338-84475"
]


def binning_process():

    # Keep asking until location is correct
    while True:
        location_input = input("Give a location (ex. A-01-01):\n")

        if location_input in locations:
            print("Location OK")
            break
        else:
            print("Wrong location, try again.")

    # Keep asking until part number is correct
    while True:
        pn_input = input("Give a part number (ex. PW423-52854):\n")

        if pn_input in part_numbers:
            print("Part number OK")
            break
        else:
            print("Wrong part number, try again.")

    print("Part is binned in location")


# Run process
binning_process()
