shopping_list = []

def add_to_list(item):    
    shopping_list.append(item)
    # Notify user the item was added and give length of list
    print("Item added: {}".format(new_item))
    print("Total items in list:  {}".format(len(shopping_list)))
    
def show_help():
    print("What groceries to get at the store?")
    print("""
    Enter 'SHOW' to see entire list.
    Enter 'DONE' to exit app.
    Enter 'HELP" for help menu.
    """)
    
def show_list():
    print("Here is your list: ")
    for item in shopping_list:
        print(item)

show_help()
while True:
    new_item = input("Add item to list: ")
    
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue
         
    add_to_list(new_item)

show_list()
        