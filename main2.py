# print("Hello World")

# print("Hello Git")

# Введення (отримання даних)
#ім_я = input("Введіть ваше ім'я: ")

# Перетворення (обробка даних)
#вітання = f"Привіт, {ім_я}!"

# Виведення (виведення даних)
#print(вітання)


#age = input("How old are you? ")
#age = int(age)


#a = float(input("Введіть сторону квадрата a: "))
#P = 4 * a
#print(f"Периметр квадрата дорівнює {P}")


# # Встановлюємо ціни на продукти
# price_per_croissant = 1.04
# price_per_glass = 0.34
# price_per_coffee_pack = 4.42

# # Кількість кожного продукту
# num_croissants = int(input("Введіть кількість круасанів: "))
# num_glasses = int(input("Введіть кількість склянок: "))
# num_coffee_packs = int(input("Введіть кількість упаковок кави: "))

# # Обчислення загальної вартості
# total_cost = num_croissants * price_per_croissant + \
#              num_glasses * price_per_glass + \
#              num_coffee_packs * price_per_coffee_pack

# # Визначаємо кількість повних доларів і центів
# total_dollars = int(total_cost)
# total_cents = int(total_cost * 100)

# # Вивід результату
# print(f"Загальна вартість у повних доларах: {total_dollars} доларів")
# print(f"Загальна вартість у центах: {total_cents} центів")


# my_list = [1, "Hello", 3.14]
# print(my_list)

# my_list.append(4)
# print(my_list)

# my_list.remove("Hello")
# print(my_list)


# my_list = [1, 2, 3, 4, 2, 2, 5, 2]
# count_2 = my_list.count(2)
# print(count_2)  # Виведе 4, оскільки число 2 зустрічається 4 рази


# my_list = [1, 2, 3, 4, 5]
# print(len(my_list))


# nums = [3, 1, 4, 1, 5, 9, 2]
# nums.sort()
# nums.sort(reverse=True)
# print(nums)


# words = ["banana", "apple", "cherry"]
# words.sort(key=len)
# print(words)


# nums = [3, 1, 4, 1, 5, 9, 2]
# # sorted_nums = sorted(nums)
# sorted_nums_desc = sorted(nums, reverse=True)
# # print(sorted_nums)  # Виведе [1, 1, 2, 3, 4, 5, 9]
# print(sorted_nums_desc)


# words = ["banana", "apple", "cherry"]
# # sorted_words = sorted(words, key=len)
# sorted_words_desc = sorted(words, key=len, reverse=True)
# # print(sorted_words)  # Виведе ['apple', 'banana', 'cherry']
# print(sorted_words_desc)


# chars =  ['a', 'b']
# chars_copy = chars.copy()

# chars = ["banana", "apple", "cherry"]
# chars.reverse()
# print(chars)


# my_dict = {"name": "Alice", "age": 25, "city": "New York"}
# print(my_dict["name"])  # Виведе 'Alice'

# my_dict["age"] = 26  # Змінює вік на 26
# my_dict["email"] = "alice@example.com"  # Додає нову пару ключ-значення
# print(my_dict)

# del my_dict["age"]
# print(my_dict)

# print("name" in my_dict)
# print("age" in my_dict)


# numbers = {1, 2, 3}
# numbers.remove(3)
# print(numbers)  # {1, 2}

# numbers = {1, 2, 3}
# numbers.discard(4)
# print(numbers)  # {1, 3}


# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a.intersection(b))  # {3}
# print(a & b)  # {3}

# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a.difference(b))  # {1, 2}
# print(a - b)  # {1, 2}

# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a.symmetric_difference(b))  # {1, 2, 4, 5}
# print(a ^ b)  # {1, 2, 4, 5}

# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a.union(b))  # {1, 2, 3, 4, 5}
# print(a | b)  # {1, 2, 3, 4, 5}

# s = "Hello" 
# print(s.upper()) # Виведе 'HELLO'

# s = "Some Text"
# print(s.lower())  # Виведе 'some text'

# s = "Bill Jons"
# print(s.startswith("Bi"))  # Виведе True

# s = "hello.jpg"
# print(s.endswith("jpg"))  # Виведе True

# s = "hello world".capitalize()  # Результат: "Hello world"

# s = "hello world".title()  # Результат: "Hello World"

# "123".isdigit()  # True
# "hello".isalpha()  # True
# " ".isspace()  # True


# # Просте форматування рядка
# name = 'John'
# print('Hello, {}!'.format(name))

# # Форматування з декількома аргументами
# age = 25
# print('Hello, {}. You are {} years old.'.format(name, age))

# # Використання іменованих аргументів
# print('Hello, {name}. You are {age} years old.'.format(name='Jane', age=30))

# # Використання індексів для вказівки порядку аргументів
# print('Hello, {1}. You are {0} years old.'.format(age, name))


# s = "Hello, World!"
# first_five = s[:5]
# print(first_five)  # Виведе 'Hello'

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# odd_numbers = numbers[0:10:2]
# print(odd_numbers)

# odd_numbers = numbers[::2]  # Виведе [1, 3, 5, 7, 9]
# print(odd_numbers)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# reverse_numbers = numbers[::-1]
# print(reverse_numbers)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# copy_numbers = numbers[:]
# print(copy_numbers)


