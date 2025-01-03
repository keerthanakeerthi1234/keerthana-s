def selection_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in the unsorted part of the array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the element at index i
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Input from user
user_input = input("Enter numbers separated by spaces: ")
# Convert the input string into a list of integers
arr = list(map(int, user_input.split()))

# Sort the array using selection sort
sorted_arr = selection_sort(arr)

# Output the sorted array
print("Sorted array:", sorted_arr)