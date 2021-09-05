class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return "{name} menu available from {start} to {end}".format(name = self.name, start = self.start_time, end = self.end_time)

  def calculate_bill(self, purchased_items):
    total = 0
    for item in purchased_items:
      total += self.items[item]
    return total

class Franchise:
  def __init__(self, address, menus):
    self.menus = menus
    self.address = address

  def __repr__(self):
    return self.address

  def available_menus(self, time):
    from datetime import datetime
    available_menus = []
    for menu in self.menus:
      #the rest in the next line
      if(datetime.strptime(time, "%I%p").hour >= datetime.strptime(menu.start_time, "%I%p").hour) and  \
      (datetime.strptime(time, "%I%p").hour < datetime.strptime(menu.end_time, "%I%p").hour):
        available_menus.append(menu.name)
    return available_menus

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises



brunch = Menu(name ="brunch", 
              items = {'pancakes': 7.50, 
                       'waffles': 9.00, 
                       'burger': 11.00, 
                       'home fries': 4.50, 
                       'coffee': 1.50, 
                       'espresso': 3.00, 
                       'tea': 1.00, 
                       'mimosa': 10.50, 
                       'orange juice': 3.50},
              start_time = "11am",
              end_time = "4pm")


early_bird = Menu(name ="early_bird", 
              items = {'salumeria plate': 8.00, 
                       'salad and breadsticks (serves 2, no refills)': 14.00, 
                       'pizza with quattro formaggi': 9.00, 
                       'duck ragu': 17.50, 
                       'mushroom ravioli (vegan)': 13.50, 
                       'coffee': 1.50, 
                       'espresso': 3.00,},
              start_time = "3pm",
              end_time = "6pm")

dinner = Menu(name ="dinner", 
              items = {'crostini with eggplant caponata': 13.00, 
                       'ceaser salad': 16.00, 
                       'pizza with quattro formaggi': 11.00, 
                       'duck ragu': 19.50, 
                       'mushroom ravioli (vegan)': 13.50, 
                       'coffee': 2.00, 
                       'espresso': 3.00,},
              start_time = "5pm",
              end_time = "11pm")


kids = Menu(name ="kids", 
            items = {'chicken nuggets': 6.50, 
                     'fusilli with wild mushrooms': 12.00, 
                     'apple juice': 3.00},
            start_time = "11am",
            end_time = "9pm")

arepas_menu = Menu(name = "Take a’ Arepa",
                   items = {'arepa pabellon': 7.00, 
                            'pernil arepa': 8.50, 
                            'guayanes arepa': 8.00, 
                            'jamon arepa': 7.50},
                    start_time = "10am",
                    end_time = "8pm")

brunch.calculate_bill(["pancakes", "home fries", "coffee"])
early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"])

flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])

new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

flagship_store.available_menus("12pm")
flagship_store.available_menus("5pm")

Basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])
Arepas = Business("Take a' Arepa", arepas_place)