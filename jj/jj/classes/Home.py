class Home:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def respuesta(self):
        return f"{self.name} " + " " + f"{self.lastname}"
    
    def favicon(self,xfavicon):
        self.favi = xfavicon
        return f"{self.favi}"

    def str(self):
        return f"{self.name} " + " " + f"{self.lastname}"