from main import app
from db_connect import cursor

@app.get("/okay")
def okay():
    cursor.execute("INSERT INTO `bolt_db`.`doctor` (`user_id`, `name`, `specialization`, `email`, `phone_no`, `patients`, `availability`) VALUES ('1', '2', '3', '4', '5', '6', '7');")
