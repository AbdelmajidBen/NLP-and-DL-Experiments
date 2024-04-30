import re

def generate_bill(text):
    # Define regular expressions to extract relevant information from the text
    item_regex = r"(\b\w+(\s\w+)*)"
    quantity_regex = r"(\d+[\s]?[k]?[g]?)"
    price_regex = r"(\d+(\.\d{2})?)"

    # Initialize lists to store extracted information
    items = []
    quantities = []
    prices = []

    # Find all matches for item, quantity, and price in the text
    item_matches = re.findall(item_regex, text)
    quantity_matches = re.findall(quantity_regex, text)
    price_matches = re.findall(price_regex, text)

    # Store the extracted information in the respective lists
    for match in item_matches:
        items.append(match[0])
        print(match)
    for match in quantity_matches:
        quantity = match[0].replace(" ", "").replace("kg", "").replace("g", "")
        quantities.append(float(quantity))
    for match in price_matches:
        price = match[0].replace(",", "")
        prices.append(float(price))

    # Calculate the total cost
    total_cost = sum(quantity * price for quantity, price in zip(quantities, prices))

    # Generate the bill
    bill = "Bill:\n"
    for item, quantity, price in zip(items, quantities, prices):
        bill += f"{item}: {quantity} x ${price:.2f} = ${quantity * price:.2f}\n"
    bill += f"Total: ${total_cost:.2f}"

    return bill

# Example usage
text = "I bought three Samsung smartphones 150 $ each, four kilos of fresh banana for 1.2 dollar a kilogram and one Hamburger with 4.5 dollar"
bill = generate_bill(text)
print(bill)

