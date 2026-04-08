from bson import ObjectId
from app.database import employee_collection
from app.database import users_collection, products_collection, orders_collection, bank_collection
from app.models import employee_helper, user_helper, product_helper, order_helper, bank_customer_helper
from app.security import hash_password, verify_password
from datetime import datetime
import uuid

# ---------------------------
# Employee CURD operations
# ---------------------------

# CREATE
def add_employee(employee: dict):
    result = employee_collection.insert_one(employee)
    new_employee = employee_collection.find_one(
        {"_id": result.inserted_id}
    )
    return employee_helper(new_employee)

# READ ALL
def get_all_employees():
    return [
        employee_helper(emp)
        for emp in employee_collection.find()
    ]

# READ ONE
def get_employee(id: str):
    employee = employee_collection.find_one({"_id": ObjectId(id)})
    if employee:
        return employee_helper(employee)
    return None

# UPDATE
def update_employee(id: str, data: dict):
    employee_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": data}
    )
    employee = employee_collection.find_one({"_id": ObjectId(id)})
    return employee_helper(employee)

# DELETE
def delete_employee(id: str):
    employee_collection.delete_one({"_id": ObjectId(id)})
    return True


# ---------------------------
# E-commerce operations
# ---------------------------

# Get all users
def get_all_users():
    return [user_helper(user) for user in users_collection.find()]

# Get all products
def get_all_products():
    return [product_helper(product) for product in products_collection.find()]

# Get all orders
def get_all_orders():
    return [order_helper(order) for order in orders_collection.find()]



# -------------------------------------------------
# Authenticate User
# -------------------------------------------------

def authenticate_customer(user_id: str, password: str):
    customer = bank_collection.find_one({"user_id": user_id})
    if not customer:
        return None

    if not verify_password(password, customer["password"]):
        return None

    return bank_customer_helper(customer)

# -------------------------------------------------
# Customer Operations
# -------------------------------------------------

# Create New Customer
def add_customer(customer: dict):
    customer["password"] = hash_password(customer["password"])
    result = bank_collection.insert_one(customer)
    new_customer = bank_collection.find_one(
        {"_id": result.inserted_id}
    )
    return bank_customer_helper(new_customer)


# Get all Customers
def get_all_customers():
    return [
        bank_customer_helper(cust)
        for cust in bank_collection.find()
    ]


# Get Customer by ID
def get_customer_by_id(id: str):
    customer = bank_collection.find_one({"_id": ObjectId(id)})
    if customer:
        return bank_customer_helper(customer)
    return None


# Get Customer by User ID
def get_customer_by_user_id(user_id: str):
    customer = bank_collection.find_one({"user_id": user_id})
    if customer:
        return bank_customer_helper(customer)
    return None


# Update Customer
def update_customer(id: str, data: dict):
    if "password" in data:
        data["password"] = hash_password(data["password"])

    bank_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": data}
    )
    customer = bank_collection.find_one({"_id": ObjectId(id)})
    return bank_customer_helper(customer)


# Delete Customer
def delete_customer(id: str):
    bank_collection.delete_one({"_id": ObjectId(id)})
    return True



# -------------------------------------------------
# Transaction Operations
# -------------------------------------------------

# Add Transaction
def add_transaction(user_id: str, transaction: dict):
    bank_collection.update_one(
        {"user_id": user_id},
        {"$push": {"transactions": transaction}}
    )
    customer = bank_collection.find_one({"user_id": user_id})
    return bank_customer_helper(customer)


# Get Transactions
def get_transactions(user_id: str):
    customer = bank_collection.find_one({"user_id": user_id})
    if customer:
        return customer.get("transactions", [])
    return []


# Transfer Money
def transfer_money(from_user_id: str, to_user_id: str, amount: float):
    sender = bank_collection.find_one({"user_id": from_user_id})
    receiver = bank_collection.find_one({"user_id": to_user_id})

    if not sender or not receiver:
        return None

    if sender["account_balance"] < amount:
        return None

    trans_id = uniqueTransactionId()

    if update_accountBalance(from_user_id, to_user_id, sender["account_balance"], receiver["account_balance"], amount):
        send_transaction = {
            "transaction_id": trans_id,
            "from_user_id": from_user_id,
            "to_user_id": to_user_id,
            "amount": amount,
            "transaction_type": "send",
            "status": "success",
            "created_at": datetime.utcnow()
        }

        receive_transaction = {
            "transaction_id": trans_id,
            "from_user_id": from_user_id,
            "to_user_id": to_user_id,
            "amount": amount,
            "transaction_type": "receive",
            "status": "success",
            "created_at": datetime.utcnow()
        }

        bank_collection.update_one(
            {"user_id": from_user_id},
            {"$push": {"transactions": send_transaction}}
        )

        bank_collection.update_one(
            {"user_id": to_user_id},
            {"$push": {"transactions": receive_transaction}}
        )

        # Deduct from sender
        bank_collection.update_one(
            {"user_id": from_user_id},
            {"$inc": {"account_balance": -amount}}
        )

        # Add to receiver
        bank_collection.update_one(
            {"user_id": to_user_id},
            {"$inc": {"account_balance": amount}}
        )

        return True

def update_accountBalance(senderId: str, receiverId: str, sender_accountBal: float, receiver_accountBal: float, amount: float):
    current_senderBalance = sender_accountBal - amount
    current_receiverBalance = receiver_accountBal + amount

    try:
        bank_collection.update_one(
            {"user_id": senderId},
            {"$set": {"account_balance": current_senderBalance}}
        )

        bank_collection.update_one(
            {"user_id": receiverId},
            {"$set": {"account_balance": current_receiverBalance}}
        )
    except:
        return False

    else:
        return True

def generate_transaction_id():
    return "FBCT" + str(uuid.uuid4().int)[:5]

def uniqueTransactionId() -> str:
    existing_ids = {
        txn["transaction_id"]
        for user in bank_collection.find()
        for txn in user.get("transactions", [])
    }

    while True:
        transaction_id = generate_transaction_id()
        if transaction_id not in existing_ids:
            return transaction_id