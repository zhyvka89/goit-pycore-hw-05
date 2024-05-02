from decorators.errors import input_error

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."
  

@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    name = args
    for user_name in contacts:
        if name[0] == user_name:
            return f"{contacts[user_name]}"
        

@input_error
def show_all(contacts):
    if len(contacts):
        str_ = ''
        for name, phone in contacts.items():
            str_ += name + ' ' + phone + '\n'
        return str_ 
    else:
        return "Your contacts list is empty."