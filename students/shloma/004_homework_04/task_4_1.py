# Task 4.1

my_list = [0, 4, 3, 7, 6, 8, 4, 3, 1, 1, 1]

# 1) Use while
i = 0
my_new_list = []

while i < len(my_list):
    my_new_list.append(my_list[i] * -2)
    i += 1

# 2) Use for
my_new_list2 = [n * -2 for n in my_list]

print("Исходный список:", my_list)
print("Новый список (используя while):", my_new_list)
print("Новый список (используя for):", my_new_list2)

