class Task:
    def __init__(self, id,description, status):
        self.id = id
        self.description = description
        self.status = status
    def get_id(self):
        return self.id

    def get_description(self):
        return self.description
    
    def set_id(self,id):
        self.id = id

    def set_description(self,description):
        self.description = description

    def set_status(self,status):
        self.status = status





