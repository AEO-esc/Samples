class Dog:
    def __init__(self, age) -> None:
        self._age = age

    def get_age(self):
        print("Calling the getter...")
        return self._age
    
    def set_age(self, new_age):
        print("Calling the setter...")
        if isinstance(new_age, int) and 0 < new_age < 30:
            self._age = new_age;
        else:
            print("Invalid age: ", new_age)
    # <property_name> = property(<getter>, <setter>)
    age = property(get_age, set_age)

my_dog = Dog(8)

print(f"My dog is {my_dog.age} years old.")
print("One year later...")
my_dog.age += 1
print(f"My dog is now {my_dog.age} years old")