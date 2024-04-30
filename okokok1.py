import re

def extract_product_names(text):
    # Define regex pattern to match product names near numerical data (within 2 words)
    product_pattern = r"(\w+\s+\w+\s+)([A-Z][a-zA-Z]*(?:\s+[A-Z][a-zA-Z]*)*)(?:\s+\w+\s+){0,2}(\d[\d,\.]*)"

    # Find all matches of product names near numerical data in the text
    product_matches = re.findall(product_pattern, text)

    # Extract product names from the matches
    product_names = [match[1].strip() for match in product_matches]

    return product_names

# Example usage with your provided text
input_text = "I bought three Samsung smartphones 150 $ each, four kilos of fresh banana for 1,2 dollar a kilogram and one Hamburger with 4,5 dollar"

# Extract and print only the names of products mentioned in proximity to numerical data
product_names = extract_product_names(input_text)
print("Product Names:")
for name in product_names:
    print(name)
