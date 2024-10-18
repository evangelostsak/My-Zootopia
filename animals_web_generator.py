import data_fetcher


def load_data_html(file_path):
    """Loader for html file"""
    try:
        with open(file_path, "r") as file:
            data = file.read()
            return data
    except FileNotFoundError:
        print(f"File named '{file_path}' was not found")
        return None


def print_animal_info(animals_data, animal_name):
    if animals_data is not None:
        output = ""
        for animal_data in animals_data:
            # append information to each string
            output += '<li class="cards__item">'
            output += f'<div class="card__title">{animal_data['name']}</div><br/>\n'
            output += '<p class="card__text">'
            output += f"<strong>Diet</strong>: {animal_data['characteristics']['diet']}<br/>\n"
            output += f"<strong>Location</strong>: {animal_data['locations'][0]}<br/>\n"
            if 'type' in animal_data['characteristics']:  # getting type only if available
                output += f"<strong>Type</strong>: {animal_data['characteristics'].get('type')}<br/>\n"
            output += '</li>'

        return output
    else:
        # Friendly Error message if animal doesnt exist
        return f"<h2>Oops! Unfortunately the animal '{animal_name}' doesn't exist.</h2>"


def main():
    """Main function"""

    user_input = input("Please enter the name of the animal: ")  # User input for animals name
    animals_info = data_fetcher.fetch_data(user_input)  # Loading animals info from the API
    html_data = load_data_html('animals_template.html')  # #Loading old template from old html file

    new_html_file = html_data.replace('__REPLACE_ANIMALS_INFO__', print_animal_info(animals_info, user_input))
    """Replacing old template with new string containing animal info
    saving it in a variable for further use."""

    with open("animals.html", "w") as file0bj:
        # writing the new html data into a new html file
        file0bj.write(new_html_file)

    print(f"\nWebsite was successfully generated to the file animals.html\n")


if __name__ == '__main__':
    main()
