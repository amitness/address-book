import pickle
import os

UI = '''
1. Add new contact
2. View contacts
3. Search contact
4. Update contact
5. Delete contact
6. Reset all
7. Exit
'''


class Person:

    def __init__(self, name=None, address=None, phone=None):
        self.name = name
        self.address = address
        self.phone = phone

    def __str__(self):
        return "{} {:>15} {:>15}".format(self.name, self.address, self.phone)


class Application:

    def __init__(self, database):
        self.database = database
        self.persons = {}
        if not os.path.exists(self.database):
            f = open(self.database, 'w')
            pickle.dump({}, f)
            f.close()
        else:
            with open(self.database, 'r') as db:
                self.persons = pickle.load(db)

    def add(self):
        name, address, phone = self.getdetails()
        if name not in self.persons:
            self.persons[name] = Person(name, address, phone)
        else:
            print "Contact already present."

    def viewall(self):
        if self.persons:
            print "{} {:>15} {:>15}".format('Name', 'address', 'Phone')
            for person in self.persons.values():
                print person
        else:
            print "No contacts in database."

    def search(self):
        name = raw_input("Enter the name: ")
        if name in self.persons:
            print self.persons[name]
        else:
            print "Contact not found."

    def getdetails(self):
        name = raw_input("Name: ")
        address = raw_input("Address: ")
        phone = raw_input("Phone:")
        return name, address, phone

    def update(self):
        name = raw_input("Enter the name: ")
        if name in self.persons:
            print "Found. Enter new details."
            name, address, phone = self.getdetails()
            self.persons[name].__init__(name, address, phone)
            print "Successfully updated."
        else:
            print "Contact not found."

    def delete(self):
        name = raw_input("Enter the name to delete: ")
        if name in self.persons:
            del self.persons[name]
            print "Deleted the contact."
        else:
            print "Contact not found in the app."

    def reset(self):
        self.persons = {}

    def __del__(self):
        with open(self.database, 'w') as db:
            pickle.dump(self.persons, db)

    def __str__(self):
        return UI


def main():
    app = Application('contacts.data')
    choice = ''
    while choice != '7':
        print app
        choice = raw_input('Choose: ')
        if choice == '1':
            app.add()
        elif choice == '2':
            app.viewall()
        elif choice == '3':
            app.search()
        elif choice == '4':
            app.update()
        elif choice == '5':
            app.delete()
        elif choice == '6':
            app.reset()

if __name__ == '__main__':
    main()
