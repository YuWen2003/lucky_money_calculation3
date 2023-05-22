letter=[50,20]
 
money=int(input())
if money>=1000:
    money=money-1000
letter.append(money)
 
money=int(input())
if money>=1000:
    money=money-1000
letter.append(money)
 
money=int(input())
if money>=1000:
    money=money-1000
letter.append(money)
 
money=int(input())
if money>=1000:
    money=money-1000
letter.append(money)
 
money=int(input())
if money>=1000:
    money=money-1000
letter.append(money)
 
print(letter)
letter.sort()
print(letter[-1])
print(letter)