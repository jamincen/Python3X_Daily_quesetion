"""
    Topic：unorded list [5, 1, 8, 9, 2, 3, 6, 5, 7]
    Requirements: odd numbers are arranged in front of the order,
                  and even numbers are arranged in reverse order.
"""
# answer1
arr = [5, 1, 8, 9, 2, 3, 6, 5, 7]

a = []
b = []
for i in arr:
    # Even list
    if i % 2 == 0:
        a.append(i)
        continue
    # Odd list
    b.append(i)

# Even list in reverse order
a.sort(reverse=True)
# Odd list positve order
b.sort()
b = b + a
print(b)

# answer2
arr = [5, 1, 8, 9, 2, 3, 6, 5, 7]
# reverse order
arr.sort(reverse=True)
for i in range(len(arr)):
    if arr[i] % 2 != 0:
        # when iterating an even number,remove and put it first
        arr.insert(0, arr.pop(i))
print(arr)
