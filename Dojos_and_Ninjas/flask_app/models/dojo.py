from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

mydb = 'dojos_and_ninjas_schema'

class Dojo:
    def __init__(self, db_data ):
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        # Create list for ninjas so that it can be associated
        # with a dojo.
        self.ninjas = []

    @classmethod
    def save(cls, data):
        query = '''INSERT INTO dojos 
        ( name, created_at, updated_at ) 
        VALUES ( %(name)s , NOW() , NOW() );'''
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(mydb).query_db( query, data )

    @classmethod
    def get_all(cls):
        query = '''SELECT * FROM dojos;'''

        results = connectToMySQL(mydb).query_db(query)
        print(results)
        return results

    @classmethod
    def get_dojo_with_ninjas( cls , data ):
        query = '''SELECT * FROM dojos LEFT JOIN ninjas 
        ON ninjas.dojo_id = dojos.id 
        WHERE dojos.id = %(id)s;'''
        results = connectToMySQL(mydb).query_db( query , data )

        dojo = cls( results[0] )
        for row_from_db in results:
            ninja_data = {
                "id" : row_from_db["ninjas.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "age" : row_from_db["age"],
                "created_at" : row_from_db["created_at"],
                "updated_at" : row_from_db["updated_at"]
            }
            dojo.ninjas.append( ninja.Ninja( ninja_data ) )
        return dojo