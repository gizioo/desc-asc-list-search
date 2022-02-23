def find_index(some_list, element):
    # if the list is empty
    if len(some_list) == 0:
        return -1

    # or has one element
    if len(some_list) == 1:
        if some_list[0] == element:
            return 0
        else:
            return -1

    # if it's outside the list range
    if element > some_list[0] and element > some_list[-1]:
        return -1

    middle_point = len(some_list) // 2

    
    # divide the lists in 2 kind of equal parts
    left_index = find_index(some_list[:middle_point], element)
    
    if left_index > -1:
        return left_index

    
    right_index = find_index(some_list[middle_point:], element)
    if right_index > -1:
        return right_index + middle_point
    return -1
    



from test_cases import cases
import time
t0 = time.perf_counter()
for _ in range(1000):
    for test_case in cases:
        result = find_index(test_case['test_list'], test_case['test_element'])
    #    print(result)
print(time.perf_counter() - t0)