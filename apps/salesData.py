def read_sales_data(filename):
    sales = {}
    with open(filename, 'r') as file:
        for line in file:
            product, amount = line.strip().split(': ')
            sales[product] = sales.get(product, 0) + int(amount)
    return sales