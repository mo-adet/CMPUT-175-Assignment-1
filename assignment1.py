"""
Title: Assignment 1
Date: Feb 6, 2024
Author: Muhammad Adetunji
"""
# importing necessary libraries
import datetime

def openFile(filename: str) -> list[list]:
    """
    Opens the Files and returns the contents
    :param filename: str
    :return: data (2D array)
    """
    data = []
    with open(filename,"r") as file:
        reader = file.readlines()
        for line in reader:
            line = line.strip()
            data.append(line.split(","))

    # removing the headers.
    data.pop(0)

    return data


def getProdcutInfo(products: list) -> dict:
    """
    gets the name and price of each product
    :param products:
    :return: dict
    """
    # dictionary that uses the product ID to get another dictionary of the name and price
    product_infos = {}
    for i in range(len(products)):
        product_id = products[i][0]
        product_name = products[i][1]
        product_price = float(products[i][2])

        #  using the product ID as a key to another dict containing the name and price of the item
        product_infos[product_id] = {"name": product_name, "price": product_price }

    return product_infos

def getFilteredSalesInfo(sales: list, returnals: list )->dict:
    """
    gets the info of all the sales, removing the ones that have been returned
    :param sales:
    :return:
    """
    #  dictionary that will use the transcation ID as the key to the sale info
    filtered_sales_infos = {}
    # ['transaction_id', 'date', 'product_id', 'quantity', 'discount']
    for i in range(len(sales)):
        transaction_id = sales[i][0]
        date = sales[i][1]
        product_id = sales[i][2]
        quantity = int(sales[i][3])
        discount = float(sales[i][4])

        filtered_sales_infos[transaction_id] = {"date": date, "product id": product_id, "quantity": quantity, "discount":discount}

    # removing the ones that have been returned.
    for i in range(len(returnals)):
        # if the returnal_id is the same as the transaction id, we remove the corresponding key/item from the dict.
        returnal_id = returnals[i][0]
        if returnal_id in filtered_sales_infos:
            filtered_sales_infos.pop(returnal_id)


    return filtered_sales_infos

def getUnfilteredSalesInfo(sales: list)->dict:
    """
    gets all the sales, disregarding the returns
    :param sales:
    :return:
    """
    # same as the last UDF.
    unfiltered_sales_infos = {}
    # ['transaction_id', 'date', 'product_id', 'quantity', 'discount']
    for i in range(len(sales)):
        transaction_id = sales[i][0]
        date = sales[i][1]
        product_id = sales[i][2]
        quantity = int(sales[i][3])
        discount = float(sales[i][4])

        unfiltered_sales_infos[transaction_id] = {"date": date, "product id": product_id, "quantity": quantity,
                                                "discount": discount}

    return unfiltered_sales_infos
def getNumSales(sales_infos)->dict:
    """
    determines the top 3 sales
    :param sales_infos: dict
    :return: none
    """

    # intiating a dictionary that will hold the number of sales for product id
    num_sales = {}

    # --- FINDING THE NUMBER OF SALES FIRST.

    for transaction_id, sale_info in sales_infos.items():
        # id of the item that the customer bought
        product_id = sale_info["product id"]
        # amount the customer bought
        purchase_qty = sale_info["quantity"]

        if product_id not in num_sales:
            # if the product id is not already in the net_sales dictionary, create the key
            num_sales[product_id] = int(purchase_qty)  # the value will be the product quantity

        else:
            # otherwise add the quantity to the already existing quantity
            num_sales[product_id] += int(purchase_qty)

    return num_sales


def determineTopSales(net_sales: dict, product_infos: dict, sales_infos: dict) -> None:
    """
    # Determines the top 3 items sold  and prints them out to user.
    :param net_sales: dict of the net sales
    :param product_infos: dict of the product info for each product
    :return: None
    """
    top_sales = []

    for id, sales in net_sales.items():
        top_sales.append([id, sales])

    # sorting the items in the list in descending order
    top_sales.sort(key=lambda x: x[1], reverse=True) # lambda function so that it sort based on the number of sales
    # slicing the list so that the top three most selling items are left.
    top_sales = top_sales[:3]

    # Outputting to user
    print("Top three number of items sold are: ")
    for i in range(len(top_sales)):
        product_id = top_sales[i][0]

        product_name = product_infos[product_id]["name"]
        products_sold = net_sales[product_id]

        print(f"{product_name:>20} {products_sold:>3}")


def getNetRevenues(product_infos: dict, sales_infos: dict)-> dict:
    """
    Gets the total revenues generated from each product
    :param product_infos: dict
    :param sales_infos: dict
    :return:
    """
    # dict that will hold the total revenue generated from each item, using the product id as the key.
    net_revenues = {}
    # transaction_id is the transaction id
    for transaction_id, sale_info in sales_infos.items():
        # product id
        product_id = sale_info["product id"]
        purchase_quantity = sale_info["quantity"]
        product_price = product_infos[product_id]["price"]
        discount = sale_info["discount"]

        revenue = purchase_quantity * product_price
        # accounting for the discount
        actual_revenue = (1-discount) * revenue

        if product_id not in net_revenues:
            net_revenues[product_id] = actual_revenue

        else:
            net_revenues[product_id] += actual_revenue


    return net_revenues


def determineTopRevenues(net_revenues: dict, product_infos:dict) -> None:
    """
    Finds the top 3 revenue generators
    :param product_infos:
    :param net_revenues:
    :return:
    """
    top_revenues = []
    for product_id, revenue in net_revenues.items():
        top_revenues.append([product_id, revenue])

    top_revenues.sort(key=lambda x: x[1], reverse=True)
    top_revenues = top_revenues[:3]

    print("\nTop three revenues are: ")
    for i in range(len(top_revenues)):
        product_id = top_revenues[i][0]
        revenue = top_revenues[i][1]
        product_name = product_infos[product_id]["name"]

        print(f"{product_name:>20} ${revenue:10,.2f}")


def getDiscountAverages(sales_infos: dict):
    """
    Gets the discount averages for each product in percent form
    :param sales_infos: dict
    :return: dict
    """
    # dictionary that will keep track of the discount averages, using the product ID as the key.
    discount_averages = {}

    for transaction_id, sale_info in sales_infos.items():
        discounts = []
        # obtaining product ID
        product_id = sale_info["product id"]
        # Checking if we have already done the current product id
        if product_id not in discount_averages:
            for transaction_id, sale_info in sales_infos.items():
                # when the product is what we're looking for, add the discount to the list.
                if sale_info["product id"] == product_id:
                    discount = sale_info["discount"]
                    discounts.append(discount)
            # getting the average of the discounts
            discount_average = sum(discounts)/len(discounts)
            discount_averages[product_id] = discount_average * 100 # multiplying by 100 so it is in percent form.


    return discount_averages

def showDiscountAverages(discount_averages: dict, product_infos: dict, net_sales: dict, net_revnues:dict) -> None:
    """
    Displays the discount averages to the user in descneding order
    :param discount_averages: dict
    :param product_infos: dict
    :param net_sales: dict
    :param net_revnues: dict
    :return: None
    """
    # list that will hold the avg discounts of each item in descending order.
    top_discounts = []
    for product_id, avg_discount in discount_averages.items():
        units_sold = net_sales[product_id]
        product_price = product_infos[product_id]["price"]
        product_revenue = net_revnues[product_id]

        # determining the toal discounted amount for each of the products
        total_discounted = (product_price * units_sold) - product_revenue

        top_discounts.append([product_id, total_discounted])

    # sorting the list in descending order.
    top_discounts.sort(key=lambda x: x[1], reverse=True)

    # Outputting to user.
    for i in range(len(top_discounts)):
        product_id = top_discounts[i][0]
        product_name = product_infos[product_id]["name"]
        units_sold = net_sales[product_id]
        product_revenue = net_revnues[product_id]
        avg_discount = discount_averages[product_id]
        total_discounted = top_discounts[i][1]

        print("+---+--------------------+---+-----------+------+-----------+")
        print(f"|{product_id:3}|{product_name:20}|{units_sold:3}|${product_revenue:10,.2f}|{avg_discount:05.2f}%|${total_discounted:10,.2f}|")
    print("+---+--------------------+---+-----------+------+-----------+")


def determineWeekdaySales(sales_infos:dict) -> None:
    """
    determines and prints the amount of sales per weekday.
    :param sales_infos: dict (unfiltered)
    :return:
    """
    # dictionary that will hold the amount of sales per weekday.
    weekday_sales = {
        "Monday": 0,
        "Tuesday": 0,
        "Wednesday":0,
        "Thursday": 0,
        "Friday": 0,
        "Saturday": 0,
        "Sunday": 0,
    }

    for trans_id, sale_info in sales_infos.items():
        date = sale_info["date"]
        # splitting the date in to the day, month and year.
        date = date.split("-")
        year = int(date[0])
        month = int(date[1])
        day = int(date[2])

        date = datetime.datetime(year,month,day)

        # getting the name of the weekday.
        weekday = date.strftime("%A")

        weekday_sales[weekday] += 1

    print("\nSales for each day of the week: ")
    for weekday, sales in weekday_sales.items():
        print(f"{weekday:9}:{sales:3}")


def determineNumReturns(returnals:list, sales_infos:dict, product_infos):
    """
    Determines and displays the number of times an items has been returned
    :param returnals:
    :param sales_infos:
    :param product_infos:
    :return:
    """
    # dict that will hold the number of times returned for each item, using the product ID as the key.
    product_returns = {}
    for i in range(len(returnals)):
        transaction_id = returnals[i][0]
        product_id = sales_infos[transaction_id]["product id"]

        # if the item hasnt been done yet, create a key and add 1
        if product_id not in product_returns:
            product_returns[product_id] = 1

        else:
            product_returns[product_id] += 1

    # Outputting to user
    print("\nItems returned: ")
    for product_id, num_returns in product_returns.items():
        product_name = product_infos[product_id]["name"]
        print(f"{product_id:3} {product_name:20} {num_returns:3>}")


def writeToFile(filename: str, total_num_sales: dict) -> None:
    """
    writes the product ID and total number of units sold. (Assuming returns are ignored).
    :param filename: str
    :param total_num_sales: total number of sales for each id ignoring whether they have been returned
    :return:
    """
    # opening in the overwrite mode
    with open(filename, "w") as file:
        file.write("Product_ID, Total_Units_Sold\n")
        for product_id, num_sold in total_num_sales.items():
            # converting the integer to str so that it cna written to the file.
            num_sold = str(num_sold)
            line = ",".join([product_id, num_sold])
            # writting the data to the file.
            file.write(f"{line}\n")




def main():
    """
    main loop program runs through
    :return: none
    """
    # asking for the name of the sales file
    sales_file = input("Sales File: ")
    # ['transaction_id', 'date', 'product_id', 'quantity', 'discount']
    sales = openFile(sales_file)

    # asking for the name of the returns file
    returnals_file = input("Returns File: ")
    # ['transaction_id', 'date']
    returnals = openFile(returnals_file)

    # asking for the name of the products file
    products_file = input("Products File: ")
    # ['Product_ID', 'Product_Name', 'Price']
    products = openFile(products_file)

    # Q1
    product_infos = getProdcutInfo(products)
    filtered_sales_infos = getFilteredSalesInfo(sales, returnals)
    unfiltered_sales_infos = getUnfilteredSalesInfo(sales)

    # Q2
    total_num_sales = getNumSales(unfiltered_sales_infos)
    net_sales = getNumSales(filtered_sales_infos)
    net_revenues = getNetRevenues(product_infos, filtered_sales_infos)

    # Q3
    determineTopSales(net_sales, product_infos, filtered_sales_infos)
    determineTopRevenues(net_revenues, product_infos)
    discount_averages = getDiscountAverages(filtered_sales_infos)
    showDiscountAverages(discount_averages,product_infos,net_sales,net_revenues)

    # Q4
    determineWeekdaySales(unfiltered_sales_infos)

    # Q5
    determineNumReturns(returnals,unfiltered_sales_infos,product_infos)

    # Q6
    writeToFile("transaction_units.txt",total_num_sales)

if __name__ == "__main__":
    main()