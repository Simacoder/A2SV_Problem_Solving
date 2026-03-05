# removing the occurence 
def remove_ele(arr, ele):
    k = 0
    for i in range(len(arr)):
        if arr[i] != ele:
            arr[k], arr[i] = arr[i], arr[k]
            k += 1
    return k

arr = [3, 2, 2, 3]
ele = 3

print(remove_ele(arr, ele))