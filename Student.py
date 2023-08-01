class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"{self.id} - {self.name}"


class Student(User):
    def __init__(self, id, nama):
        super().__init__(id, nama)


class Teacher(User):
    def __init__(self, id, nama):
        super().__init__(id, nama)
