
# 1. Get the name of the pet shop
def get_pet_shop_name(cc_pet_shop):
    pet_shop_name = cc_pet_shop["name"]
    return pet_shop_name


# 2. Get total cash from the pet shop
def get_total_cash(cc_pet_shop):
    total_cash = cc_pet_shop["admin"]["total_cash"]
    return total_cash


# 3 and 4. Add or remove cash from the total cash of the pet shop
def add_or_remove_cash(cc_pet_shop,money):
    cc_pet_shop["admin"]["total_cash"] += money # Update dict value for total cash
    total_cash_update = get_total_cash(cc_pet_shop)
    return total_cash_update

# 5. Get the number of pets sold
def get_pets_sold(cc_pet_shop):
    pets_sold = cc_pet_shop["admin"]["pets_sold"]
    return pets_sold

# 6. Increase the number of pets sold
def increase_pets_sold(cc_pet_shop,pets_number):
    cc_pet_shop["admin"]["pets_sold"] += pets_number # Update dict value for pets_sold
    pets_sold_update = get_pets_sold(cc_pet_shop)
    return pets_sold_update

# 7. Count how many pets are in the shop
def get_stock_count(cc_pet_shop):
    stock_count = len(cc_pet_shop["pets"])
    return stock_count

# 8 and 9. Get a list of pets of a specified breed
def get_pets_by_breed(cc_pet_shop,breed):
    breed_list = []
    pets = cc_pet_shop["pets"]
    for pet in pets:
        if pet["breed"] == breed:
            breed_list.append(pet)
    return breed_list

# 10 and 11. Get the pet dictionary by pet name
def find_pet_by_name(cc_pet_shop,pet_name):
    pets = cc_pet_shop["pets"]
    for pet in pets:
        if pet["name"] == pet_name:
            return pet

# 12. Remove a pet from the shop using said pet name
def remove_pet_by_name(cc_pet_shop, pet_name):
    pets = cc_pet_shop["pets"]
    for pet in pets:
        if pet["name"] == pet_name:
            pets.remove(pet)

# 13. Return the number of pets in the shop after adding a new one
def add_pet_to_stock(cc_pet_shop, new_pet):
    pets = cc_pet_shop["pets"]
    pets.append(new_pet)
    return get_stock_count(cc_pet_shop)

# 14. Returns the cash of a customer in the list
def get_customer_cash(customer):
    return customer["cash"]

# 15. Remove specified amount from specified customer cash
def remove_customer_cash(customer, amount):
    customer["cash"] -= amount

# 16. Get number of pets from a customer (value of that dic key is a list!!!)
def get_customer_pet_count(customer):
    return len(customer["pets"])

# 17. Add a new pet to the customer's list. New pet is a dict.
def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)

# 18 and 19. Check if customer can afford pet. Return True if so, False if not.
def customer_can_afford_pet(customer, new_pet):
    customer_cash = get_customer_cash(customer)
    pet_price = new_pet["price"]
    if customer_cash >= pet_price:
        return True
    else:
        return False

# 20. Check if customer has same amount of cash as new pet price:
def customer_can_afford_pet__exact_funds(customer, new_pet):
    customer_cash = get_customer_cash(customer)
    pet_price = new_pet["price"]
    if customer_cash == pet_price:
        return True

# INTEGRATION TESTS

# 1. Sell pet to customer:
    # a. Add pet to customer pets
    # b. Update pets sold
    # c. Update customer cash
    # d. Update shop cash

# cc_pet_shop, pet and customer are all dictionaries
def sell_pet_to_customer(cc_pet_shop,pet,customer):

    # Only run if pet is found and customer can afford it
    if pet != None and customer_can_afford_pet(customer, pet):
        add_pet_to_customer(customer, pet)
        increase_pets_sold(cc_pet_shop,1)
        remove_customer_cash(customer, pet["price"])
        add_or_remove_cash(cc_pet_shop, pet["price"])
