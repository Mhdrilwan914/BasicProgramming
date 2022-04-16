import numbers
import pdb
from array import array


def sorting(arr):
    n=len(arr)
    for i in range(n,1,-1):
        for x in range(0,i-1):
            if arr[x]>arr[x+1]:
                swap(x,x+1,arr)
                


def swap(k,b,arr):
    temp=arr[k]
    arr[k]=arr[b]
    arr[b]=temp

def check_in(arr):
    sorting(arr)
    print("Sorted array is ",arr)
    crnt_val=arr[0]
    crnt_cnt=0
    high_val=arr[0]
    high_cnt=0
    for i in arr:
       
        if(crnt_val==i):
            crnt_cnt+=1
        else:
            if(crnt_cnt>high_cnt):
                high_cnt=crnt_cnt
                high_val=crnt_val
            crnt_val=i
            crnt_cnt=1
    if(crnt_cnt>high_cnt):
        high_cnt=crnt_cnt
        high_val=crnt_val
    
            
    print("Highest repeated item : {}".format(high_val))
    print("Highest count : {}".format(high_cnt))


def main():
    arr=[]
    n=int(input("Enter the size of an array: "))
    for i in range(0,n):
        numbers=int(input("Enter the numbers: "))
        arr.append(numbers)
    check_in(arr)
main()


