

items_in_cart = 0

# First option to raise an exception
if items_in_cart != 2:
    raise Exception("Products Cart cout not matching")

# Second option to raise exception, often used in automation
assert items_in_cart == 2