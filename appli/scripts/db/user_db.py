import os
import sys
import mysql.connector

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from common import conf        

class User_db :
    
    def __init__(self) :
        self.db = mysql.connector.connect(
            host      = conf.host,
            user      = conf.user,
            password  = conf.password,
            database  = conf.database
        )
            
        self.cursor = self.db.cursor(buffered=True)
    
    
    
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~CRUD User~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
    
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~Read One User~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
    
    def get_user_by_username(self, username) :
        request = "SELECT * FROM {} WHERE username = '{}'".format(conf.user_table_name,
                                                                   username)
        self.cursor.execute(request)
        return self.cursor.fetchone()
    
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~Read All User~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
    
    def select_all(self) :
        request = "SELECT * FROM {}".format(conf.user_table_name)        
        self.cursor.execute(request)
        return self.cursor.fetchall()
    
    
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~Create One User~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
    
    def create_user(self, user) :
        request = "INSERT INTO {} (username, password) VALUES ('{}', '{}')".format(conf.user_table_name,
                                                                                    user.username, 
                                                                                    user.password)        
        self.cursor.execute(request)
        self.db.commit()
        
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~Update One User~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
        
    def update_user(self, user) :
        request = "UPDATE {} SET username = '{}', password = '{}' WHERE user_id = '{}'".format(conf.user_table_name,
                                                                                                user.username, 
                                                                                                user.password,
                                                                                                user.id)
        self.cursor.execute(request)
        self.db.commit()
        
    ##~~~~~~~~~~~~~~~~~~~~~~~~~~~~Delete One User~~~~~~~~~~~~~~~~~~~~~~~~~~~~##
        
    def delete_user(self, user) :
        request = "DELETE FROM {} WHERE id = '{}'".format(conf.user_table_name, user.id)

        self.cursor.execute(request)
        self.db.commit()