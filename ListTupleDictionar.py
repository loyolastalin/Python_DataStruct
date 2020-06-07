# list mutable 

numbers = [1, 7, 9]
numbers[0] =200
print(numbers[0]) # prints the fist element
numbers.append(10)
numbers.insert(0, 44)
print(numbers)

# tuples are immutable
tuplelist = (1, 2, 3)

x, y, z = tuplelist
print(" x: {} y: {} z: {}".format(x, y, z))

# dictionary
customer = { 
    "name" : "Jhon",
    "age" : 30
}

dd = "new name"
customer[dd] = "stalin"
print(customer)
print(customer.get("dasd")) #  will retun None in the absense of an item
print(customer.get("dasd", "Default Value")) #  will retun None in the absense of an item