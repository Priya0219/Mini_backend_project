def individual_data(todo):
    return{
        "id": str(todo["_id"]),
        "title": todo["title"],
        "description": todo["description"],
        "is_completed": todo["is_completed"],
        "is_deleted": todo["is_deleted"],
        "updated_at": todo["updated_at"],
        "created_at" : todo["created_at"]
    }

def all_tasks(todos):
    return[individual_data(todo) for todo in todos]