# ========================================================
# SmartBuy Supermarket Billing System
# Course  : IPG101 - Introduction to Programming
# Examiner: Ansumana Kabba
# ========================================================

def display_receipt(customer_number, items, subtotal, discount, total):
    """Print a formatted receipt for one customer."""
    print("\n" + "=" * 48)
    print("        SMARTBUY SUPERMARKET")
    print("        Freetown, Sierra Leone")
    print("=" * 48)
    print(f"  Customer #: {customer_number}")
    print("-" * 48)
    print(f"  {'PRODUCT':<18} {'QTY':>4}  {'PRICE':>7}  {'TOTAL':>8}")
    print("-" * 48)
    for item in items:
        name  = item["name"]
        qty   = item["quantity"]
        price = item["price"]
        line  = qty * price
        print(f"  {name:<18} {qty:>4}  Le{price:>6.2f}  Le{line:>7.2f}")
    print("-" * 48)
    print(f"  {'Subtotal':<30} Le{subtotal:>7.2f}")
    if discount > 0:
        print(f"  {'Discount (10%)':<30} Le{discount:>7.2f}")
    print(f"  {'TOTAL TO PAY':<30} Le{total:>7.2f}")
    print("=" * 48)
    print("      Thank you for shopping with us!")
    print("=" * 48 + "\n")


def get_positive_float(prompt):
    """Keep asking until a valid positive number is entered."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("  Please enter a value greater than 0.")
            else:
                return value
        except ValueError:
            print("  Invalid input. Please enter a number.")


def get_positive_int(prompt):
    """Keep asking until a valid positive integer is entered."""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("  Please enter a whole number greater than 0.")
            else:
                return value
        except ValueError:
            print("  Invalid input. Please enter a whole number.")


def process_customer(customer_number):
    """Collect products and generate a bill for one customer."""
    items    = []                  # list (array) of product dictionaries
    subtotal = 0.0

    print(f"\n--- Customer #{customer_number} ---")
    print("Enter purchased products (type 'done' when finished).\n")

    while True:
        name = input("  Product name (or 'done'): ").strip()
        if name.lower() == "done":
            if len(items) == 0:
                print("  No products entered. Please add at least one product.")
                continue
            break
        if name == "":
            print("  Product name cannot be empty.")
            continue

        quantity   = get_positive_int("  Quantity purchased : ")
        unit_price = get_positive_float("  Price per unit (Le): ")

        line_total  = quantity * unit_price
        subtotal   += line_total

        items.append({
            "name"    : name,
            "quantity": quantity,
            "price"   : unit_price
        })
        print(f"  Added: {name}  ->  Le{line_total:.2f}\n")

    # Apply 10% discount if subtotal exceeds Le 500
    discount = subtotal * 0.10 if subtotal > 500 else 0.0
    total    = subtotal - discount

    display_receipt(customer_number, items, subtotal, discount, total)


def main():
    """Main loop - process customers until cashier exits."""
    print("\n" + "*" * 48)
    print("*   SMARTBUY SUPERMARKET BILLING SYSTEM   *")
    print("*" * 48)

    customer_number = 1

    while True:
        process_customer(customer_number)
        customer_number += 1

        again = input("Process another customer? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\nSystem closed. Goodbye!\n")
            break


if __name__ == "__main__":
    main()
