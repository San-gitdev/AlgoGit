# python3


def gcd(x,y):
    z=x%y
    print(x,y,z)
    if(z==0):
        print("gcd is ",y)
        return
    else:    
        gcd(y,z)
    return
    


if __name__ == '__main__':
    a, b = map(int, input().split())
    if(a<b):
        gcd(b,a)
    else:
        gcd(a,b)
