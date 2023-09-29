# задача 1

import random

NUM_SIZE = 10
numbers = [random.randint(-10, 10) for i in range(NUM_SIZE)]
print(numbers)
neg_sum = 0
for num in numbers:
    if num < 0:
        neg_sum += num
print(neg_sum)
pair_sum = 0
for num in numbers:
    if num % 2 == 0:
        pair_sum += num
print(pair_sum)
unpair_sum = 0
for num in numbers:
    if num % 2 != 0:
        unpair_sum += num
print(unpair_sum)
mult = 1
for i in range(len(numbers)):
    if i != 0:
        if i % 3 == 0:
            mult *= numbers[i]
print(mult)

min_value = min(numbers)
max_value = max(numbers)
min_value_index = numbers.index(min_value)
max_value_index = numbers.index(max_value)
mult_i = 1
if max_value_index < min_value_index:
    for i in range(max_value_index + 1, min_value_index):
        mult_i *= numbers[i]
elif max_value_index > min_value_index:
    for i in range(min_value_index + 1, max_value_index):
        mult_i *= numbers[i]
print(mult_i)

first_positive = None
second_positive = None
sum_el = 0
for num in numbers:
    if num > 0:
        if first_positive is None:
            first_positive = numbers.index(num)
        second_positive = numbers.index(num)
if first_positive is not None and second_positive is not None:
    for i in range(first_positive + 1, second_positive):
        sum_el += numbers[i]
print(sum_el)

# задача 2

import random

NUM_SIZES = 15
num_list = [random.randint(-10, 10) for i in range(NUM_SIZES)]
print(num_list)
num_list2 = []
for num in num_list:
    if num != 0:
        if num % 2 == 0:
            num_list2.append(num)
print(num_list2)

num_list3 = []
for num in num_list:
    if num != 0:
        if num % 2 != 0:
            num_list3.append(num)
print(num_list3)

num_list4 = []
for num in num_list:
    if num < 0:
        num_list4.append(num)
print(num_list4)

num_list5 = []
for num in num_list:
    if num > 0:
        num_list5.append(num)
print(num_list5)
