product = {
    "Laptop": 900,
    "Smartphone": 129,
    "Tablet": 100,
    "Headphones": 1000
}
total_price = 0
discounted_price = 0
for i in product.values():
    total_price += i
    discounted_price += i * 0.8

print(f"Total Price: {total_price}")
print(f"Discounted Price: {discounted_price}")
print(f"Discount: {int(total_price - discounted_price)}")


for i in product.keys():
    print(i)

for i in product.items():
    print(i)

# Enumaration:
for i in enumerate(product):
    print(i)
