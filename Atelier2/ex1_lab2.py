import re

def extract_quantity(text):
    # Define regex pattern to match quantity (specifically word-based numbers)
    quantity_pattern = r"\b(one|two|three|four|five)\b"  # Matches specific word-based numbers

    # Find all matches of quantity in the text
    quantity_matches = re.findall(quantity_pattern, text, flags=re.IGNORECASE)

    return quantity_matches  # Return the list of quantities found

def extract_prices(text):
    # Define regex pattern to match prices with decimal parts
    price_pattern = r"\b\d+(?:,\d+)?\b"  # Matches integer or decimal numbers (prices)

    # Find all matches of prices in the text
    prices = re.findall(price_pattern, text)

    return prices  # Return the list of prices

# Function to calculate and print individual product quantities multiplied by prices
def calculate_and_print_product_quantities(input_text):
    # Extract quantities and prices from the input text
    quantities = extract_quantity(input_text)
    prices = extract_prices(input_text)

    # Validate extracted quantities and prices
    if not quantities:
        print("No quantity found in the text.")
        return
    if not prices:
        print("No price found in the text.")
        return

    # Convert word-based quantities to numeric values
    quantity_mapping = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5
    }
    numeric_quantities = [quantity_mapping.get(q.lower(), 0) for q in quantities]

    # Print the multiplication calculations and calculate the total
    print("-- Product Quantities Multiplied by Prices --")
    total = 0
    for quantity, price in zip(numeric_quantities, prices):
        product_price = quantity * float(price.replace(",", "."))
        total += product_price
        print(f"{quantity} * {price}: {product_price}")

    # Print the total of all product prices
    print("-- Total --")
    print(f"Total: {total}")

# Example usage with your provided text
input_text = "I bought three Samsung smartphones 150 $ each, four kilos of fresh banana for 1,2 dollar a kilogram and one Hamburger with 4,5 dollar"
calculate_and_print_product_quantities(input_text)