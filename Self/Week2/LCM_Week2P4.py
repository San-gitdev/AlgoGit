# python3
# Task. Given two integers 𝑎 and 𝑏, find their least common multiple.
# Input Format. The two integers 𝑎 and 𝑏 are given in the same line separated by space.
# Constraints. 1 ≤ 𝑎, 𝑏 ≤ 2 · 109.
# Output Format. Output the least common multiple of 𝑎 and 𝑏.
def gcd(i,j):
   
    k=i%j
    while(k!=0):
     #   print(i,j,k)
        i,j=j,k

        k=i%j
   # print("Returning value: ", j)
    return j

def lcm(y,z):
    x= gcd(y,z)
    #print ("GCD of ", y, " and ", z, " is ", x)
    #print(x,y,z)
    return ((y*z/x))

if __name__ == '__main__':
    a, b = map(int, input().split())
    if(a<b):
        c=lcm(b,a)
    else:
        c=lcm(a,b)
    print ((c))