
def get_selection(options):
    for i, s in enumerate(options):
        print(f"{i}. {s}")
    selection = input("Select an option by number: ")
    return options[int(selection)]
