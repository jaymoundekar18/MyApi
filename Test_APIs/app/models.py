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
