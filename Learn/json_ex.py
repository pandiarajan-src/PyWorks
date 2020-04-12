"""Learn how to get JSON format file and read/write JSON."""
import json

input_file = "C:\\Users\\pandi\\source\\repos\\PyWorks\\test_files\\input.json"
output_file = "C:\\Users\\pandi\\source\\repos\\PyWorks\\test_files\\output.txt"


def dump_person_details_in_json():
    """Dump person details in json."""
    while input("Do you want to add a person? ").lower() == 'yes':
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        country = input("Enter nationality: ")
        zipcode = input("Enter Zipcode: ")
        person = {'Firstname': first_name, 'Lastname': last_name}
        person['Address'] = {'Country': country, 'Zipcode': zipcode}
        person_json = json.dumps(person)
        print(person_json)


def read_json_write_text():
    """How to read the json file and dumps to text file."""
    with open(input_file, 'r') as input:
        input_content = json.load(input)
        with open(output_file, 'w') as output:
            output.write(inpuy_content["name"] + "'s  are \n")
