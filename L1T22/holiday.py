#User inputs 
nights = int(input("Nights required for your stay: "))
city = input("Which city (Johanesburg | Cape Town | Durban): ")
days = int(input("Car hire required for how many days: "))

# Function 1 - hotel_cost
def hotel_cost(nights):
    return nights * 1235

# Function 2 - plane_cost
def plane_cost(city):
    if city == "Johannesburg":
        return 4500
    elif city == "Cape Town":
        return 6050
    elif city == "Durban":
        return 3050

# Function 3 - car_rental_cost
# This calc the car_hired by the number of days
def car_rental(days):
    return days * 650

# Function 4 - holiday_cost
def holiday_cost(nights, city, days):
    hotel = hotel_cost(nights)
    print("Hotel stay for", nights, "nights is: R",hotel)
    plane = plane_cost(city)
    print("Flight cost to", city, "is: R",plane)
    car = car_rental(days)
    print("The cost for your car rental for", days, "days is: R",car)
    total = hotel + plane + car
    print("Total: R",total)
holiday_cost(nights, city, days)
