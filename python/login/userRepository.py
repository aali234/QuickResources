'''A simple class to represnt a user'''


class userRepo:
    def __init__(self,uid,email,name,username,dob="") -> None:
        self.uid = uid
        self.email = email
        self.name = name
        self.username = username
        self.dob = dob
    
    
    def get_uid(self):
        return self.uid
    
    def get_email(self):
        return self.email
    
    def get_name(self):
        return self.name
    
    def get_username(self):
        return self.username
 


        
    
