'''Learn CSV by implementing PhoneContact class'''

import csv
from pathlib import Path

class PhoneContact:
    """This class is just property class, no operations"""
    def __init__(self, firstname, lastname, mobileno, emailid):
        """init all properties"""
        self.first_name = firstname
        self.last_name = lastname
        self.mobile_no = mobileno
        self.email_id = emailid

    def __str__(self):
        return self.first_name + ":" + self.last_name + ":" + self.mobile_no + ":" + self.email_id

    def __dict__(self):
        return {self.mobile_no:(self.first_name, self.last_name, self.email_id)}

class Phone:
    """Phone class that implements contacts app"""
    def __init__(self, contacts_file_name):
        """Initialize phone class with its contacts"""
        self.contacts_file_name = contacts_file_name
        self.contacts_list = []
        self.load_contacts_from_csv()

    def load_contacts_from_csv(self):
        """Load contacts details into contacts_list"""
        with open(self.contacts_file_name, newline='') as contacts_file:
            field_names = ['FirstName', 'LastName', 'MobileNo', 'EmailId']
            #we can use either csv.reader or csv.dictreader
            reader = csv.DictReader(contacts_file, fieldnames=field_names)
            for row in reader:
                ph_con = PhoneContact(row['FirstName'], row['LastName'], \
                                      row['MobileNo'], row['EmailId'])
                self.contacts_list.append(ph_con)

    def write_new_contact_to_csv(self):
        """Add a new contact to the csv file in a phonebook app"""
        f_name = input("Enter first name: ")
        l_name = input("Enter last name: ")
        m_no = input("Enter mobile no: ")
        e_id = input("Enter email id:")
        with open(self.contacts_file_name, 'w', newline='') as contacts_write_file:
            contacts_writer = csv.writer(contacts_write_file, \
                                         delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            contacts_writer.writerow([f_name, l_name, m_no, e_id])
        #Once the contents were written, in-memory contact list to be updated
        self.load_contacts_from_csv()

    def print_all_contacts_from_contact_list(self):
        """Print all the contact list item into stdout"""
        for search_item in self.contacts_list:
            print("FirstName: {0} \t LastName:{1} \t MobileNo: {2} \t EmailId: {3}\t". \
                format(search_item.first_name, search_item.last_name, \
                       search_item.mobile_no, search_item.email_id))

    def search_contacts(self, search_string):
        """Search any input that matches the contact details"""
        found_list = []
        for list_item in self.contacts_list:
            if list_item.first_name.find(search_string) >= 0 or \
                list_item.last_name.find(search_string) >= 0 or \
                list_item.mobile_no.find(search_string) >= 0 or \
                list_item.email_id.find(search_string) >= 0:
                found_list.append(list_item)
        return found_list

if __name__ == "__main__":
    try:
        INPUT_FILE = input("Enter CSV File path: ")
        FILE_PATH = Path(INPUT_FILE)
        if FILE_PATH.exists() and FILE_PATH.is_file():
            PH_OBJ = Phone(INPUT_FILE)
            PH_OBJ.print_all_contacts_from_contact_list()
            PH_OBJ.write_new_contact_to_csv()
            PH_OBJ.print_all_contacts_from_contact_list()
            SEARCH_STR = input("Enter search string to search phone contact: ")
            SEARCH_LIST = PH_OBJ.search_contacts(SEARCH_STR)
            for item in SEARCH_LIST:
                print("FirstName: {0} \t LastName:{1} \t MobileNo: {2} \t EmailId: {3}\t". \
                    format(item.first_name, item.last_name, item.mobile_no, item.email_id))
    except Exception as ex:#pylint: disable=broad-except
        print("Unknown Exception occured: {0}".format(str(ex)))
