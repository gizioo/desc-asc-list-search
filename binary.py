def binarySearch(arr, l, r, x):
  
    # Check base case
    if r >= l:
  
        mid = l + (r - l) // 2
  
        # determine the order
        order = 1 if arr[0] < arr[-1] else -1

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
  
        # If element is smaller than mid, then it
        # can only be present in left subarray
        
        elif order * arr[mid] >  order * x:
            return binarySearch(arr, l, mid-1, x)
  
        # Else the element can only be present
        # in right subarray
        else:
            return binarySearch(arr, mid + 1, r, x)
  
    else:
        # Element is not present in the array
        return -1

if __name__ == '__main__':
    from test_cases import cases
    import time
    t0 = time.perf_counter()
    for _ in range(1000):
        for test_case in cases:
            left_arr = None
            right_arr = None
            split_index = 0
            for x in range(1, len(test_case['test_list'])):
                if test_case['test_list'][x - 1] < test_case['test_list'][x]:
                    split_index = x
                    left_arr = test_case['test_list'][:x]
                    right_arr = test_case['test_list'][x:]
                    break
            if not (left_arr or right_arr):
                # desc
                

                result = binarySearch(test_case['test_list'], 0, len(test_case['test_list']), test_case['test_element'])
            elif not left_arr:
                # asc
                
                result = binarySearch(test_case['test_list'], 0, len(test_case['test_list']), test_case['test_element'])
            else:
                result = binarySearch(left_arr, 0, len(left_arr), test_case['test_element'])
                
                if result < 0:
                    result = binarySearch(right_arr, 0, len(right_arr), test_case['test_element'])
                    # if result < 0:
                    #     print(-1)
                    # else:
                    #     print(result + split_index)
            #     else:
            #         print(result)
            # print(result)
    print(time.perf_counter() - t0)