class Bag:
    #constructor
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.luggage = []

    def add_luggage(self):
        item = input("please input the item you want to add: ")
        quantity = input("Please input the amount of that item you wish to pack: ")
        self.luggage.append([item, quantity])

    def check_weight(self):
        if int(self.weight) >= 40:
            print("Bag needs to be checked because it exceeds 40 pounds")
        else:
            print("Bag can be carried on")

    def check_luggage(self):
        print(self.luggage)






class User:
    #constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.bags = []

#------------------------------------------------------------------------------------------------

    def pack_bag(self):

        bag_name = input("please give the bag a name: ")
        bag_weight = input("How many pounds is the packed bag: ")
        num_items = int(input("How many items do you wish to pack in this bag: "))

        bag_name = Bag(bag_name, bag_weight)

                
        for i in range(0, num_items):
            bag_name.add_luggage()

        self.bags.append(bag_name)


#--------------------------------------------------------------------------------------------------
    def check_bags(self):

        bag_name = input("Name the bag you would like to look through: ")

        for bag in self.bags:
            if bag.name.lower() == bag_name.lower():
                bag.check_luggage()
            else:
                pass
#---------------------------------------------------------------------------------------------------

    def list_bags(self):
        for bag in self.bags:
            print(bag.name)
    
#----------------------------------------------------------------------------------------------------

    def search_for_bag(self, inspected_bag):
        for bags in self.bags:
            if bags.name.lower() == inspected_bag.lower():
                bags.check_luggage()
            else:
                pass

#-----------------------------------------------------------------------------------------------------

    def remove_bag(self, selected_bag):
        for bags in self.bags:
            if bags.name.lower() == selected_bag.lower():
                position = self.bags.index(bags)
            else:
                pass
               
                
        del self.bags[position]

#---------------------------------------------------------------------------------------------------

    def weigh_bag(self, selected_bag):
        for bags in self.bags:
            if bags.name.lower() == selected_bag.lower():
                bags.check_weight()
            else:
                pass
        
    
    


class Manager:
    #constructor
    def __init__(self):
        self.users = []


    def look_for_user(self, username):
        for user in self.users:
            if user.name.lower() == username.lower():
                return user
        return -1

            
                
            

    def menu(self):

        # Program Variables
        loop = True
        
        # Main Program Loop

        while loop:
            print("\nMAIN MENU")
            print("1: Create a User")
            print("2: Pack a bag")
            print("3: View packed bags")
            print("4: View items in packed bag")
            print("5: Remove a bag from the list")
            print("6: Check weight of a bag")
            print("7: Exit")
            selection = input("please input a selection: ")

            if selection == "1":
               name = input("Please insert the name of the new user: ")
               age = input("Please insert the age of the new user: ")

               name = User(name, age)

               self.users.append(name)


            elif selection == "2":
                
                username = input("please insert the name of the bag owner: ")
                user = self.look_for_user(username)
                if user != -1:
                    user.pack_bag()
                elif user == -1:
                    print("user not found")

                
            elif selection == "3":
                username = input("please insert the name of the bag owner: ")

                user = self.look_for_user(username)
                if user != -1:
                    user.list_bags()
                elif user == -1:
                    print("User does not exist")
                
                    
            elif selection == "4":

                username = input("please insert the name of the bag owner: ")
                inspected_bag = input("please insert the name of the bag you want to look through: ")
                user = self.look_for_user(username)
                if user != -1:
                    user.search_for_bag(inspected_bag)
                elif user == -1:
                    print("Bag not available")
                
                
                
            elif selection == "5":
                username = input("please insert the name of the bag owner: ")
                selected_bag = input("please insert the name of the bag you want to unpack: ")
                user = self.look_for_user(username)
                if user != -1:
                    user.remove_bag(selected_bag)
                elif user == -1:
                    print("no User found")


            elif selection == "6":
                username = input("please insert the name of the bag owner: ")
                selected_bag = input("please insert the name of the bag you wish to weigh: ")
                user = self.look_for_user(username)
                if user != -1:
                    user.weigh_bag(selected_bag)
                elif user == -1:
                    print("User not found")
                

            elif selection == "7":
                loop = False



