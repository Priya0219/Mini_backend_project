from fastapi import FastAPI,APIRouter,HTTPException
from configrations import collection
from database.models import todo_input
from database.schemas import all_tasks
from bson.objectid import ObjectId
from datetime import datetime
from router.delete_user import router as delete_user

app = FastAPI()
router = APIRouter()

@router.get("/")
async def get_all_todos():
    data = collection.find()
    return all_tasks(data)

@router.post("/")
async def create_todo(new_task: todo_input):
    try:
        resp = collection.insert_one(dict(new_task))
        return{"status_code":200, "id":str(resp.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code =500, detail=f"Some error occured {e}")

@router.put("/{task_id}")
async def update_todo(task_id:str, updated_task:todo_input):
    try:
        id = ObjectId(task_id)
        existing_doc = collection.find_one({"_id":id, "is_deleted":False})
        if not existing_doc:
            return HTTPException(status_code =404, detail="Task does not exsits")
        updated_task.updated_at = datetime.timestamp(datetime.now())
        resp = collection.update_one({"_id":id},{"$set":dict(updated_task)})
        return {"status_code":200, "message":"Task Updated Sccessfully"}

    except Exception as e:
        raise HTTPException(status_code =500, detail=f"Some error occured {e}")

@router.delete("/{task_id}")
async def delete_todo(task_id:str):
    try:
        id = ObjectId(task_id)
        existing_doc = collection.find_one({"_id":id, "is_deleted":False})
        if not existing_doc:
            return HTTPException(status_code =404, detail="Task does not exsits")
        resp = collection.update_one({"_id":id},{"$set":{"is_deleted":True}})
        return {"status_code":200, "message":"Task Deleted Sccessfully"}

    except Exception as e:
        raise HTTPException(status_code =500, detail=f"Some error occured {e}")
   
app.include_router(router,prefix="/Task", tags=["Todo App"])

app.include_router(delete_user,tags=["Delete User"])

