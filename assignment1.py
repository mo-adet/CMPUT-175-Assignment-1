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

def getProductNames(products: list) -> dict:
    """

    :param products:
    :return:
    """
    product_names = {}
    for i in range(len(products)):

        product_id = products[i][0]
        product_name = products[i][1]

        product_names[product_id] = product_name

    return product_names

def getProductPrices(products: list) -> dict:
    """

    :param products:
    :return:
    """

    product_prices = {}
    for i in range(len(products)):
        product_id = products[i][0]
        product_price = products[i][2]
        product_prices[product_id] = int(product_price)

    return product_prices



def getSales(sales: list, returnals: list, products: list)->dict:
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
        product_id = sales[i][2]
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


def determineTopSales(net_sales: dict, product_names: dict, product_prices: dict)->None:
    """
    # Determines the top 3 items sold (along with the revenue) and prints them out to user.
    :param net_sales: dict of the net sales
    :param product_names: dict of the product names
    :return:
    """
    top_sales = []

    for id, sales in net_sales.items():
        top_sales.append([id, sales])

    # sorting the items in the list in descending order
    top_sales.sort(key=lambda x: x[1], reverse=True)
    # slicing the list so that the top three most selling items are left.
    top_sales = top_sales[:3]


    top_revenues = []
    for id, price in product_prices.items():
        products_sold = net_sales[id]
        product_revenue = float(price * products_sold)
        top_revenues.append([id, product_revenue])

    top_revenues.sort(key=lambda x: x[1], reverse=True)
    top_revenues = top_revenues[:3]


    # Outputting to user
    print("Top three number of items sold are: ")
    for i in range(len(top_sales)):
        product_id = top_sales[i][0]

        product_name = product_names[product_id]
        products_sold = net_sales[product_id]

        print(f"{product_name:>20} {products_sold:>3}")

    print("Top three largest sale revenues: ")
    for i in range(len(top_revenues)):
        product_id = top_revenues[i][0]
        product_revenue = top_revenues[i][1]
        product_name = product_names[product_id]
        print(f"{product_name:>20} ${product_revenue:<10,.2f}")



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

    net_sales = getSales(sales, returnals, products)
    print(net_sales)

    product_names = getProductNames(products)
    product_prices = getProductPrices(products)

    determineTopSales(net_sales, product_names, product_prices)

if __name__ == "__main__":
    main()