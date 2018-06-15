# python3
import array

def RecFn(n):
    RecArr=array.array('Q',[0,1])
    #for i in range (0,1):
      #  print (RecArr[i])
    for x in range(2,n+1):
        RecArr.append((RecArr[x-1]+RecArr[x-2]))
    print (RecArr[x], end="\n")
    return
if __name__ == '__main__':
    a = int(input())
    if(a==0 or a==1):
        print("1")
    else:
        RecFn(a)
