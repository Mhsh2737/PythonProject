from farayand.parking import *

while True:
    option = show_menu()
    match option:
        case "1":
            get_information()

        case "2":
            find_by_plate()

        case "3":
            show_result()

        case "0":
            break

        case _:
            print("Sorry, I didn't understand that.")
            print("-" * 20)






