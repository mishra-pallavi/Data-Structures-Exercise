# Write a program to reverse an array or string


def reverseList(A):
    start = 0
    end = len(A)-1
    while start < end:
        A[start],A[end] = A[end],A[start]
        start +=1
        end -=1

A = [1, 2, 3, 4, 5, 6]
RA = A[::-1]
print(RA)

print("Original List is : ",A)
reverseList(A)
print("Reverse list is : ",A)


def reverseListRecursive(arr,start,end):
    while start >= end:
        return
    arr[start],arr[end] = arr[end],arr[start]
    reverseListRecursive(arr,start+1,end-1)


arr = [1, 2, 3, 4, 5, 6]
start = 0
end = len(arr)-1
reverseListRecursive(arr,start,end)
print("reverce list by recursive: ",arr)