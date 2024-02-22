from db_connect import connect_to_database
from fastapi import HTTPException,APIRouter


crud_router = APIRouter()

@crud_router.post("/insert-data/")
async def insert_data():
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            query = "INSERT INTO `bolt_db`.`doctor` (`user_id`, `name`, `specialization`, `email`, `phone_no`, `patients`, `availability`) VALUES ('1', '2', '3', '4', '5', '6', '7');"
            cursor.execute(query)
            connection.commit()
            connection.close()
            return {"message": "Data inserted successfully"}
        else:
            raise HTTPException(status_code=500, detail="Unable to connect to database")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@crud_router.post("/CrudTest")
async def crudTest():
    return {"message": "Test POST call From CRUD APIs"}
