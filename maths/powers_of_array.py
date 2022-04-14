from array import array
#testing git pull

def main():
    a=[]
    n=int (input("enter the size: "))
    b=[1]*n
    pow_num=int(input("enter the power: "))
    for i in range(0,n):
        j=int(input("Enter array elements -{}: ".format(i)))
        a.append(j)
    print(a)
    for x in range(0,n):
        for k in range(pow_num):
            b[x]=b[x]*a[x]
    
    print(b) 

main()

