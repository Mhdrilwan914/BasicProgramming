from array import array


def bubblesort(un_arr):
    n=len(un_arr)
    for i in range(n,2,-1):
        for j in range(i-1):
            if un_arr[j]>un_arr[j+1]:
                swap(j,j+1,un_arr)

    print(un_arr)

def swap(a,b,arr):
    temp=arr[a]
    arr[a]=arr[b]
    arr[b]=temp


def main():
    arr=[]
    
    n=int (input("enter the list size: "))
    for i in range(0,n):
        x=int(input("entrer element number- {}: ".format(i)))
        arr.append(x)


    bubblesort(arr)
    
main()

