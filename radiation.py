import numpy as np

# Initial radiation information for different locations
radiation_info = {
                "City Center": [22, 19, 20, 31, 28], 
                "Industrial Zone": [35, 32, 30, 37, 40], 
                "Residential District": [15, 12, 18, 20, 14], 
                "Rural Outskirts": [9, 13, 16, 14, 7],
                "Downtown": [25, 18, 22, 21, 26]
                }


# Function to calculate the average radiation level
def calc_avg_radiation(radiation):
    return round(sum(radiation) / len(radiation), 2)

# Function to print average radiation levels 
# and standard deviation for each location
def print_avg_radiation(radiation_info):
    for location, radiation in radiation_info.items():
        
        std_dev = np.std(radiation)
        
        print(f"\n{location} has and average radiation level of {calc_avg_radiation(radiation)} and a standard deviation of {round(std_dev, 2)}")


new_rad_readings_list = []


print_avg_radiation(radiation_info)


# Input loop to get a new location with radiation
while True:

    new_location = input("\nPlease enter a new location that has radiation: ").title().strip()

    # Check if the input contains only alphabets
    if new_location.replace(" ", "").isalpha():

        if new_location in radiation_info.keys():
            
            while True:
                choice = input("\nWe already have a reading for the location you entered. Do you want to ovewrite readings? (y/n): ").lower().strip()

                if choice == "y":
                    break
                
                elif choice == "n":
                    break

                else:
                    print("Need to choose between(y/n)")
                    continue

        else:
            break

    else:
        print("Invlaid input! Please only use alphabets.")
        continue

    if choice == "y":
        break


print(f"\nPlease enter 5 radiation readings of {new_location} below.")

# Get 5 radiation readings for the new location
for reading in range(5):
    
    while True:

        try:
            radiation_input = float(input(f"\nPlease enter {reading + 1} of 5 radiation reading: "))
            new_rad_readings_list.append(radiation_input)
            break

        except ValueError:
            print("Invalid input! Please input valid numerical value.")
            continue

# Add the new location and its readings to the dictionary
radiation_info[new_location] = new_rad_readings_list

# Print updated average radiation levels
print_avg_radiation(radiation_info)

# print(radiation_info)
