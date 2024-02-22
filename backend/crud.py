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


#POST APIs to Insert User Accounts
#1. Doctor Info

@crud_router.post("/doctor_signup")
async def doctorSignup(json_data: dict):
    try:
        connection = connect_to_database()
        if connection:
            columns = ', '.join(json_data.keys())
            values_template = ', '.join(['%s'] * len(json_data))
            cursor = connection.cursor()
            query = f"INSERT INTO `bolt_db`.`doctor` ({columns}) VALUES ({values_template});"
            values = tuple(json_data.values())
            cursor.execute(query, values)
            connection.commit()
            connection.close()
            return {"Message":"Doctor Signup Success"}
        else:
            raise HTTPException(status_code=500, detail="Unable to connect to database")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#2. Patient Signup
@crud_router.post("/patient_signup")
async def doctorSignup(json_data: dict):
    try:
        connection = connect_to_database()
        if connection:
            columns = ', '.join(json_data.keys())
            values_template = ', '.join(['%s'] * len(json_data))
            cursor = connection.cursor()
            query = f"INSERT INTO `bolt_db`.`patient` ({columns}) VALUES ({values_template});"
            values = tuple(json_data.values())
            cursor.execute(query, values)
            connection.commit()
            connection.close()
            return {"Message":"patient Signup Success"}
        else:
            raise HTTPException(status_code=500, detail="Unable to connect to database")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

#3. Helper Signup
@crud_router.post("/helper_signup")
async def doctorSignup(json_data: dict):
    try:
        connection = connect_to_database()
        if connection:
            columns = ', '.join(json_data.keys())
            values_template = ', '.join(['%s'] * len(json_data))
            cursor = connection.cursor()
            query = f"INSERT INTO `bolt_db`.`doctor` ({columns}) VALUES ({values_template});"
            values = tuple(json_data.values())
            cursor.execute(query, values)
            connection.commit()
            connection.close()
            return {"Message":"Doctor Signup Success"}
        else:
            raise HTTPException(status_code=500, detail="Unable to connect to database")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

#VITALS UPLOAD
