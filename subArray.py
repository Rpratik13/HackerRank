def findSubarray(a, k, n):

    # Data-structure to store all
    # the sub-arrays of size K
    vec=[]

    # Iterate to find all the sub-arrays
    for i in range(n-k+1):
        temp=[]

        # Store the sub-array elements in the array
        for j in range(i,i+k):
            temp.append(a[j])

        # Push the vector in the container
        vec.append(temp)

    # Sort the vector of elements
    print(vec)
    vec=sorted(vec)

    # The last sub-array in the sorted order
    # will be the answer
    print(vec)
    return vec[len(vec) - 1]

# Driver code

a =[1, 9, 2, 7, 9, 3]
k = 3
n = len(a)

# Get the sub-array
ans = findSubarray(a, k, n)

for it in ans:
    print(it,end=" ")
