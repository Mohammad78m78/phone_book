class Address:
    def __init__(self ,country , state , city , alley , no) -> None:
        self.country = country
        self.state = state
        self.city = city
        self.alley = alley
        self.no = no

    def __str__(self) -> str:
        return f" {self.no}  {self.alley}  {self.city}  {self.state}  {self.country}"


class Contact:
    def __init__(self, email , phone_number='') -> None:
        self.phone_number = phone_number
        self.email = email

    @property
    def phone_number(self):
        return self.__phone_number
    @phone_number.setter
    def phone_number(self , value):
        if len(value) == 11:
            self.__phone_number = value
        else:
            self.__phone_number =""

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self,value):
        import re
        regex = "^[a-zA-Z0-9-_.]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
        if (re.match(regex, value)):
            self.__email = value
        else:
            self.__email =""

    def __str__(self) -> str:
        return f"Phone number : {self.__phone_number}\nEmail : {self.email}"

class PhoneBook():
    my= []
    contact_list = []
    def __init__(self , first_name , last_name , contact,address ,relationships) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.contact = Contact(email , phone_number)
        self.address = Address(country, state , city , alley , no)
        self.relationships = relationships

    def show_contact(li):
        for i in li:
            print(i) 

    def edit(self , name , family):
        import os
        for i in self.contact_list:
            if name == i.first_name and family == i.last_name:
                edit_menu()
                
                while (e_option :=input("Choose an option .")) != "0":
                    if e_option == "1":
                        os.system("cls")
                        new_name = input("Enter the new first name :")
                        if new_name !="":
                            i.first_name = new_name
                        else:
                            i.first_name = i.first_name
                        os.system("cls")
                        edit_menu()
                    elif e_option == "2":
                        os.system("cls")
                        new_family = input("Enter the new last name :")
                        if new_family !="":
                            i.last_name = new_family
                        else:
                            i.last_name = i.last_name
                        os.system("cls")
                        edit_menu()
                    elif e_option == "3":
                        os.system("cls")
                        new_phone = input("Enter the new phone number :")
                        if new_phone !="":
                            i.contact.phone_number = new_phone
                        else:
                            i.contact.phone_number = i.contact.phone_number
                        os.system("cls")
                        edit_menu()
                    elif e_option == "4":
                        os.system("cls")
                        new_email = input("Enter the new email :")
                        if new_email !="":
                            i.contact.email = new_email
                        else:
                            i.contact.email = i.contact.email
                        os.system("cls")
                        edit_menu()
                    elif e_option == "5":
                        os.system("cls")
                        new_no = input("Enter the new no :")
                        if new_no !="":
                            i.address.no= new_no
                        else:
                            i.address.no = i.address.no
                        os.system("cls")
                        edit_menu()
                    elif e_option == "6":
                        os.system("cls")
                        new_alley = input("Enter the new alley :")
                        if new_alley !="":
                            i.address.alley = new_alley
                        else:
                            i.address.alley = i.address.alley
                        os.system("cls")
                        edit_menu()
                    elif e_option == "7":
                        os.system("cls")
                        new_city = input("Enter the new city :")
                        if new_city !="":
                            i.address.city = new_city
                        else:
                            i.address.city = i.address.city
                        os.system("cls")
                        edit_menu()
                    elif e_option == "8":
                        os.system("cls")
                        new_state = input("Enter the new stats :")
                        if new_state !="":
                            i.address.state = new_state
                        else:
                            i.address.state = i.address.state
                        os.system("cls")
                        edit_menu()
                    elif e_option == "9":
                        os.system("cls")
                        new_country = input("Enter the new country :")
                        if new_country !="":
                            i.address.country = new_country
                        else:
                            i.address.country = i.address.country
                        os.system("cls")
                        edit_menu()
                    elif e_option == "10":
                        os.system("cls")
                        new_relationships = input("Enter the new relationships :")
                        if new_relationships !="":
                            i.relationships = new_relationships
                        else:
                            i.relationships = i.relationships
                        os.system("cls")
                        edit_menu()
            else:
                print("Contact not found") 

    def remove(self , name , family):
        for i in self.contact_list:
            if name == i.first_name and family == i.last_name :
                self.contact_list.remove(i)
        
    def __str__(self) -> str:
        return f"First name : {self.first_name}\nLast name : {self.last_name}\n{self.contact}\nAddress : {self.address}\nRelationships : {self.relationships}"
def edit_menu():
        print(" ------------------------")
        print("| 1) First name         |")
        print("| 2) Last name          |")
        print("| 3) Phone number       |")
        print("| 4) Email              |")
        print("| 5) No                 |")
        print("| 6) Alley              |")
        print("| 7) City               |")
        print("| 8) State              |")
        print("| 9) Country            |")
        print("| 10) Relationships     |")
        print("| 0) EXIT               |")
        print(" ------------------------")

def show_menu():
    print(" ------------------------")
    print("| 1) Add new contact    |")
    print("| 2) Show               |")
    print("| 3) Edit contact       |")
    print("| 4) Delete contact     |")
    print("| 5) Show date now      |")
    print("| 6) EXIT               |")
    print(" ------------------------")


if __name__=="__main__":
    import os
    show_menu()
    while (current :=input()) != "6":
        if current == "1":
            os.system("cls")

            print("Leave the options you do'nt want to fill in blank . ")

            first_name = input("Please enter first name :")
            last_name = input("Please enter last name :")

            print("The phone number must be 11 digits long .")
            phone_number = input("Please enter phone number :")

            q1 = input("Do you want to enter an email ? 1.Yes 2.No\n")
            if q1 == "1":
                print("The correct form of email is : example@email.com ")
                email = input("Please enter email :")
            else:
                email =""

            q2 = input("Do you want to enter an address ? 1.Yes 2.No \n")
            if q2 == "1":
                country = input("country :")
                state = input("state :")
                city = input("city :")
                alley = input("alley :")
                no = input("no :")
            else:
                country = ""
                state = ""
                city = ""
                alley = ""
                no = ""
            q3 = input("Do you want to choose a relationship ? 1.Yes 2.No\n")
            if q3 == "1":
                print("1.Grandpa")
                print("2.Grand mother")
                print("3.Father")
                print("4.Mother")
                print("5.Brother")
                print("6.Sister")
                print("7.Spouse")
                print("8.Child")
                print("9.Friend")
                relation = input("Please enter the desires option number :")
                if relation == "1":
                    relationships = "Grandpa"
                elif relation == "2":
                    relationships = "Grand mother"
                elif relation == "3":
                    relationships = "Father"
                elif relation == "4":
                    relationships = "Mother"
                elif relation == "5":
                    relationships = "Brother"
                elif relation == "6":
                    relationships = "Sister"
                elif relation == "7":
                    relationships = "Spouse"
                elif relation == "8":
                    relationships = "Child"
                else: 
                    relationships = "Friend"
            else:
                relationships = ""

            
            person = Contact(email , phone_number)
            c_address = Address(country, state , city , alley , no)
            audience_create = PhoneBook(first_name , last_name , person ,c_address ,relationships)
            PhoneBook.contact_list.append((audience_create))
            PhoneBook.my.append(PhoneBook.contact_list)
            os.system("cls")
            show_menu()

        elif current == "2":
            if PhoneBook.contact_list:
                PhoneBook.show_contact(PhoneBook.contact_list)
                home = input("Want to return to the home page ? 1.Return\n")
                if home == "1":
                    os.system("cls")
                    show_menu()
            else:
                os.system("cls")
                print("There is no audience")
                
                show_menu()

        elif current == "3":
            os.system("cls")
            fname = input("Please enter first name :")
            lname = input("Please enter last name :")
            for i in PhoneBook.contact_list:
                PhoneBook.edit(audience_create , fname , lname)
            os.system("cls")
            show_menu()
        elif current == "4":
            os.system("cls")
            f_name = input("Please enter the first name of the contact :")
            l_name = input("Please enter the last name of the contact :")

            for i in PhoneBook.contact_list:
                PhoneBook.remove(audience_create , f_name , l_name)
            os.system("cls")
            show_menu()

        elif current == "5":
            os.system("cls")
            import datetime as dt
            print(dt.datetime.now())
            show_menu()