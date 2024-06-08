from abc import ABC, abstractmethod

class UserInterface(ABC):
    @abstractmethod
    def display_contacts(self, contacts):
        pass

    @abstractmethod
    def display_commands(self):
        pass

class ConsoleUserInterface(UserInterface):
    def display_contacts(self, contacts):
        print("Contacts:")
        for contact in contacts:
            print(contact)

    def display_commands(self):
        print("Available commands:")
        print("1. add - Add a new contact")
        print("2. change - Change phone number of a contact")
        print("3. phone - Get phone number of a contact")
        print("4. all - Show all contacts")
        print("5. add-birthday - Add birthday for a contact")
        print("6. show-birthday - Show birthday of a contact")
        print("7. birthdays - Show upcoming birthdays")
        print("8. exit - Exit the application")

class Application:
    def __init__(self, user_interface):
        self.user_interface = user_interface

    def run(self):
        print("Welcome to the address book application!")
        while True:
            command = input("Enter a command: ")
            if command == "exit":
                print("Goodbye!")
                break
            elif command == "commands":
                self.user_interface.display_commands()
            elif command == "example contacts":
                example_contacts = [
                    "John Doe, 1234567890",
                    "Jane Smith, 0987654321"
                ]
                self.user_interface.display_contacts(example_contacts)
            else:
                print("Invalid command. Type 'commands' to see available commands.")


# Usage:
console_ui = ConsoleUserInterface()
app = Application(console_ui)
app.run()