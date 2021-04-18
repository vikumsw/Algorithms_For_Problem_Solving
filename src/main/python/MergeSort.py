# merge sort
arr = [9,5,18,1]

def mergesort(arr):
    l = len(arr)
    if l==1:
        return

    a = arr[:l//2]
    b = arr[l//2:]

    mergesort(a)
    mergesort(b)

    i = j = k = 0
    while len(a)>i and len(b)>j:
        if a[i]<b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k]=b[j]
            j+=1
        k+=1

    while len(a)>i:
        arr[k] = a[i]
        i+=1
        k+=1

    while len(b)>j:
        arr[k] = b[j]
        j+=1
        k+=1


mergesort(arr)
print(arr)
