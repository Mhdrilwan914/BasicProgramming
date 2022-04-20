from asyncio import exceptions
#Here we search for years in a sentence and calculate the diff between the years

def seraching_integer(sentence):
    first_year=0
    last_year=0
    strlp=str.split(sentence)
    for items in strlp:
        try:
            orig_year=int(items)
        except Exception as e:
            print(e)
            continue

        if(first_year==0):
            first_year=orig_year
        else:
            if(last_year==0):
                last_year=orig_year
    gap=last_year-first_year
    print(gap)


def main():
    sentence=input("Enter the string: ")
    seraching_integer(sentence)
   
main()
