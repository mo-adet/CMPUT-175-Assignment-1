"""
Title: Assignment 1
Date: Feb 6, 2024
Author: Muhammad Adetunji
"""
import datetime

def openFile(filename: str):
    """
    Opens the Files and returns the contents
    :param filename:
    :return:
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

    :param products:
    :return:
    """
    product_infos = {}
    for i in range(len(products)):
        product_id = products[i][0]
        product_name = products[i][1]
        product_price = float(products[i][2])

        product_infos[product_id] = {"name": product_name, "price": product_price }

    return product_infos

def getSalesInfo(sales: list, returnals: list ):
    """
    gets the info of all the sales, removing the ones that have been returned
    :param sales:
    :return:
    """
    sales_infos = {}
    # ['transaction_id', 'date', 'product_id', 'quantity', 'discount']
    for i in range(len(sales)):
        transaction_id = sales[i][0]
        date = sales[i][1]
        product_id = sales[i][2]
        quantity = int(sales[i][3])
        discount = float(sales[i][4])

        sales_infos[transaction_id] = {"date": date, "product id": product_id, "quantity": quantity, "discount":discount}

    # removing the ones that have been returned.
    for i in range(len(returnals)):
        returnal_id = returnals[i][0]
        if returnal_id in sales_infos:
            sales_infos.pop(returnal_id)

    print(sales_infos)

    return sales_infos


def getNetSales(sales: list, returnals: list, products: list)->dict:
    """
    determines the top 3 sales
    :param sales:
    :param returnals:
    :return: none
    """

    # intiating a dictionary that will hold the number of sales for product id
    net_sales = {}

    # --- FINDING THE NUMBER OF SALES FIRST.

    for i in range(len(sales)):
        # index that holds the transaction id
        transaction_id = sales[i][0]
        # Index that holds the product idea in the "sales" 2D array
        product_id = sales[i][2]
        # Index that holds the product quantity bought in the "sales" 2D array.
        purchase_qty = int(sales[i][3])


        if product_id not in net_sales:
            # if the product id is not already in the net_sales dictionary, create the key
            net_sales[product_id] = int(purchase_qty)  # the value will be the product quantity

        else:
            # otherwise add the quantity to the already existing quantity
            net_sales[product_id] += int(purchase_qty)

        # --- NEXT DEDUCT THE NUMBER OF RETURNS.
        for j in range(len(returnals)):
            # if the transaction is the same as the return id...
            return_id = returnals[j][0]
            if return_id == transaction_id:
                net_sales[product_id] -= purchase_qty


    return net_sales


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
    top_sales.sort(key=lambda x: x[1], reverse=True)
    # slicing the list so that the top three most selling items are left.
    top_sales = top_sales[:3]

    # Outputting to user
    print("Top three number of items sold are: ")
    for i in range(len(top_sales)):
        product_id = top_sales[i][0]

        product_name = product_infos[product_id]["name"]
        products_sold = net_sales[product_id]

        print(f"{product_name:>20} {products_sold:>3}")


def getNetRevenues(product_infos: dict, sales_infos: dict, returnals: list):
    """

    :param product_infos:
    :param sales_infos:
    :return:
    """
    net_revenues = {}
    # transaction_id is the transaction id
    for transaction_id, sale_info in sales_infos.items():
        # product id
        product_id = sale_info["product id"]
        quantity = sale_info["quantity"]
        product_price = product_infos[product_id]["price"]
        discount = sale_info["discount"]

        revenue = quantity * product_price
        # accounting for the discount
        actual_revenue = (1-discount) * revenue

        if product_id not in net_revenues:
            net_revenues[product_id] = actual_revenue

        else:
            net_revenues[product_id] += actual_revenue

        for j in range(len(returnals)):
            return_id = returnals[j][0]
            if return_id == transaction_id:
                net_revenues[product_id] -= quantity

    return net_revenues


def determineTopRevenues(net_revenues: dict, product_infos:dict) -> None:
    """

    :param prodcut_infos:
    :param net_revenues:
    :return:
    """
    top_revenues = []
    for product_id, revenue in net_revenues.items():
        top_revenues.append([product_id, revenue])

    top_revenues.sort(key=lambda x: x[1], reverse=True)
    top_revenues = top_revenues[:3]

    print("Top three revenues are: ")
    for i in range(len(top_revenues)):
        product_id = top_revenues[i][0]
        revenue = top_revenues[i][1]
        product_name = product_infos[product_id]["name"]

        print(f"{product_name:>20} ${revenue:<10,.2f}")


def getDiscountAverages(sales_infos: dict, sales):
    """
    Gets the discount averages for each product
    :param sales_infos: dict
    :return:
    """
    # dictionary that will keep track of the discount averages, using the product ID as the key.
    discount_averages = {}

    for transaction_id, sale_info in sales_infos.items():
        discounts = []
        # obtaining product ID
        product_id = sale_info["product id"]
        # Checking if we have already done the current product id
        if product_id not in discount_averages:
            # iterate throught the sales list and get the discounts.
            for i in range(len(sales)):
                discount = float(sales[i][4])
                if product_id == sales[i][2]: # product id in the sales list.
                    discounts.append(discount)
            # getting the average of the discounts
            discount_average = sum(discounts)/len(discounts)
            discount_averages[product_id] = discount_average

    return discount_averages

def showDiscountAverages(discount_averages: dict):
    """
    displays the discount averages to the user
    :param discount_averages:
    :return:
    """





def main():
    """
    main loop program runs through
    :return: none
    """
    # ['transaction_id', 'date', 'product_id', 'quantity', 'discount']
    sales = openFile("transactions_Sales.csv")
    # ['transaction_id', 'date']
    returnals = openFile("transactions_Returns.csv")
    # ['Product_ID', 'Product_Name', 'Price']
    products = openFile("transactions_Products.csv")
    print(sales)
    print(returnals)
    print(products)

    product_infos = getProdcutInfo(products)

    sales_infos = getSalesInfo(sales, returnals)

    net_sales = getNetSales(sales, returnals, products)
    net_revenues = getNetRevenues(product_infos, sales_infos, returnals)


    determineTopSales(net_sales, product_infos, sales_infos)
    determineTopRevenues(net_revenues, product_infos)

if __name__ == "__main__":
    main()