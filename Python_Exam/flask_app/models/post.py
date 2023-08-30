from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

mydb = 'Python_BeltExam_Schema'

class Post:
    def __init__(self, data):
        self.id = data['id']
        self.location = data['location']
        self.date = data['date']
        self.content = data['content']
        self.sasquatches = data['sasquatches']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.creator = None

    @staticmethod
    def validate_post(request):
        is_valid = True

        # LOCATION
        if len(request['location']) < 1:
            flash('Please Enter A Location')
            is_valid = False

        # DATE
        if len(request['date']) < 1:
            flash('Please Enter A Date')
            is_valid = False

        # CONTENT
        if len(request['content']) < 1:
            flash('Please Enter What Happened')
            is_valid = False

        # SASQUATCHES
        if len(request['sasquatches']) < 1:
            flash('Please Enter Number Of Sasquatches')
            is_valid = False

        return is_valid

    @classmethod
    def save(cls, data):
        query = '''INSERT INTO posts 
        ( location, date, content, 
        sasquatches, user_id, created_at, updated_at ) 
        VALUES ( %(location)s , %(date)s, 
        %(content)s, %(sasquatches)s, %(user_id)s, NOW() , NOW() );'''
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(mydb).query_db( query, data )

    @classmethod
    def get_all_posts_with_creator(cls):
        query = '''SELECT * FROM 
        posts JOIN users ON 
        posts.user_id = users.id 
        ORDER BY posts.created_at;'''
        results = connectToMySQL(mydb).query_db(query)
        posts = []
        for row in results:
            post = cls(row)
            post_creator_info = {
                "id" : row['users.id'],
                "first_name" : row['first_name'],
                "last_name" : row['last_name'],
                "email" : row['email'],
                "password" : row['password'],
                "created_at" : row['created_at'],
                "updated_at" : row['updated_at']
            }
            creator = user.User(post_creator_info)
            post.creator = creator
            posts.append(post)
        return posts

    @classmethod
    def getById_w_user(cls, data):
        query = '''SELECT * FROM 
        posts JOIN users ON 
        posts.user_id = users.id WHERE posts.id = %(post_id)s;'''
        results = connectToMySQL(mydb).query_db(query, data)
        row = results[0]
        post = cls(row)
        one_posts_user_info = {
            "id" : row['users.id'],
            "first_name" : row['first_name'],
            "last_name" : row['last_name'],
            "email" : row['email'],
            "password" : row['password'],
            "created_at" : row['users.created_at'],
            "updated_at" : row['users.updated_at']
            }
        creator = user.User(one_posts_user_info)
        post.creator = creator
        return post

    @classmethod
    def deleteById(cls, data):
        query = '''
        DELETE FROM posts
        WHERE id = %(post_id)s;'''
        results = connectToMySQL(mydb).query_db( query, data )
        print(f"results: {results}")

    @classmethod
    def editById(cls, data):
        query = '''
        UPDATE posts
        SET location = %(location)s,
        date = %(date)s,
        content = %(content)s,
        sasquatches = %(sasquatches)s
        WHERE id = %(post_id)s;'''
        return connectToMySQL(mydb).query_db( query, data )