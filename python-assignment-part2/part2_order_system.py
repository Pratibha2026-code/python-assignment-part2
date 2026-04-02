menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}


# Task 1 — Explore the Menu

# Given Data (Paste above this in your file)

# Step 1: Get all categories
categories = set()
for item in menu:
    categories.add(menu[item]["category"])

# Step 2: Print menu category-wise
for category in categories:
    print(f"\n===== {category} =====")
    
    for item, details in menu.items():
        if details["category"] == category:
            price = details["price"]
            status = "Available" if details["available"] else "Unavailable"
            print(f"{item:15} ₹{price:.2f}   [{status}]")

# Step 3: Total number of items
total_items = len(menu)
print("\nTotal items on menu:", total_items)

# Step 4: Total available items
available_items = 0
for item in menu:
    if menu[item]["available"]:
        available_items += 1

print("Total available items:", available_items)

# Step 5: Most expensive item
max_price = 0
expensive_item = ""

for item, details in menu.items():
    if details["price"] > max_price:
        max_price = details["price"]
        expensive_item = item

print("Most expensive item:", expensive_item, "₹", max_price)

# Step 6: Items under ₹150
print("\nItems under ₹150:")
for item, details in menu.items():
    if details["price"] < 150:
        print(item, "₹", details["price"])



# Task 1 Output

        # ===== Starters =====
# Paneer Tikka   ₹180.00   [Available]
# Chicken Wings  ₹220.00   [Unavailable]
# Veg Soup       ₹120.00   [Available]

# ===== Mains =====
# Butter Chicken ₹320.00   [Available]
# Dal Tadka      ₹180.00   [Available]
# Veg Biryani    ₹250.00   [Available]
# Garlic Naan    ₹40.00    [Available]

# ===== Desserts =====
# Gulab Jamun    ₹90.00    [Available]
# Rasgulla       ₹80.00    [Available]
# Ice Cream      ₹110.00   [Unavailable]

# Total items on menu: 10
# Total available items: 8
# Most expensive item: Butter Chicken ₹ 320.0

# Items under ₹150:
# Veg Soup ₹ 120.0
# Garlic Naan ₹ 40.0
# Gulab Jamun ₹ 90.0
# Rasgulla ₹ 80.0
# Ice Cream ₹ 110.0


# Task 2 — Cart Operations


cart = []

# Function to add item
def add_to_cart(item_name, quantity):
    if item_name not in menu:
        print(f"{item_name} does not exist in menu.")
        return
    
    if not menu[item_name]["available"]:
        print(f"{item_name} is currently unavailable.")
        return
    
    # Check if item already in cart
    for item in cart:
        if item["item"] == item_name:
            item["quantity"] += quantity
            print(f"Updated {item_name} quantity to {item['quantity']}")
            return
    
    # Add new item
    cart.append({
        "item": item_name,
        "quantity": quantity,
        "price": menu[item_name]["price"]
    })
    print(f"Added {item_name} x{quantity} to cart")


# Function to remove item
def remove_from_cart(item_name):
    for item in cart:
        if item["item"] == item_name:
            cart.remove(item)
            print(f"Removed {item_name} from cart")
            return
    print(f"{item_name} not found in cart")


# Function to print cart
def print_cart():
    print("\nCurrent Cart:")
    for item in cart:
        print(item)
    print()


# ---------------- SIMULATION ----------------

add_to_cart("Paneer Tikka", 2)
print_cart()

add_to_cart("Gulab Jamun", 1)
print_cart()

add_to_cart("Paneer Tikka", 1)  # should update quantity
print_cart()

add_to_cart("Mystery Burger", 1)  # does not exist
print_cart()

add_to_cart("Chicken Wings", 1)  # unavailable
print_cart()

remove_from_cart("Gulab Jamun")
print_cart()


# ---------------- ORDER SUMMARY ----------------

print("\n========== Order Summary ==========")

subtotal = 0

for item in cart:
    total_price = item["quantity"] * item["price"]
    subtotal += total_price
    print(f"{item['item']:15} x{item['quantity']}    ₹{total_price:.2f}")

print("------------------------------------")

gst = subtotal * 0.05
total = subtotal + gst

print(f"Subtotal:                ₹{subtotal:.2f}")
print(f"GST (5%):               ₹{gst:.2f}")
print(f"Total Payable:          ₹{total:.2f}")
print("====================================")


# Task 2 OUTPUT

# Added Paneer Tikka x2 to cart
# Current Cart:
# {'item': 'Paneer Tikka', 'quantity': 2, 'price': 180.0}

# Added Gulab Jamun x1 to cart
# Current Cart:
# {'item': 'Paneer Tikka', 'quantity': 2, 'price': 180.0}
# {'item': 'Gulab Jamun', 'quantity': 1, 'price': 90.0}

# Updated Paneer Tikka quantity to 3
# Current Cart:
# {'item': 'Paneer Tikka', 'quantity': 3, 'price': 180.0}
# {'item': 'Gulab Jamun', 'quantity': 1, 'price': 90.0}

# Mystery Burger does not exist in menu.
# Current Cart:
# {'item': 'Paneer Tikka', 'quantity': 3, 'price': 180.0}
# {'item': 'Gulab Jamun', 'quantity': 1, 'price': 90.0}

# Chicken Wings is currently unavailable.
# Current Cart:
# {'item': 'Paneer Tikka', 'quantity': 3, 'price': 180.0}
# {'item': 'Gulab Jamun', 'quantity': 1, 'price': 90.0}

# Removed Gulab Jamun from cart
# Current Cart:
# {'item': 'Paneer Tikka', 'quantity': 3, 'price': 180.0}

# ========== Order Summary ==========
# Paneer Tikka   x3    ₹540.00
# ------------------------------------
# Subtotal:                ₹540.00
# GST (5%):               ₹27.00
# Total Payable:          ₹567.00
# ====================================


# Task 3 — Inventory Tracker with Deep Copy

import copy

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

# Step 1: Deep Copy
inventory_backup = copy.deepcopy(inventory)

# Step 2: Modify original
inventory["Paneer Tikka"]["stock"] = 2

print("Modified Inventory:", inventory)
print("Backup Inventory:", inventory_backup)

# Step 3: Restore
inventory = copy.deepcopy(inventory_backup)

# Step 4: Cart from Task 2
cart = [
    {"item": "Paneer Tikka", "quantity": 3, "price": 180.0},
    {"item": "Garlic Naan", "quantity": 5, "price": 40.0},
    {"item": "Rasgulla", "quantity": 6, "price": 80.0},
]

# Step 5: Deduct stock
for entry in cart:
    item = entry["item"]
    qty = entry["quantity"]

    if item in inventory:
        if inventory[item]["stock"] >= qty:
            inventory[item]["stock"] -= qty
        else:
            print(f"⚠ Warning: Only {inventory[item]['stock']} {item} available")
            inventory[item]["stock"] = 0

# Step 6: Reorder Alert
for item, details in inventory.items():
    if details["stock"] <= details["reorder_level"]:
        print(f"⚠ Reorder Alert: {item} — Only {details['stock']} unit(s) left (reorder level: {details['reorder_level']})")

# Step 7: Final print
print("\nFinal Inventory:", inventory)
print("\nBackup Inventory (unchanged):", inventory_backup)


#Output Task 3
# Modified Inventory: Paneer Tikka stock becomes 2
# Backup Inventory: Paneer Tikka stock still 10 (proves deep copy works)

# ⚠ Warning: Only 4 Rasgulla available

# ⚠ Reorder Alert: Paneer Tikka — Only 7 unit(s) left (reorder level: 3)
# ⚠ Reorder Alert: Rasgulla — Only 0 unit(s) left (reorder level: 3)

# Final Inventory: updated after deduction
# Backup Inventory (unchanged): original values remain same





# Task 4 — Daily Sales Log Analysis

sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"], "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"], "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"], "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"], "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"], "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"], "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"], "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"], "total": 270.0},
    ],
}

# Revenue per day
daily_revenue = {}

for date, orders in sales_log.items():
    total = 0
    for order in orders:
        total += order["total"]
    daily_revenue[date] = total

print("Revenue per day:")
for date, total in daily_revenue.items():
    print(date, "→", total)

# Best-selling day
best_day = max(daily_revenue, key=daily_revenue.get)
print("\nBest-selling day:", best_day, "with revenue", daily_revenue[best_day])

# Most ordered item
item_count = {}

for orders in sales_log.values():
    for order in orders:
        for item in order["items"]:
            item_count[item] = item_count.get(item, 0) + 1

most_ordered = max(item_count, key=item_count.get)
print("\nMost ordered item:", most_ordered, "-", item_count[most_ordered], "times")

# Add new day
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
]

# Recalculate revenue
daily_revenue = {}

for date, orders in sales_log.items():
    total = sum(order["total"] for order in orders)
    daily_revenue[date] = total

print("\nUpdated Revenue per day:")
for date, total in daily_revenue.items():
    print(date, "→", total)

best_day = max(daily_revenue, key=daily_revenue.get)
print("\nUpdated Best-selling day:", best_day, "with revenue", daily_revenue[best_day])

# Numbered list
print("\nAll Orders:")

count = 1
for date, orders in sales_log.items():
    for order in orders:
        items = ", ".join(order["items"])
        print(f"{count}. [{date}] Order #{order['order_id']} — ₹{order['total']:.2f} — Items: {items}")
        count += 1



#Output Task 4

# Revenue per day:
# 2025-01-01 → 790.0
# 2025-01-02 → 560.0
# 2025-01-03 → 960.0
# 2025-01-04 → 570.0

# Best-selling day: 2025-01-03 with revenue 960.0

# Most ordered item: Garlic Naan - 5 times

# Updated Revenue per day:
# 2025-01-05 → 750.0 (added)

# Updated Best-selling day: 2025-01-03 with revenue 960.0

# 1. [2025-01-01] Order #1 — ₹220.00 — Items: Paneer Tikka, Garlic Naan
# 2. [2025-01-01] Order #2 — ₹210.00 — Items: Gulab Jamun, Veg Soup
# ...
# continues till Order #12