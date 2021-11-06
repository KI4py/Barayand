import math
a=int(input("[!] Enter the value of your vector please : "))
print("    360/0\n      ↑\n270 ←   → 90\n      ↓\n     180")
ja=int(input("[!] Enter the degrees of vectors please: "))
b=int(input("[!] Enter the value of your vector please: "))
print("    360/0\n      ↑\n270 ←   → 90\n      ↓\n     180")
jb=int(input("[!] Enter the value of your vector please: "))
if jb == ja:
    result=a+b
    print("\n[!]The result of two vectors : ",result)
if jb-ja==90 or ja-jb==90:
    result22=math.sqrt(a**2+b**2)
    print("\n[!]The result of two vectors : ",result22)

if jb-ja==180 or ja-jb==180:
    result12=a+b
    result11111=str(result12)
    if "-" in result11111:
        result11111=result11111.replace("-","")
        result111112=str(result11111)
        print("\n[!]The result of two vectors : ",result111112)
    else:
        print("\n[!]The result of two vectors : ",result11111)
