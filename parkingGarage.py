class ParkingGarage():
    def __init__(self):
        self.yourTicket = ''
        self.tickets = {
            "1": {
                "available": True,
                "paid": False,
                "owed": 0},
            "2": {
                "available": True,
                "paid": False,
                "owed": 0},
            "3": {
                "available": True,
                "paid": False,
                "owed": 0},
            "4": {
                "available": True,
                "paid": False,
                "owed": 0},
            "5": {
                "available": True,
                "paid": False,
                "owed": 0},
            "6": {
                "available": True,
                "paid": False,
                "owed": 0},
            "7": {
                "available": True,
                "paid": False,
                "owed": 0},
            "8": {
                "available": True,
                "paid": False,
                "owed": 0},
            "9": {
                "available": True,
                "paid": False,
                "owed": 0},
            "10": {
                "available": True,
                "paid": False,
                "owed": 0},
            }
        
    def takeTicket(self):
        flag = False
        for key,value in self.tickets.items():
            if value["available"]:
                value["available"] = False
                value["owed"] = 10
                print(f"You have parking space {key}.")
                flag = False
                break
            else:
                flag = True
                continue
        if flag:
            print("Sorry no more spots available!")
            
    def payForParking(self):
        t = self.yourTicket
        if self.tickets[t]["paid"] == True:
            print(f"Car {t} already paid!")
        else:
            while self.tickets[t]["owed"] > 0:
                try:
                    amount = int(input(f"Parking Spot #{t} still owes {self.tickets[t]['owed']}. How much do you want to pay?\n"))
                    self.tickets[t]["owed"] -= amount 
                except:
                    print("must be a number...")         
            if self.tickets[t]["owed"] < 0:
                print("Your change is:", end=" ")        
                print(abs(self.tickets[t]["owed"]))
            print(f"Ticket {t} has been paid. You have 15 minutes to leave, before the building implodes...") 
            self.tickets[t]["paid"] = True
            self.tickets[t]["owed"] = 0
        
    def leaveGarage(self):
        t = self.yourTicket
        if self.tickets[t]["available"] == False:
            if self.tickets[t]["paid"] != True:
                self.payForParking()
                self.leaveGarage()
            else:
                print("Thank you, have a nice day!")
                self.tickets[t]["available"] = True
                self.tickets[t]["paid"] = False
        else:
            print(f'There is no car in space {t}')
    
    def setCar(self):
        car = 0
        while car < 1 or car > 10:
            if car > 10:
                print("Spaces only go up to 10")
            try:
                car = int(input("Which car? \n"))
                self.yourTicket = str(car)  
            except:
                print('Enter a number please...')     
            
    def runner(self):
        park = ""
        print('\n')
        print("Welcome to Lee's junkyard parking emporium.")
        for i in range(14):
            print('-', end='')
            print('-', end="")
            print('*', end="")
            print('-', end='')  
        print('\n')
        while True:
            park = input("Park a car? (y/n)\n")
            if park.lower() == 'y' or park.lower() == 'yes':
                self.takeTicket()
                print("Enjoy the junk...\n")
                selection = ''     
                while True:
                    selection = input("When ready, please (pay) for parking and/or (leave) or (park) another car...\n(q) to quit\n")
                    if selection.lower() == 'q' or selection.lower() =="quit":
                        break
                    if selection.lower() == "pay":
                        self.setCar()
                        self.payForParking()
                        selection = ""
                    elif selection.lower() == "leave":
                        self.setCar()
                        self.leaveGarage()
                        flag = False
                        cars = []
                        for k,v in self.tickets.items():                  
                            if v["available"] == False:
                                flag = True
                                cars.append(k)
                        if flag == False:
                            print("All spaces are now availble!")
                            park = ""                  
                        else:
                            if len(cars) > 1:
                                print("The following cars still need drivers:")
                                for car in cars:
                                    print('-' + car + '- ')
                            else:
                                print(f"Car {cars[0]} still needs a driver!")                                                
                    elif selection.lower() == "park":
                        self.takeTicket()
                        selection = ''
                        continue
            elif park.lower() == 'n' or park.lower() == "no":
                print('Bye bye!!!')
                break
                
            

ParkingGarage().runner()
            
        
    
    
    
    
    
    
    
    
#     Your parking garage class should have the following methods:
# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1

# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True

# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)



# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary

# each person in the group should list the portion of the project they were responsible for inside of the python file and inside the README file.

# By the end of this project each group/student should be able to:
# - Explain and/or demonstrate using Git and Github for collaboration
# - Explain and/or demonstrate creating classes
# - Explain and/or demonstrate creating class methods
# - Explain and/or demonstrate class instantiation