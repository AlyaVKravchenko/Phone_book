def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Invalid command"

    return inner

phone_book = {}

@input_error
def hello():
    return "How can I help you?"

@input_error
def add_contact(name, phone):
    phone_book[name] = phone
    return f"Added {name.title()} with phone {phone}"

@input_error
def change_contact(name, phone):
    if name in phone_book:
        phone_book[name] = phone
        return f"Changed phone for {name.title()} to {phone}"
    else:
        return f"Contact {name.title()} not found"

@input_error
def get_phone(name):
    if name in phone_book:
        return f"The phone for {name.title()} is {phone_book[name]}"
    else:
        return f"Contact {name.title()} not found"
@input_error
def show_all():
    if not phone_book:
        return "Phone book is empty"
    else:
        return "\n".join([f"{name.title()}: {phone}" for name, phone in phone_book.items()])

@input_error
def goodbye():
    return "Good bye!"

def main():
    while True:
        user_input = input("Enter a command: ").lower()
        if user_input == "hello":
            print(hello())
        elif user_input.startswith("add"):
            _, name, phone = user_input.split()
            print(add_contact(name, phone))
        elif user_input.startswith("change"):
            _, name, phone = user_input.split()
            print(change_contact(name, phone))
        elif user_input.startswith("phone"):
            _, name = user_input.split()
            print(get_phone(name))
        elif user_input == "show all":
            print(show_all())
        elif user_input in ["good bye", "close", "exit"]:
            print(goodbye())
            break
        else:
            print("Invalid command")



if __name__ == "__main__":
    bot = main()
    bot.main()