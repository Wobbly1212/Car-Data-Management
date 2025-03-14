# FUNCTION 1
def create_car_tuple():
    # Get user input
    car_id = input("Enter car_id: ")
    car_model = input("Enter car_model: ")
    car_owner_id = input("Enter car_owner_id: ")

    # Create a tuple
    car_tuple = (car_id, car_model, car_owner_id)

    # Return the tuple
    return car_tuple

# Example usage:
# resulting_car_tuple = create_car_tuple()
# print("Resulting Car Tuple:", resulting_car_tuple)


# FUNCTION 2
def create_owner_tuple():
    # Get user input
    car_owner_id = input("Enter car_owner_id: ")
    car_owner_name = input("Enter car_owner_name: ")
    car_owner_surname = input("Enter car_owner_surname: ")
    car_owner_phone = input("Enter car_owner_phone: ")
    car_owner_country = input("Enter car_owner_country: ")

    # Create a tuple
    owner_tuple = (car_owner_id, car_owner_name, car_owner_surname, car_owner_phone, car_owner_country)

    # Return the tuple
    return owner_tuple

# Example usage:
# resulting_owner_tuple = create_owner_tuple()
# print("Resulting Owner Tuple:", resulting_owner_tuple)


# FUNCTION 3
# Function to create lists of cars and car owners
def create_lists():
    # Create empty lists to store cars and car owners
    cars_list = []
    cars_owner_list = []

    # Ask the user for the number of cars (at least 5)
    num_cars = 0
    while num_cars <= 5:
        num_cars = int(input("Enter the number of cars (at least 5): "))
        if num_cars <= 5:
            print("Number of cars must be at least 5.")

    # Ask the user for the number of car owners (at least 5)
    num_owners = 0
    while num_owners <= 5:
        num_owners = int(input("Enter the number of car owners (at least 5): "))
        if num_owners <= 5:
            print("Number of car owners must be at least 5.")

    # Loop to get input for cars and car owners
    for _ in range(num_cars):
        # Create car tuple and add it to cars_list
        car_tuple = create_car_tuple()
        cars_list.append(car_tuple)

    for _ in range(num_owners):
        # Create owner tuple and add it to cars_owner_list
        owner_tuple = create_owner_tuple()
        cars_owner_list.append(owner_tuple)

    # Return the created lists
    return cars_list, cars_owner_list

# Example usage:
# cars_list, cars_owner_list = create_lists()

# Print the resulting lists
# print("Cars List:", cars_list)
# print("Car Owners List:", cars_owner_list)


# FUNCTION 4
# Function to create dictionaries from lists
def create_dictionaries(cars_list, owners_list):
    # Create Dictionary1 (Car_ID as key, tuple as value)
    dict1 = {}
    for car in cars_list:
        car_id = car[0]
        dict1[car_id] = car

    # Create Dictionary2 (CarOwner_ID as key, tuple as value)
    dict2 = {}
    for owner in owners_list:
        owner_id = owner[0]
        dict2[owner_id] = owner

    # Return the dictionaries
    return dict1, dict2

# Example usage:
# dict1, dict2 = create_dictionaries(cars_list, cars_owner_list)

# Print the resulting dictionaries
# print("Dictionary1 (Car_ID as key):", dict1)
# print("Dictionary2 (CarOwner_ID as key):", dict2)


#  FUNCTION 5
def main_program():
    # Step 1: Define data structures
    cars_list, cars_owner_list = create_lists()

    # Step 2: Call functions to fill in data structures
    dict1, dict2 = create_dictionaries(cars_list, cars_owner_list)

    # Step 3: Print values from both dictionaries
    print("Dictionary1 (Car_ID as key):", dict1)
    print("Dictionary2 (CarOwner_ID as key):", dict2)

    # Step 4: Ask the user to provide a Car_ID
    car_id_to_search = input("Enter Car_ID to search for owner: ")

    # Search for the owner of the specified Car_ID
    if car_id_to_search in dict1:
        car_owner_id = dict1[car_id_to_search][2]  # Index 2 is the car owner ID in the car tuple
        if car_owner_id in dict2:
            # Step 5: Print the full data of the owner
            car_owner_data = dict2[car_owner_id]
            print("Car Owner Data for Car_ID {}: {}".format(car_id_to_search, car_owner_data))
        else:
            print("Car Owner not found for Car_ID {}".format(car_id_to_search))
    else:
        print("Car_ID {} not found.".format(car_id_to_search))

# Step 6: Execute the main program
if __name__ == "__main__":
    main_program()