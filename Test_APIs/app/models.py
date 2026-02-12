def employee_helper(employee) -> dict:
    return {
        "id": str(employee["_id"]),
        "firstname": employee["firstname"],
        "lastname": employee["lastname"],
        "gender": employee["gender"],
        "email": employee["email"],
        "address": employee["address"],
        "phone": employee["phone"],
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
