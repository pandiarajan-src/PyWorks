"""Learn how to get JSON format file and read/write JSON."""
import json

class Who:
    """Jsust JSON property class"""
    def __init__(self, name, age):
        """Just JSON property class"""
        self.name = name
        self.age = age

    def __str__(self):
        return "name: " + self.name + " age: " + str(self.age)

    def __dict__(self):
        return {self.name: self.age}

# TODO: This Encoder and Decoder gives an error, need to fix this.
#class MyEncoder(json.JSONEncoder):
#    """JSON encoder to dump Py object to JSON"""
#    def default(self, w):
#        """Encoder overridden method"""
#        if isinstance(w, Who):
#            return w.__dict__
#        else:
#            return super().default(self, w)


#class MyDecoder(json.JSONDecoder):
#    """JSON decoder to dump JSON object to PY object"""
#    def __init__(self):
#        """Initialize Decoder constr"""
#        json.JSONDecoder.__init__(self, object_hook=self.decode_who)

#    def decode_who(self, d):
#        """Actual decode happens here"""
#        return Who(**d)

def encode_who(w_obj):
    """JSON encode of the given object, it is Who"""
    if isinstance(w_obj, Who):
        return w_obj.__dict__
    raise TypeError(w_obj.__class__.__name__ + 'is not JSON serializable')


def decode_who(w_json):
    """JSON decode of the given object, it is Who"""
    return Who(w_json['name'], w_json['age'])

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

def read_json_write_text(input_file_path, output_file_path):
    """How to read the json file and dumps to text file."""
    with open(input_file_path, 'r') as input_file:
        input_content = json.load(input_file)
        with open(output_file_path, 'w') as output_file:
            output_file.write(input_content["name"] + "'s  are \n")

if __name__ == "__main__":
    INPUT_FILE_PATH = "C:\\Users\\pandi\\source\\repos\\PyWorks\\test_files\\input.json"
    OUTPUT_FILE_PATH = "C:\\Users\\pandi\\source\\repos\\PyWorks\\test_files\\output.txt"
    dump_person_details_in_json()

    ##How to dump class variables into JSON
    #some_man = Who('Jane Doe', 23)
    #json_str = json.dumps(some_man, cls=MyEncoder)
    #new_man = json.loads(json_str, cls=MyDecoder)
    #print(type(new_man))
    #print(new_man.__dict__)

    #method based implementation
    OLD_MAN = Who("Jane Doe", 23)
    JSON_STR = json.dumps(OLD_MAN, default=encode_who)
    NEW_MAN = json.loads(JSON_STR, object_hook=decode_who)
    print(type(NEW_MAN))
    print(NEW_MAN.__dict__)
