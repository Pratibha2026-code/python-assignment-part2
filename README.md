# python-assignment-part2
# 🍽️ Restaurant Menu & Order Management System

This project is a command-line based Restaurant Order Management System built using Python’s core data structures such as dictionaries, lists, and nested data structures.

It simulates real-world restaurant operations including menu exploration, cart management, inventory tracking, and sales analysis.

---

## 📌 Objective

The goal of this project is to:

* Work with complex nested data structures
* Implement real-world logic using Python
* Simulate restaurant workflows such as ordering and inventory tracking
* Analyse sales data effectively

---

## 📋 Provided Data

The system uses three main datasets:

* **Menu** → Item details (category, price, availability)
* **Inventory** → Stock levels and reorder thresholds
* **Sales Log** → Daily order records

---

## 🧾 Task 1 — Explore the Menu

* Displayed menu grouped by categories:

  * Starters
  * Mains
  * Desserts
* Indicated item availability status
* Computed:

  * Total number of menu items
  * Total available items
  * Most expensive item
  * Items priced under ₹150

---

## 🛒 Task 2 — Cart Operations

* Implemented a cart system using a list of dictionaries

* Features:

  * Add items (with validation)
  * Prevent duplicate entries (update quantity instead)
  * Handle unavailable or invalid items
  * Remove items from cart
  * Update item quantities

* Simulated user actions:

  * Adding multiple items
  * Handling invalid/unavailable items
  * Removing items

* Generated final order summary:

  * Item-wise cost
  * Subtotal
  * GST (5%)
  * Total payable amount

---

## 📦 Task 3 — Inventory Tracker (Deep Copy)

* Created a deep copy of inventory using `copy.deepcopy()`

* Demonstrated that backup remains unchanged after modification

* Simulated order fulfilment:

  * Deducted stock based on cart
  * Handled insufficient stock cases

* Generated reorder alerts:

  * Triggered when stock ≤ reorder level

* Verified:

  * Original backup remains unchanged
  * Working inventory updates correctly

---

## 📊 Task 4 — Sales Log Analysis

* Calculated total revenue per day

* Identified best-selling day (highest revenue)

* Determined most ordered item across all days

* Added new sales data dynamically and updated results

* Displayed all orders using `enumerate()`:

  * Included date, order ID, total amount, and items

---

## 🛠️ Technologies Used

* Python (Core Concepts)

  * Dictionaries
  * Lists
  * Nested Data Structures
  * Loops & Conditionals
  * Functions
  * copy.deepcopy()

---

## 🚀 Key Learning Outcomes

* Handling nested data structures effectively
* Implementing real-world business logic
* Managing state (cart & inventory)
* Performing data aggregation and analysis
* Writing clean, modular Python code

---

## 📌 Conclusion

This project demonstrates how Python can be used to build a complete system that handles:

* Data management
* User interactions
* Inventory control
* Business analytics

It provides hands-on experience with real-world problem-solving using core programming concepts.

---

## 👩‍💻 Author

Pratibha Rathore
