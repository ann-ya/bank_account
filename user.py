class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        return f"Thank you, {self.name.title()}"