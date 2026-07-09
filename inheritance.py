class Animal:
    def eat(self):
        print("Animal eats food")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
class cat(Animal):
    def meows(self):
        print ("cat meows")
class Duck(Animal):
    def quack(self):
        print("Duck quacks")
class lion(Animal):
    def roar(self):
        print("lion roar")

dog=Dog()
cat=cat()
duck=Duck()
lion=lion()

dog.eat()
dog.bark()
cat.eat()
cat.meows()
duck.eat()
duck.quack()
lion.eat()
lion.roar()



        