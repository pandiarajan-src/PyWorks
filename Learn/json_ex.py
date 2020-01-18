import json

def do_want_to_continue_enter_persion():
    need_to_add_person = input("Do you want to add a person? ")
    if( need_to_add_person.lower() == 'yes'):
        ret_result = True
    else:
        ret_result = False
    return ret_result

    
while do_want_to_continue_enter_persion() == True:
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    country = input("Enter nationality: ")
    zipcode = input("Enter Zipcode: ")
    person = {'Firstname': first_name, 'Lastname': last_name }
    person['Address'] = {'Country':country, 'Zipcode':zipcode}
    person_json = json.dumps(person)
    print(person_json)

