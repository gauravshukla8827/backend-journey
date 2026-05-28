import random
"""num = random.randint(1, 4)
print(num)
import my_module
print(my_module.favorite_number)"""



num = random.random()*10
print(num)
num = random.uniform(1,4)
print(num)

choice = random.randint(1,2)
if choice == 1:
    print("Head")

else:
    print("Tail")

fruit = ["a", "b", "c"]
print(fruit[0])


print(random.choice(fruit))
# or
pick = random.randint(0, 2)
print(fruit[pick])
print(fruit[3])