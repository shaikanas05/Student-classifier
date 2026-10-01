def selection_sort(arr):
    n=len(arr)
    
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                
        arr[i],arr[min_index]=arr[min_index],arr[i]

user_input= input("enter the number:")
data=[int(x) for x in user_input.split()]
print(selection_sort(data))
print("sorted data:",data)
    