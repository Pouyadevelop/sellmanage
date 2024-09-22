"""class setting():
    def connection(self):
        with open("Driver.txt") as F:
            return str(F.read())



import os

class setting():
    def connection(self):
        print("Current working directory:", os.getcwd())
        with open("Driver.txt") as F:
            return str(F.read())
"""


class setting():
    def connection(self):
        try:
            with open("driver1") as F:
                return str(F.read())
        except FileNotFoundError:
            print("Error: The file 'driver1' was not found.")
            return None


