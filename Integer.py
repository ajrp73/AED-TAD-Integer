class Integer:

    def __init__(self, número=None):     

        if número != None and not isinstance(número, int):

            raise TypeError("El número debe ser un valor entero.")

        
        if número != None and isinstance(número, int):

            self.número = número
        else:
             self.número = 1

 
    def __str__(self):

            return f"Integer: {self.número}"

   

i1 = Integer()

i2 = Integer(2)

print(f"i1: {i1}")

print(f"i2: {i2}")