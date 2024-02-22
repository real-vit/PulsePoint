from db_connect import connect_to_database
from fastapi import HTTPException, APIRouter

crud_router = APIRouter()


@crud_router.post("/CrudTest")
async def crudTest():
    return {"message": "Test POST call From CRUD APIs"}


"""
================================
POST APIs for Signup related activities.
================================
"""

# 1. Doctor Info


@crud_router.post("/doctor_signup")
async def doctorSignup(json_data: dict):
    try:
        connection = connect_to_database()
        if connection:
            columns = ", ".join(json_data.keys())
            values_template = ", ".join(["%s"] * len(json_data))
            cursor = connection.cursor()
            query = f"INSERT INTO `bolt_db`.`doctor` ({columns}) VALUES ({values_template});"
            values = tuple(json_data.values())
            cursor.execute(query, values)
            connection.commit()
            connection.close()
            return {"Message": "Doctor Signup Success"}
        else:
            raise HTTPException(status_code=500, detail="Unable to connect to database")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 2. Patient Signup
@crud_router.post("/patient_signup")
async def doctorSignup(json_data: dict):
    try:
        connection = connect_to_database()
        if connection:
            columns = ", ".join(json_data.keys())
            values_template = ", ".join(["%s"] * len(json_data))
            cursor = connection.cursor()
            query = f"INSERT INTO `bolt_db`.`patient` ({columns}) VALUES ({values_template});"
            values = tuple(json_data.values())
            cursor.execute(query, values)
            connection.commit()
            connection.close()
            return {"Message": "patient Signup Success"}
        else:
            raise HTTPException(status_code=500, detail="Unable to connect to database")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 3. Helper Signup
@crud_router.post("/helper_signup")
async def doctorSignup(json_data: dict):
    try:
        connection = connect_to_database()
        if connection:
            columns = ", ".join(json_data.keys())
            values_template = ", ".join(["%s"] * len(json_data))
            cursor = connection.cursor()
            query = f"INSERT INTO `bolt_db`.`doctor` ({columns}) VALUES ({values_template});"
            values = tuple(json_data.values())
            cursor.execute(query, values)
            connection.commit()
            connection.close()
            return {"Message": "Doctor Signup Success"}
        else:
            raise HTTPException(status_code=500, detail="Unable to connect to database")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


"""
================================
APIs for Vitals related
================================
"""

# 1. Vitals Upload (POST)

from datetime import datetime


@crud_router.post("/vitals_upload")
async def vitalsUpload(json_data: dict):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()

            columns = ", ".join([*json_data.keys(), "date"])
            values_template = ", ".join(["%s"] * (len(json_data) + 1))

            today_date = datetime.now().date().strftime("%Y-%m-%d")

            values = (*json_data.values(), today_date)

            query = f"INSERT INTO `bolt_db`.`vitals` ({columns}) VALUES ({values_template});"
            cursor.execute(query, values)
            connection.commit()
            connection.close()
            return {"Message": "Vitals Successfully Uploaded"}
        else:
            raise HTTPException(status_code=500, detail="Unable to connect to database")
    except Exception:
        return {"Message": "Vitals can be posted only once per day."}


# 2. Vitals Update (PUT)


@crud_router.put("/vitals_edit/{vital_id}")
async def vitalsUpdate(vital_id: int, json_data: dict):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()

            set_values = ", ".join([f"{key} = %s" for key in json_data.keys()])

            values = list(json_data.values())
            values.append(vital_id)

            query = f"UPDATE `bolt_db`.`vitals` SET {set_values} WHERE vital_id = %s;"

            cursor.execute(query, tuple(values))
            connection.commit()
            connection.close()
            return {"Message": "Vitals Successfully Updated"}
        else:
            raise HTTPException(status_code=500, detail="Unable to connect to database")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# 3. Vitals Delete (DELETE)


@crud_router.delete("/vitals_delete/{vitals_id}")
async def vitalsDelete(vitals_id: int):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()

            query = "DELETE FROM `bolt_db`.`vitals` WHERE vital_id = %s;"

            cursor.execute(query, (vitals_id,))
            connection.commit()
            connection.close()
            return {"Message": "Vitals Successfully Deleted"}
        else:
            raise HTTPException(status_code=500, detail="Unable to connect to database")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@crud_router.get("/vitals_fetch/{user_id}")
async def vitalsFetch(user_id: int):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()

            query = "SELECT * FROM `bolt_db`.`vitals` WHERE user_id = %s ORDER BY date DESC;"

            cursor.execute(query, (user_id,))

            rows = cursor.fetchall()

            vitals_list = []
            for row in rows:
                vitals_dict = {
                    "UserID": row[0],
                    "PulseRate": row[1],
                    "SysPressure": row[2],
                    "DiaPressure": row[3],
                    "BloodSugar": row[4],
                    "VitalID": row[5],
                    "StepCount": row[6],
                    "SleepDuration": row[7],
                    "Symptoms": row[8],
                    "RecordDate": row[9].strftime("%Y-%m-%d"),
                }
                vitals_list.append(vitals_dict)

            connection.close()
            return {"Vitals": vitals_list}
        else:
            raise HTTPException(status_code=500, detail="Unable to connect to database")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
