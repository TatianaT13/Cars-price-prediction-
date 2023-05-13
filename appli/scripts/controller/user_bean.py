import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model.user import User
from db.user_db import User_db

class User_bean :
    
    def __init__(self, id:int=None, username:str='', password:str='') :
        self.user_db    = User_db()
        self.user       = User(id=id, username=username, password=password)
        
        
    def set_user(self, id:int=None, username:str='', password:str='') :
        self.user       = User(id=id, username=username, password=password)
        
        
        
    def form_user(self, user_list) :
        self.user       = User(id=user_list[0], username=user_list[1], password=user_list[2])
        return self.user
        
    def connect(self, username, password) -> bool:
        """Checks if the username/password combination exists in the database

        Args:
            username (string): username
            password (string): password
        
        Returns:
            boolean: True if connection was successful, false otherwise
        """
        if self.is_exist(username) :
            if password == self.user.password :
                return True
        self.destruct_user()
        return False
    
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~Check if the user exist and build user object~~~~~~~~~~~~~~~~~~~~~~~~~~~~##

    def is_exist(self, username)-> bool:
        """Checks if a user exists

        Args:
            username (string): username
        
        Returns:
            user | False: if user exists returns user object, False if user doesn't exist
        """
        return self.get_user_by_username(username=username)        
        
    
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~Destruct the user object~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
        
    def destruct_user(self) :
        """Destroy user object
        """
        self.set_user(id=-1, username='', password='')
        
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~CRUD user~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
    
   
    
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~Read user by username~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
       
    def get_user_by_username(self, username:str='') : 
        username    = username if username !='' else self.user.username
        user        = self.user_db.get_user_by_username(username=username)
        return self.form_user(user)

    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~Create One user ~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
        
    def create_user(self) :
        self.user_db.create_user(user=self.user)
        
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~Update One user ~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
        
    def update_user(self) :
        self.user_db.update_user(user=self.user)
        
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~Delete One user ~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
        
    def delete_user(self) :
        self.user_db.delete_user(user=self.user)