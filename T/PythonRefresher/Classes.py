class Dog:

    def __init__(self, name="", age=0, furcolor=""):
        self.name = name
        self.age = age
        self.furcolor = furcolor

    def bark(self, str):
        print("Bark! "+ str)

mydog = Dog("Fido", 13, "Brown")

print(mydog.age)