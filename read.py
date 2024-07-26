def read_laptop_stock():
    laptop_stock_file = open("Laptop_stock.txt", "r")
    laptop_SN = 1
    laptop_stock_dict = {}
    for line in laptop_stock_file:
        line = line.replace("\n", "")
        laptop_stock_dict[laptop_SN] = (line.split(","))
        laptop_SN += 1
    laptop_stock_file.close()
    return laptop_stock_dict
