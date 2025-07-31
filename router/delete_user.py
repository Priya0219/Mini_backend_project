from fastapi import APIRouter
from configrations import collection
from bson.objectid import ObjectId

router = APIRouter()

@router.delete("/{object_id}")
def delete_User(object_id:str):
    id = ObjectId(object_id)
    del_user = collection.delete_one({"_id":id})
    return {"status":200,"data":"deleted user"}
    