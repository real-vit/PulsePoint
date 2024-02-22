from flask import Flask
from flask_login import LoginManager, UserMixin
from .dbconnect import connect_to_database

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY'] = "thisisasecretkehy"

    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    login_manager=LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    # # Define User Model
    # class User(UserMixin):
    #     def __init__(self, user_id):
    #         self.id = user_id
    # # User Loader Function
    # @login_manager.user_loader
    # def load_user(user_id):
    #     connection = connect_to_database()
    #     cursor = connection.cursor()
    #     query = "SELECT * FROM auth WHERE user_id = %s"
    #     cursor.execute(query, (user_id,))
    #     user_data = cursor.fetchone()
    #     if user_data:
    #         return User(user_data[0])
    #     return None
        
    class User(UserMixin):
        def __init__(self, user_id, user_type):
            self.user_id = user_id
            self.user_type = user_type

    @login_manager.user_loader
    def load_user(user_id):
        connection = connect_to_database()
        cursor = connection.cursor()
        query = "SELECT * FROM auth WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        user_data = cursor.fetchone()
        if user_data:
            return User(user_data[0], user_data[4])
        return None
    return app