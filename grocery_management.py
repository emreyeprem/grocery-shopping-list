
shopping_lists = []

class GroceryItem:
    def __init__(self,name):
        self.name = name

    def sorted_list(self):
        for i in range(0, len(item_list)):
            print(shopping_list[i])
            print(item_list[i])

    def __repr__(self):
            return "{0}".format(self.name)



class ShoppingList:
    def __init__(self,title, description):
        self.title = title
        self.description = description
        self.items = []

    def __repr__(self):
            return "{0} : {1}".format(self.title, self.description)

    # def display(self):
    #     display_stores = input('Press d to display stores: ')
    #     if display_stores == 'd':
    #         print(shopping_list)
# #------------------------------------------------------
while True:
    name = input('Enter grocery store name or q to stop: ')
    if(name == 'q'):
        break
    address = input('Enter the address of store: ')
    store = ShoppingList(name, address)
    shopping_lists.append(store)

    print(shopping_lists)

    while True:

        name = input('Enter item name for {0} or q to stop: '.format(store.title))
        quit = input('Press q to quit or enter to add: ')

        grocery_item = GroceryItem(name)
        store.items.append(grocery_item)

        #itemList = Grocery_items(item,[],[] )
        #item_list.append(itemList.names)
        if(quit == 'q'):
            break

    print(shopping_lists)

for shopping_list in shopping_lists:
    print(shopping_list.title)
    for item in shopping_list.items:
        print(item.name)
