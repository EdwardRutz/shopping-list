# User, Provide help to user when called for
def show_help():
    print("What groceries to get at the store?")
    print("""
    Enter 'DONE' to exit app.
    Enter 'HELP" for help menu.
    """)

show_help()

# As a user, Contually be prompted to add an item to list if needed
while True:
    new_item = input("> ")
    
    #User, state when done, print out entire list
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
        
        