def vbluser_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "fullname": user["fullname"],
        "email": user["email"],
        "username": user["username"],
        "books": user.get("books", []),
        "yearly_goal": user.get("yearly_goal",[]),
        "streak": user.get("streak", {"current_streak": 0, "longest_streak": 0, "last_read_date": None})
    }
