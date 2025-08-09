def calculate_total(discount, *prices, extra_charges=None):
    if extra_charges is None:
        extra_charges = {}

    total = 0

    for price in prices:
        total += price
        if price in extra_charges:
            total += extra_charges[price]

    # Apply discount
    total -= (total * discount / 100)
    return total


# Example usage:
items = (100, 101, 102)
charges = {100: 10, 101: 15, 102: 20}

final_amount = calculate_total(20, *items, extra_charges=charges)
print(f"Final Amount: {final_amount}")





# def my_function(arg1, arg2, *args, **kwargs):
#     print("Fixed arguments:", arg1, arg2)
#     print("Positional arguments (*args):", args)  # args will be a tuple
#     print("Keyword arguments (**kwargs):", kwargs) # kwargs will be a dictionary

# # Example calls:
# my_function(10, 20)
# my_function(10, 20, 30, 40)
# my_function(10, 20, name="Alice", age=30)
# my_function(10, 20, 30, 40, city="New York", zip_code="10001")