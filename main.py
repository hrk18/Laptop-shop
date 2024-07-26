from operation import buy_Laptop
from operation import sall_Laptop
from write import write_laptopbuyDetails, write_sellDetails


def display_available_laptops():
    print("------------------------------------------------------------------------------------------------------------")
    print("S.N. \t Name \t\t     Brand \t    Price \t Quantity \t Processor \t Graphic Card")
    print("------------------------------------------------------------------------------------------------------------")
    a = 1
    file = open("Laptop_stock.txt", "r")
    for line in file:
        print(a, "\t" + line.replace(",", "\t"))
        a = a + 1
    print("------------------------------------------------------------------------------------------------------------")
    file.close()
    print("\n")


print("\n")
print("----------------------------------------------------------------------------------------------------")
print("\t \t \t \t Welcome to Hrk Laptop Shop")
print("-----------------------------------------------------------------------------------------------------")
print("\t \t \t Address: Balkumari, Kathmandu | Contact: 9814848773")
print("-----------------------------------------------------------------------------------------------------")
print("\n")

continueLoop = True
while continueLoop:
    print("\n")
    print("Press 1 to buy laptops from manufacture")
    print("Press 2 to sell laptops to customer")
    print("Press 3 to display available laptops")
    print("Press 4 to exit")
    print("\n")
    print("---------------------------------------------------------------------------")
    try:
        user_response = int(input("Press 1,2,3 or 4 :"))
        if user_response == 1:
            company_name, contact_number, date_time, laptop_bought, VAT_amount, final_total = buy_Laptop()
            write_laptopbuyDetails(company_name, contact_number, date_time,
                                   laptop_bought, VAT_amount, final_total)

        elif user_response == 2:
            full_name, contact_number, date_time, laptop_sold, cost_of_shipping, final_total = sall_Laptop()
            write_sellDetails(full_name, contact_number, date_time,
                              laptop_sold, cost_of_shipping, final_total)

        elif user_response == 3:
            display_available_laptops()

        elif user_response == 4:
            continueLoop = False
            print("Thank you for Visiting our shop")

        else:
            print("Invalid input. Please Try again")
    except ValueError:
        print("Invalid input. Please enter  1, 2, 3 or 4.")
