def write_sellDetails(custmer_name, contact_number, date_time, laptop_sold, shipping_Cost, final_total):
    with open(str(custmer_name) + "-sell-laptop" + ".txt", "w")as file:
        file.write("\n")
        file.write("\t \t \t \t WelCome To Hrk Laptop Shop")
        file.write("\n")
        file.write("\t \t \t Balkumari, Kathmandu | Contact No: 9814848773 ")
        file.write("\n")
        file.write(
            "-------------------------------------------------------------------------------------------\n")
        file.write("\n")
        file.write("\t\t\t\t\t Laptop Selling Details: ")
        file.write("\n")
        file.write(
            "-------------------------------------------------------------------------------------------\n")
        file.write("Customer Name:" + str(custmer_name))
        file.write("\n")
        file.write("Phone Number: " + str(contact_number))
        file.write("\n")
        file.write("Date and Time: " + str(date_time))
        file.write("\n")
        file.write("\n")
        file.write(
            "-------------------------------------------------------------------------------------------\n")
        file.write(
            "Laptop Name \t\t  Brand \t\t   Quantity \t\tUnit Price \t\tTotal")
        file.write("\n")
        file.write(
            "-------------------------------------------------------------------------------------------\n")
        for i in laptop_sold:
            file.write(str(i[0]) + "\t" + str(i[1]) + "\t\t\t" +
                       str(i[2]) + "\t\t\t\t" +  str(i[3]) + "\t\t\t"+ "$" + str(i[4])+"\n")
        file.write(
            "-------------------------------------------------------------------------------------------\n")
        file.write("\n")
        if shipping_Cost == 200:
            file.write("Shipping Cost:" + "" + str(shipping_Cost) + "\n")
            file.write("\n")
            file.write("Total Amount: $" + str(final_total) + "\t\t\t"
                       "[Note: Shipping Amount added to total amount]" + "\n")
            file.write("\n")
        else:
            file.write("Total Amount: $" + str(final_total))
        file.write(
            "\nThank you for shopping with us. Your support is greatly appreciated. !! \n")
        file.write("Please keep the receipt for your records ")


def write_laptopbuyDetails(company_name, company_contact, date_time, laptop_bought, VAT_amount, final_total_amount):
    with open(str(company_name) + "-buy-laptop" + ".txt", "w")as file:
        file.write("\n")
        file.write("\t \t \t \t  Welcome To Hrk Laptop Shop")
        file.write("\n")
        file.write("\t \t\t Balkumari, Kathmandu | Contact: 9814848773 ")
        file.write("\n")
        file.write(
            "-------------------------------------------------------------------------------------------\n")
        file.write("\t\t\t\t\t Laptop Buying Details ")
        file.write("\n")
        file.write(
            "--------------------------------------------------------------------------------------------\n")
        file.write("Company Name:" + str(company_name))
        file.write("\n")
        file.write("Contact: " + str(company_contact))
        file.write("\n")
        file.write("Date and Time: " + str(date_time))
        file.write("\n")
        file.write("\n")
        file.write(
            "-------------------------------------------------------------------------------------------\n")
        file.write("Laptop Name  \t\t Brand   \t\t Quantity \t\t Unit Price \t\t Total")
        file.write("\n")
        file.write(
            "-------------------------------------------------------------------------------------------\n")
        for i in laptop_bought:
            file.write(str(i[0]) + "\t" + str(i[1]) + "\t\t\t" +
                       str(i[2]) + "\t\t\t" +  str(i[3]) + "\t\t\t\t"+ "$" + str(i[4])+"\n")
        file.write(
            "-------------------------------------------------------------------------------------------\n")
        file.write("\n")
        if VAT_amount:
            file.write("Vat Amount:" + "" + str(VAT_amount) + "\n")
            file.write("\n")
            file.write("Total Amount: $" + str(final_total_amount) +
                       "\t\t[Note: Total Amount include VAT Amount + Total]"+"\n")
            file.write("\n")
        else:
            file.write("Total Amount: $" + str(final_total_amount))
        file.write(
            "\nThank you for shopping with us. Your support is greatly appreciated. !! \n")
        file.write("Please keep the receipt for your records ")
