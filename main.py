def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 1. Input your Full Name
full_name = "Jeveme Arendain"

# 2. Check if the name contains symbols or numbers (spaces are allowed)
if not full_name.replace(" ", "").isalpha():
    print("Error: Names with symbols or numbers are excluded.")
else:
    # 3. Create the UNSORTED array (excluding spaces and duplicate letters)
    unsorted_array = []
    for char in full_name.upper():  # Convert to uppercase so 'E' and 'e' are treated as duplicates
        if char != " " and char not in unsorted_array:
            unsorted_array.append(char)

    # 4. Create the SORTED array using Bubble Sort
    sorted_array = bubble_sort(unsorted_array.copy())

    # 5. Display both arrays
    print("Full Name:     ", full_name)
    print("Unsorted Array:", unsorted_array)
    print("Sorted Array:  ", sorted_array)