# python3
#    Task. Given two integers 𝑎 and 𝑏, find their greatest common divisor.
#   Input Format. The two integers 𝑎, 𝑏 are given in the same line separated by space.
#   Constraints. 1 ≤ 𝑎, 𝑏 ≤ 2 · 109.
#   Output Format. Output GCD(𝑎, 𝑏).
def gcd(x,y):
    z=x%y
    #print(x,y,z)
    if(z==0):
        print(y)
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
