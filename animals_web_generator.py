import json


def load_data(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File named '{file_path}' was not found")
        return None


def print_animal_info(animals_data):

    if animals_data is not None:

        for animal in animals_data:
            name = animal["name"]
            diet = animal["characteristics"]["diet"]
            location = animal["locations"][0]
            type_ = animal["characteristics"].get("type") # Solves the problem with traceback errors.

            if type_:
                # Printing the extracted information
                print(f"Name: {name}")
                print(f"Diet: {diet}")
                print(f"Location Primary: {location}")
                print(f"Type: {type_}\n")
            else:
                print(f"Name: {name}")
                print(f"Diet: {diet}")
                print(f"Location Primary: {location}\n")


animals_info = load_data('animals_data.json')

print_animal_info(animals_info)
