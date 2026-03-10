import os
import csv
from pprint import pprint

TEMPLATE_DIR = "templates/"
TEMPLATES = {
    "order": "order_confirmation.txt",
    "payment": "payment_request.txt",
    "shipping": "shipping_update.txt"
}


def load_template(template_key):
    filename = TEMPLATES.get(template_key)
    if not filename:
        raise ValueError("template not found!")

    path = os.path.join(TEMPLATE_DIR, filename)
    with open(path, mode="r", encoding="utf-8") as file:
        content_file = file.read()
    return content_file


def load_customers():
    data_list = []
    with open("data/customer's_data.csv", mode="r", newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data_list.append(row)

        for customer in data_list:
            customer["pcs"] = int(customer["pcs"])
            customer["price"] = int(customer["price"])
            customer["total"] = int(customer["pcs"]*customer["price"])
        return data_list


customer_data = load_customers()


def generate_message(template, customers_data):
    """replaces the keys information in the tmeplates with values from customers data"""
    new_file = template
    for key, value in customers_data.items():
        placeholder = f"[{key}]"
        new_file = new_file.replace(placeholder, str(value))
    return new_file


available = ", ".join(TEMPLATES.keys())

all_customer = input(
    "do you want to send to send same msg to all customers? type 'y' or 'n'")

if all_customer == "y":
    while True:
        user_choice = input(
            f"Which templates do you want to send? availabel templates: {available.title()} \n").lower()
        if user_choice not in TEMPLATES:
            print(
                "invalid selection, please choose from available list of templates.")
            continue
        template = load_template(user_choice)

        for customer in customer_data:
            personalized_msg = generate_message(template, customer)
            file_name = f"{customer['order_id']}_order.txt"
            with open(f"output/messages/{file_name}", mode="w", encoding="utf-8") as ready_msg:
                new_msg = ready_msg.write(personalized_msg)

            print(f"Generated: {file_name}")
        break
else:
    print("customer's order id ---- status")
    for customer in customer_data:
        print(f"{customer["order_id"]} : {customer["status"]}")

    while True:
        id = input(
            "\nOn which 'order_id' do you want to send msg? (type 'q' to quit):")

        # quit command
        if id.lower() in ["q", "quit"]:
            print("Exiting program...")
            break

        selected_customer = None

        for customer in customer_data:
            if customer["order_id"] == id:
                selected_customer = customer
                break
        if selected_customer is None:
            print(
                f"invalid order id{id}. please type valid order id from above.")
            continue

        user_choice = input(
            f"Which templates do you want to send? availabel templates: {available.title()} \n").lower()
        if user_choice not in TEMPLATES:
            print(
                "invalid selection, please choose from available list of templates.")
            continue

        template = load_template(user_choice)
        personalized_msg = generate_message(template, selected_customer)

        file_name = f"{selected_customer['order_id']}_order.txt"

        with open(f"output/messages/{file_name}", mode="w", encoding="utf-8") as ready_msg:
            new_msg = ready_msg.write(personalized_msg)

        print(f"massage generated: {file_name}")
