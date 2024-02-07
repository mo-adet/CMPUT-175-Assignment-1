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



def determineSales(sales: list, returnals: list, products: list):
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
        # Index that holds the product idea in the "sales" 2D array
        product_id =  sales[i][2]
        # Index that holds the product quantity bought in the "sales" 2D array.
        product_qty = sales[i][3]

        if product_id not in net_sales:
            # if the product id is not already in the net_sales dictionary, create the key
            net_sales[product_id] = int(product_qty)  # the value will be the product quantity

        else:
            # otherwise add the quantity to the already existing quantity
            net_sales[product_id] += int(product_qty)

        # --- NEXT DEDUCT THE NUMBER OF RETURNS.
        if sales[0] == returnals[0]:
            # removee the number of items that the customer orignally bought.
            net_sales[product_id] -= product_qty

    return net_sales

def determineTopSales(net_sales: dict, products):
    """

    :param net_sales:
    :return:
    """
    top_sales = []
    for key, value in net_sales:
        top_sales.append([key,value])








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

    net_sales = determineSales(sales, returnals, products)
    print(net_sales)

if __name__ == "__main__":
    main()