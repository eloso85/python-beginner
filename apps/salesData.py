def read_sales_data(filename):
    sales = {}
    with open(filename, 'r') as file:
        for line in file:
            product, amount = line.strip().split(': ')
            sales[product] = sales.get(product, 0) + int(amount)
    return sales


def total_sales(sales):
    return sum(sales.values())


def average_sales(sales):
    return total_sales(sales) / len(sales) if sales else 0


def best_selling_product(sales):
    return max(sales, key=sales.get)


def display_sales_summary(sales):
    print(f"Total Sales: {total_sales(sales)}")
    print(f"Average Sales per Product: {average_sales(sales)}")
    print(f"Best Selling Product: {best_selling_product(sales)}")


def main():
    sales_data_file = 'data/sales_data.txt'
    sales = read_sales_data(sales_data_file)
    display_sales_summary(sales)


if __name__ == "__main__":
    main()
