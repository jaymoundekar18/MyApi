def vbluser_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "fullname": user["fullname"],
        "email": user["email"],
        "username": user["username"],
        "books": user.get("books", []),
        "yearly_goal": user.get("yearly_goal",0)
    }
