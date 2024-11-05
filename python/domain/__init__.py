"""
Transient Objects.
"""

class CustomResponse():
     def __init__(self, status, message, data):
        self.status = status
        self.message = message
        self.data = data

     def stringify(self):
         return "[ status: " + str(self.status) + " message: " +  str(self.message) + " content: " +  str(self.data) +" ]"


"""
Domain.
"""

class Example():
    def __init__(self, id, name):
      self.id = id
      self.name = name

    def stringify(self):
         return "[ id: " + str(self.id) + " name: " +  str(self.name) + " ]"