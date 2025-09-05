arr=[45,89,23,1,65,4,17,13,2]
arr = input()

# Bubble sort                O(n^2)
def bubbleSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

print(bubbleSort(arr))


#selection sort                   theta(n^2)
def selectionSort(arr):
    n=len(arr)
    for i in range(n-1):
        minj = i
        minx = arr[i]
        for j in range(i+1,n):
            if arr[j]<minx:
                minj = j
                minx=arr[j]
                arr[minj]=arr[i]
                arr[i]=minx
    return arr              

print(selectionSort(arr))


#insertion sort
def insertionSort(arr):
    n=len(arr)
    for i in range(n):
        x = arr[i]
        j = i-1
        while( x<arr[j] and j>-1):
            arr[j+1] = arr[j]
            j=j-1
            arr[j+1]=x
    return arr

print(insertionSort(arr))

#merge sort            n log n     !!!!!!!
def merge(u,v,t):
    i,j=1,1
    m=len(u)
    n=len(v)
    for k in range(1,n):
        if u[i]<v[j]:
            t[k]=u[i]
            i=i+1
        else:
            t[k]=v[i]
            j=j+1
    return t

def mergeSort(arr):
    n = len(arr)
    if n==1:
        merge(u,v,arr)
    else:        
        u,v=[],[]
        s=int(n/2)
        for i in range(s):
            u=arr[i]
        for i in range(s+1,n):
            v=arr[i]
        mergeSort(u)
        mergeSort(v)

g = mergeSort(arr)
print(g)


#QuickSort 
def quickSort(arr):
    pivot = arr[0]
    k=0
    
