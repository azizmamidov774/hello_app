# from dotenv import load_dotenv
# import os 

# load_dotenv()
# my_veriable = os.getenv('MY_KEY')

# print(my_veriable)
# def main():
#     print("Hello from hello!")

# name = "Mamidov"

# if __name__ == "__main__":
#     main()


# class Cat:
#     eyes = True
#     name = Мурка 
#     color = Black
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#     def run(self):
#         print("Кошка бежит")
# cat1 = Cat(name= "Мурка", color= "black")
# cat2 = Cat(name= "Борис", color= "orange")

# cat1.eyes = "У Мурки зеленые глаза"
# cat1.run()
# print(cat1.name, cat1.color, cat1.eyes)
# print(cat2.name, cat2.color)

# class npc:
#     name = "Pioneer"
#     body_color = "White"
#     hp = 100
#     def __init__(self, name, body_color, hp):
#         self.name = name
#         self.body_color = body_color
#         self.hp = hp
#     def __del__(self):
#         print("Персонаж убит")
#     def get_damage(self, damage):
#         self.hp -= damage
#         print("Pioneer получил урон -12")
#     def regenerate(self, regenrate):
#         self.hp += regenrate
#         print("Успешно вылечились на 5 hp")

# Pioneer_npc = npc(name="Pioneer", body_color="White", hp=100)
# Pioneer_npc.get_damage(12)
# print(Pioneer_npc.hp)


# Pioneer_npc.regenerate(5)
# print(Pioneer_npc.hp)

class Person:
    
    def __init__(self, name, age):
        self.__user_name = name 
        self.__user_age = age
    def print_person(self):
        print(f"Имя: {self.__user_name}, Возраст: {self.__user_age}")

    @property
    def age(self):
        return self.__user_age
    
    @age.setter
    def age(self, age):
        if 0 < age and age < 110:
            self.__user_age = age
        else:
            print("Недопустимый возвраст")




person_tom = Person("Tom", 34)

person_tom.age = 88
print(person_tom.age)
