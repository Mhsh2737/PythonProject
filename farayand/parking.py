from re import match
cars_list = []

def show_menu():
    print("1) Add car")
    print("2) Find by plate")
    print("3) Show car list")
    print("0) exit")
    print("-" * 20)
    option = input("Enter your option: ")
    print("-" * 37)
    return option

def name_validator(name):
    if match(r"^[A-Za-z0-9\s]{3,30}$",name):
        return True
    else:
        return False

def model_validator(model):
    if match(r"^[A-Za-z0-9]{3,30}$",model):
        return True
    else:
        return False

def plate_validator(plate):
    if match(r"^\d{2} .{1} \d{3} _ .{4} \d{2}$",plate):
        return True
    else:
        return False

def colo_validator(color):
    if match(r"^(white|red|blue|black)$",color):
        return True
    else:
        return False

def get_information():
    name = input("Enter your name: ")
    model = input("Enter your model: ")
    plate = input("Enter your plate: ")
    color = input("Enter your color: ")
    if name_validator(name) and model_validator(model) and plate_validator(plate) and colo_validator(color):

        product = {
            "name": name,
            "model": model,
            "plate": plate,
            "color": color
        }

        cars_list.append(product)

def find_by_plate():
    plate = input("Enter Plate number: ")
    for product in cars_list:
        if product["plate"] == plate:
            print(product)
        else:
            print("Error: plate not found!!!")

def show_car_list():
    for product in cars_list:
        print(cars_list)

def show_result():
    for product in cars_list:
        print(f"Name car: {product["name"]:<20} Model: {product["model"]:<8}  Plate:  {product["plate"]:<25} Color: {product["color"]:<5}")
        print("-" * 37)



