class User:
    def __init__(self, first_name:str, last_name:str, id:str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

class Data:
    def __init__(self, errors:str=None, value:User=None) -> None:
        self.errors = errors
        self.value = value
