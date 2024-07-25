class Home:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def __respuesta__(self):
        return f"{self.name} " + " " + f"{self.lastname}"
    



    def __str__(self):
        return f"{self.name} " + " " + f"{self.lastname}"