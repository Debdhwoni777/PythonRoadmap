
# ============================================================
#                 EXERCISE 4 — SHOPPING BILL
# ============================================================


# ------------------------------------------------------------
# 1. CUSTOMER INFORMATION
# ------------------------------------------------------------

customer_name = input("Enter your name: ")
phone_number = int(input("Enter your phone number: "))


# ------------------------------------------------------------
# 2. PRODUCT 1
# ------------------------------------------------------------

product_1 = input("Enter product 1 name: ")
price_1 = float(input("Enter price of product 1: "))
quantity_1 = int(input("Enter quantity of product 1: "))

product_1_price = price_1 * quantity_1


# ------------------------------------------------------------
# 3. PRODUCT 2
# ------------------------------------------------------------

product_2 = input("Enter product 2 name: ")
price_2 = float(input("Enter price of product 2: "))
quantity_2 = int(input("Enter quantity of product 2: "))

product_2_price = price_2 * quantity_2


# ------------------------------------------------------------
# 4. PRODUCT 3
# ------------------------------------------------------------

product_3 = input("Enter product 3 name: ")
price_3 = float(input("Enter price of product 3: "))
quantity_3 = int(input("Enter quantity of product 3: "))

product_3_price = price_3 * quantity_3


# ------------------------------------------------------------
# 5. PRODUCT 4
# ------------------------------------------------------------

product_4 = input("Enter product 4 name: ")
price_4 = float(input("Enter price of product 4: "))
quantity_4 = int(input("Enter quantity of product 4: "))

product_4_price = price_4 * quantity_4


# ------------------------------------------------------------
# 6. PRODUCT 5
# ------------------------------------------------------------

product_5 = input("Enter product 5 name: ")
price_5 = float(input("Enter price of product 5: "))
quantity_5 = int(input("Enter quantity of product 5: "))

product_5_price = price_5 * quantity_5


# ------------------------------------------------------------
# 7. STORE PRODUCTS IN A LIST
# ------------------------------------------------------------

products = [
    {
        "name": product_1,
        "price": price_1,
        "quantity": quantity_1,
        "total": product_1_price
    },
    {
        "name": product_2,
        "price": price_2,
        "quantity": quantity_2,
        "total": product_2_price
    },
    {
        "name": product_3,
        "price": price_3,
        "quantity": quantity_3,
        "total": product_3_price
    },
    {
        "name": product_4,
        "price": price_4,
        "quantity": quantity_4,
        "total": product_4_price
    },
    {
        "name": product_5,
        "price": price_5,
        "quantity": quantity_5,
        "total": product_5_price
    }
]


# ------------------------------------------------------------
# 8. CALCULATE SUBTOTAL
# ------------------------------------------------------------

subtotal = (
    product_1_price
    + product_2_price
    + product_3_price
    + product_4_price
    + product_5_price
)


# ------------------------------------------------------------
# 9. CALCULATE DISCOUNT
# ------------------------------------------------------------

# Subtotal >= 5000 → 20% discount
# Subtotal >= 3000 → 15% discount
# Subtotal >= 1500 → 10% discount
# Otherwise        → 0% discount


if subtotal >= 5000:
    discount = subtotal * 20 / 100
    discount_rate = 20

elif subtotal >= 3000:
    discount = subtotal * 15 / 100
    discount_rate = 15

elif subtotal >= 1500:
    discount = subtotal * 10 / 100
    discount_rate = 10

else:
    discount = 0
    discount_rate = 0


# ------------------------------------------------------------
# 10. FINAL TOTAL
# ------------------------------------------------------------

final_total = subtotal - discount


# ------------------------------------------------------------
# 11. DELIVERY CHARGE
# ------------------------------------------------------------

# Final total >= 3000 → Free Delivery
# Otherwise          → Delivery Charge: 50


if final_total >= 3000:
    delivery_charge = 0
    delivery_status = "Free Delivery"

else:
    delivery_charge = 50
    delivery_status = "Delivery Charge: 50"


# ------------------------------------------------------------
# 12. GRAND TOTAL
# ------------------------------------------------------------

grand_total = final_total + delivery_charge


# ------------------------------------------------------------
# 13. FINAL BILL
# ------------------------------------------------------------

print()
print("=" * 55)
print("                    SHOPPING BILL")
print("=" * 55)

print("Customer Name :", customer_name)
print("Phone Number  :", phone_number)

print("-" * 55)

print("Product 1     :", product_1)
print("Price         :", price_1)
print("Quantity      :", quantity_1)
print("Total         :", product_1_price)

print("-" * 55)

print("Product 2     :", product_2)
print("Price         :", price_2)
print("Quantity      :", quantity_2)
print("Total         :", product_2_price)

print("-" * 55)

print("Product 3     :", product_3)
print("Price         :", price_3)
print("Quantity      :", quantity_3)
print("Total         :", product_3_price)

print("-" * 55)

print("Product 4     :", product_4)
print("Price         :", price_4)
print("Quantity      :", quantity_4)
print("Total         :", product_4_price)

print("-" * 55)

print("Product 5     :", product_5)
print("Price         :", price_5)
print("Quantity      :", quantity_5)
print("Total         :", product_5_price)

print("=" * 55)

print("Subtotal      :", subtotal)
print("Discount      :", discount_rate, "%")
print("Discount Amt. :", discount)
print("After Discount:", final_total)
print("Delivery      :", delivery_status)
print("Grand Total   :", grand_total)

print("=" * 55)
print("              THANK YOU FOR SHOPPING!")
print("=" * 55)


# ### 🔴 Important correction

# You had:

# ```python
# final_total = subtotal + discount
# ```

# That would **increase** the bill.

# For a discount, it must be:

# ```python
# final_total = subtotal - discount
# ```

# For example:

# ```text
# Subtotal = ₹5000
# 20% discount = ₹1000

# Final Total = ₹5000 - ₹1000
#             = ₹4000
# ```

# Your exercise now combines **input → typecasting → lists → dictionaries → arithmetic operators → `if/elif/else` → calculations → formatted output**. 🐍🛒
