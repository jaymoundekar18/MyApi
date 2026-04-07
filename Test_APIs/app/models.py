def employee_helper(employee) -> dict:
    return {
        "id": str(employee["_id"]),
        "firstname": employee["firstname"],
        "lastname": employee["lastname"],
        "gender": employee["gender"],
        "email": employee["email"],
        "address": employee["address"],
        "phone": employee["phone"],
        "empid": employee["empid"]
    }


def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "country": user["country"],
        "age": user["age"],
        "signup_date": user["signup_date"],
    }

def product_helper(product) -> dict:
    return {
        "id": str(product["_id"]),
        "name": product["name"],
        "price": product["price"],
        "category": product["category"],
        "in_stock": product["in_stock"],
    }

def order_helper(order) -> dict:
    return {
        "id": str(order["_id"]),
        "user_id": str(order["user_id"]),
        "items": [
            {
                "product_id": str(item["product_id"]),
                "quantity": item["quantity"],
                "price": item["price"],
            }
            for item in order["items"]
        ],
        "total_amount": order["total_amount"],
        "order_date": order["order_date"],
        "status": order["status"],
    }


def bank_customer_helper(customer) -> dict:
    return {
        "id": str(customer["_id"]),
        "user_id": customer["user_id"],
        "name": customer["name"],
        "phone_number": customer["phone_number"],
        "email": customer["email"],
        "account_number": customer["account_number"],
        "upi_id": customer["upi_id"],
        "account_balance": customer["account_balance"],
        "transactions": customer.get("transactions", [])
    }


# def transaction_helper(transaction) -> dict:
#     return {
#         "transaction_id": transaction["transaction_id"],
#         "from_user_id": transaction["from_user_id"],
#         "to_user_id": transaction["to_user_id"],
#         "amount": transaction["amount"],
#         "transaction_type": transaction["transaction_type"],
#         "status": transaction["status"],
#         "created_at": transaction["created_at"],
#     }


# def bank_customer_helper(customer) -> dict:
#     return {
#         "id": str(customer["_id"]),
#         "user_id": customer["user_id"],
#         "name": customer["name"],
#         "phone_number": customer["phone_number"],
#         "email": customer["email"],
#         "account_number": customer["account_number"],
#         "upi_id": customer["upi_id"],
#         "account_balance": customer["account_balance"],
#         "transactions": [
#             transaction_helper(txn) for txn in customer.get("transactions", [])
#         ]
#     }