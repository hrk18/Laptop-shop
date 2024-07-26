from read import read_laptop_stock
from datetime import datetime


def buy_Laptop():
    # Input validation for name
    while True:
        try:
            company_name = input("Enter company name: ")
            if not company_name.isalpha():
                raise ValueError("Please enter a valid name !!")
            break
        except ValueError as e:
            print(e)
            print("\n")

    # Input validation for phone number
    while True:
        try:
            company_contact = input("Enter your phone: ")
            if not company_contact.isdigit() or len(company_contact) != 10:
                raise ValueError("Please enter a valid phone number !!")
            break
        except ValueError as e:
            print(e)
            print("\n")
    print("-------------------------------------------------------------------------------------------------------------")
    print("S.N. \t Name \t\t     Brand \t    Price \t Quantity \t Processor \t Graphic Card")
    print("-------------------------------------------------------------------------------------------------------------")
    a = 1
    file = open("Laptop_stock.txt", "r")
    for line in file:
        print(a, "\t" + line.replace(",", "\t"))
        a = a + 1
    print("-------------------------------------------------------------------------------------------------------------")
    file.close()
    print("\n")

    laptop_bought = []
    while True:
        valid_id = int(
            input(" To place an order,please provide the ID number of the laptop you'd like to purchase:"))
        print("\n")

        # validating user input for the laptop ID and quantity
        while valid_id <= 0 or valid_id > len(read_laptop_stock()):
            print("Invalid Laptop ID. Try again!!")
            print("\n")
            valid_id = int(
                input("To place an order, please provide the ID number of the laptop you'd like to purchase: "))

        laptop_quantity = None
        while laptop_quantity is None:
            quantity_input = input(
                "Please specify the quantity of laptops you wish to purchase: ")
            if not quantity_input.isnumeric():
                print("Invalid input. Please enter a valid integer value.")
            elif int(quantity_input) <= 0:
                print("Invalid input. Quantity must be greater than 0.")
            else:
                laptop_quantity = int(quantity_input)

        mylaptop_dict = read_laptop_stock()
        # valid_id = input("Please enter the ID of the laptop you wish to purchase: ")

        getlaptop_quantity = mylaptop_dict.get(
            valid_id, [None, None, None, 0])[3]
        while laptop_quantity > int(getlaptop_quantity) or laptop_quantity <= 0:
            print("We're sorry, but the requested quantity of laptops is currently unavailable. Please select a different quantity or choose from our other available laptops.")
            laptop_quantity = None
            while laptop_quantity is None:
                quantity_input = input(
                    "Please specify the quantity of laptops you wish to purchase: ")
                if not quantity_input.isnumeric():
                    print("Invalid input. Please enter a valid integer value.")
                elif int(quantity_input) <= 0:
                    print("Invalid input. Quantity must be greater than 0.")
                else:
                    laptop_quantity = int(quantity_input)
            getlaptop_quantity = mylaptop_dict.get(
                valid_id, [None, None, None, 0])[3]

        print("\n")

        # Updating quantity of laptop in the text file
        mylaptop_dict[valid_id][3] = int(
            mylaptop_dict[valid_id][3]) + int(laptop_quantity)
        file = open("Laptop_stock.txt", "w")
        for values in mylaptop_dict.values():
            file.write(str(values[0])+"," + str(values[1])+"," + str(values[2]) +
                       "," + str(values[3])+"," + str(values[4])+"," + str(values[5]))
            file.write("\n")
        file.close()

        # Purchasing from manufacturer
        laptop_name = mylaptop_dict[valid_id][0]
        laptop_brand = mylaptop_dict[valid_id][1]
        quantity_of_laptop = laptop_quantity
        unit_price = mylaptop_dict[valid_id][2]
        total_price_of_laptop = mylaptop_dict[valid_id][2].replace("$", '')
        final_price = int(total_price_of_laptop)*int(quantity_of_laptop)
        laptop_bought.append(
            [laptop_name, laptop_brand, quantity_of_laptop, total_price_of_laptop, final_price,])

        buy_more = input("Are you interested in buying more laptops? (Y/N): ")
        if buy_more.isalpha() and buy_more.lower() == 'n':
            break
        elif buy_more.isalpha() and buy_more.lower() == 'y':
            continue
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
            buy_more = input(
                "Are you interested in buying any more laptops? (Y/N): ")
        if buy_more.lower() == 'n':
            break
        elif buy_more.lower() == 'y':
            continue
        else:
            print("Invalid input. Exiting loop.")
            buy_more = input(
                "Are you interested in buying any more laptops? (Y/N): ")
        if buy_more.lower() == 'n':
            break
        elif buy_more.lower() == 'y':
            continue
        else:
            print("Sorry, the input you provided is invalid.Try again")
            break

    total = 0
    for i in laptop_bought:
        total += int(i[4])
        VAT = 0.13*(total)
    final_total = total + VAT
    date_time = datetime.now()
    print("\n")
    print("\t \t \t \t WelCome TO Hrk Laptop Shop")
    print("\t \t\t Balkumari, Kathmandu | Contact No: 9814848773 ")
    print("\n")
    print("----------------------------------------------------------------------------------------")
    print("Laptop Buying Details: ")
    print("----------------------------------------------------------------------------------------")
    print("Customer Name:" + str(company_name))
    print("Phone Number: " + str(company_contact))
    print("Date and Time: " + str(date_time))
    print("----------------------------------------------------------------------------------------")
    print("\n")
    print("Buying Details are:")
    print("------------------------------------------------------------------------------------------------------------------")
    print("Laptop Name \t\t\tBrand \t\t Total Quantity \t\t  Unit Price \t\t Total ")
    print("------------------------------------------------------------------------------------------------------------------")
    for i in laptop_bought:
        print(i[0], "\t\t", i[1],
              "\t\t", i[2], "\t\t\t", i[3], "\t\t", "$", i[4])
    print("------------------------------------------------------------------------------------------------------------------")

    print("Vat Amount:",  VAT)
    print("Final Total Amount:" + str(final_total))
    print("Note: Vat Amount added to final total amount")

    return company_name, company_contact, date_time, laptop_bought, VAT, final_total


def sall_Laptop():

    print("To receive the bill, please enter your name and phone number:")
    print("---------------------------------------------------------------------")
    print("\n")
    # Input validation for full name
    while True:
        try:
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            if not (first_name.isalpha() and last_name.isalpha()):
                raise ValueError("Please provide a valid name !!")
            full_name = first_name + " " + last_name
            break
        except ValueError as e:
            print(e)
            print("\n")

    # Input validation for phone number
    while True:
        try:
            phone = input("Enter your phone: ")
            if not phone.isdigit() or len(phone) != 10:
                raise ValueError("Please provide a valid phone number !!")
            break
        except ValueError as e:
            print(e)
            print("\n")
    print("-------------------------------------------------------------------------------------------------------------")
    print("S.N. \t Name \t\t      Brand \t   Price \t Quantity \t Processor \t Graphic Card")
    print("-------------------------------------------------------------------------------------------------------------")
    a = 1
    file = open("Laptop_stock.txt", "r")
    for line in file:
        print(a, "\t" + line.replace(",", "\t"))
        a = a + 1
    print("-------------------------------------------------------------------------------------------------------------")
    file.close()
    print("\n")

    laptop_sold = []

    while True:
        valid_id = int(
            input("To place an order,please provide the ID number of the laptop you'd like to sell:"))
        print("\n")

        if valid_id == 0:
            print("Exiting the program...")
            break

        # validating user input for the laptop ID and quantity
        while valid_id <= 0 or valid_id > len(read_laptop_stock()):
            print("Invalid Laptop ID. Try again!!")
            print("\n")
            valid_id = int(
                input("To place an order, please provide the ID number of the laptop you'd like to sell: "))

        laptop_quantity = 0
        while laptop_quantity is 0:
            quantity_input = input(
                "Please specify the quantity of laptops you wish to sell: ")
            if not quantity_input.isnumeric():
                print("Invalid input. Please enter a valid integer value.")
            elif int(quantity_input) <= 0:
                print("Invalid input. Quantity must be greater than 0.")
            else:
                laptop_quantity = int(quantity_input)

        mylaptop_dict = read_laptop_stock()

        getlaptop_quantity = mylaptop_dict.get(valid_id, [0, 0, 0, 0])[3]
        while laptop_quantity > int(getlaptop_quantity) or laptop_quantity <= 0:
            print("We're sorry, but the requested quantity of laptops is currently unavailable. Please select a different quantity or choose from our other available laptops.")
            laptop_quantity = 0
            while laptop_quantity is 0:
                quantity_input = input(
                    "Please specify the quantity of laptops you wish to sell: ")
                if not quantity_input.isnumeric():
                    print("Invalid input. Please enter a valid integer value.")
                elif int(quantity_input) <= 0:
                    print("Invalid input.The quantity must be greater than 0")
                else:
                    laptop_quantity = int(quantity_input)
            getlaptop_quantity = mylaptop_dict.get(valid_id, [0, 0, 0, 0])[3]
            print("\n")
        # Updating quanity of laptop in the text file

        mylaptop_dict[valid_id][3] = int(
            mylaptop_dict[valid_id][3]) - int(laptop_quantity)

        file = open("Laptop_stock.txt", "w")

        for values in mylaptop_dict.values():
            file.write(str(values[0])+"," + str(values[1])+"," + str(values[2]) +
                       "," + str(values[3])+"," + str(values[4])+"," + str(values[5]))
            file.write("\n")
        file.close()

        # Details of laptop sold

        laptop_name = mylaptop_dict[valid_id][0]
        laptop_brand = mylaptop_dict[valid_id][1]
        quantity_of_laptop = laptop_quantity
        unit_price = mylaptop_dict[valid_id][2]
        total_price_of_laptop = mylaptop_dict[valid_id][2].replace("$", '')
        final_price = int(total_price_of_laptop)*int(quantity_of_laptop)

        laptop_sold.append(
            [laptop_name, laptop_brand, quantity_of_laptop, total_price_of_laptop, final_price])

        sell_more = input(
            "Are you interested in selling more laptops? (Y/N): ")
        if sell_more.isalpha() and sell_more.lower() == 'n':
            break
        elif sell_more.isalpha() and sell_more.lower() == 'y':
            continue
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
            sell_more = input(
                "Are you interested in selling more laptops? (Y/N): ")
        if sell_more.lower() == 'n':
            break
        elif sell_more.lower() == 'y':
            continue
        else:
            print("Invalid input.Try again.")
            sell_more = input(
                "Are you interested in selling more laptops? (Y/N): ")
        if sell_more.lower() == 'n':
            break
        elif sell_more.lower() == 'y':
            continue
        else:
            print("Invalid input. Try again.")
            break

    date_time = datetime.now()

    print("\n")
    print("\t \t \t \t WelCome To Hrk Laptop Shop")
    print("\t \t\t Balkumari, Kathmandu | Contact No: 9814848773 ")
    print("----------------------------------------------------------------------------------------")
    print("\n")
    print("Customer Details: ")
    print("---------------------")
    print("Customer Name:" + str(full_name))
    print("Phone Number: " + str(phone))
    print("Date and Time: " + str(date_time))
    print("----------------------------------------------------------------------------------------")
    print("\n")
    print("Laptop Selling Details:")
    print("-----------------------------------------------------------------------------------------------------------------")
    print("Laptop Name \t\t\tBrand   \t\t Total Quantity \tUnit Price \tTotal")
    print("-----------------------------------------------------------------------------------------------------------------")

    for i in laptop_sold:
        print(i[0], "\t\t", i[1],
              "\t\t", i[2], "\t\t\t", i[3], "$", "\t", i[4])
    print("-----------------------------------------------------------------------------------------------------------------")

    total = 0
    shipping_Cost = 0
    while True:
        shipping_choice = input(
            "Dear Customer do you want your laptop to be shipped? (Y/N)")
        if shipping_choice.lower() == "y":
            shipping_Cost = 200
            break
        elif shipping_choice.lower() == "n":
            break
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")

    print("Shipping Cost:", shipping_Cost)
    print("Note: Shipping Cost added to grand total")

    for i in laptop_sold:
        total += int(i[4])
    final_total = total + shipping_Cost
    print("Total Amount:" + str(final_total))
    print("Note: Shipping Amount added to total amount")

    return full_name, phone, date_time, laptop_sold, shipping_Cost, final_total
