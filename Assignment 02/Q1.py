class Vehicle:
  def __init__(self,id,brnd, rent):
    self.id = id
    self.brand = brnd
    self.rent_per_day = rent

  def display_details(self):
    print(f"Vehicle ID: {self.id}")
    print(f"Brand: {self.brand}")
    print(f"Rent per Day: {self.rent_per_day}")
  
  def calculate_rent(self, n):
    print(f"Rent for {n} days: ", n * self.rent_per_day)

v1 = Vehicle(1, "Honda", 400)
v2 = Vehicle(2, "Mercedes", 1000)


v1.calculate_rent(x)

v1.display_details()
v2.display_details()

x = int(input("Enter the number of days you want to rent car: "))
