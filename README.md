# Smart Communication Automation System

A Python-based CLI tool that automates customer communication by generating personalized messages using customer order data from a CSV file.

This project simulates a small business communication workflow where different types of messages (order confirmation, payment request, shipping update) can be generated automatically.

---

## Features

- Reads customer order data from a CSV file
- Calculates total order cost automatically
- Uses message templates for different communication types
- Generates personalized messages for customers
- Supports sending messages to:
  - All customers
  - A specific order ID
- Saves generated messages as individual `.txt` files

---

## Project Structure
project/
│
├── data/
│ └── customer's_data.csv
│
├── templates/
│ ├── order_confirmation.txt
│ ├── payment_request.txt
│ └── shipping_update.txt
│
├── output/
│ └── messages/
│
└── main.py

---

## How It Works

1. The program reads customer data from a CSV file.
2. It calculates the total order value (`pcs × price`).
3. The user chooses whether to send messages to:
   - all customers
   - a specific order ID
4. The user selects a message template.
5. The program replaces template placeholders with real customer data.
6. Personalized message files are generated in the `output/messages` folder.

---

## Example Template Placeholder

Example template:
Hello [customer_name],

Your order [order_id] has been successfully processed.

Total amount: [total]

Transport: [transport]
LR Number: [lr_no]

Thank you for your purchase!

The system automatically replaces placeholders like `[customer_name]` and `[order_id]` with real data.

---

## Example Output
ORD-9244_order.txt

Generated message:

---

## Technologies Used

- Python
- CSV file processing
- File handling
- Basic CLI interaction
- Template-based message generation

---

## Learning Objectives

This project helped me practice:

- Python scripting
- Working with CSV data
- File automation
- Data processing with dictionaries
- Building CLI tools
- Implementing a simple templating system

---

## Future Improvements

Possible future enhancements:

- Email integration for sending messages
- GUI interface
- Database integration
- Logging system
- Status-based automatic messaging

---

## Author

Built as a learning project while exploring Python automation and software development fundamentals.
