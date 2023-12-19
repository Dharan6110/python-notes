class Human2:
    count = 0
    def __init__(self,gender,color):
        self.legs = 2
        self.hands = 2
        self.__feelings = "Sensitive"
        self.color = color
        self.gender = gender
        self.__heart = "Heart"
        self._genital_parts = "Genital Parts"

    def get_feelings(self):
        return self.__feelings

    def set_feelings(self,feeling):
        self.__feelings = feeling
        
    def __heart_beat(self):
        self.disease = "Heart Attack"
        print("Thinking....!")
        
    def living(self):
        self.__heart_beat()
        self.cry()
        
    def cry(self):
        print(self.count)
        print(f"Crying because of {self.__feelings} feelings")

    @classmethod
    def add_count(cls):
        print("Adding 1 to the count")
        cls.count += 1
        
a= Human2("Male","White")
print(a.legs)
print(a._genital_parts)
print(a.gender)