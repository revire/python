### put your python code here
##x = int(input())
##hours = x//60
##min = x/60 - hours 
##min *= 60
##print(hours)
##print(round(min))


##x = int(input())
##h = int(input())
##m = int(input())
##
##start = (h*60 + m)
##finish = start + x
##hours = finish //60
##min = (finish/60-hours)*60
##print(hours)
##print(round(min))

##x = 5
##y = 10
##print(y > x * x or y >= 2 * x and x < y)


##a = int(input())
##b = int(input())
##h = int(input())
##if (h > b):
##    print ('Пересып')
##elif h >= a:
##    print('Это нормально')
##elif (h < a):
##    print('Недосып')    
##    
##

##y = int(input())
##if ((y%100 == 0) and (y%400 == 0)):
##    print('Високосный')
##elif ((y%4)==0 and (not(y%100 == 0) and not(y%400 == 0))):
##    print('Високосный')
##else:
##    print('Обычный')

##import math
##x = int(input())
##y = int(input())
##z = int(input())
##pp = (x+y+z)/2
##s = math.sqrt(pp*(pp-x)*(pp-y)*(pp-z))
##print(s)

#(−15,12]∪(14,17)∪[19,+∞)


##x = int(input())
##if((x > -15 and x <= 12) or (x > 14 and x < 17) or (x >= 19)):
##    print('True')
##else:
##    print('False')


##x = float(input())
##y = float(input())
##z = input()
##if z == '+':
##    print(x + y)
##elif z == '-':
##    print(x-y)
##elif z == '*':
##    print(x*y)
##elif z == '/':
##    if y == 0:
##        print('Деление на 0!')
##    else:    
##        print(x/y)
##elif z == 'mod':
##    if y == 0:
##        print('Деление на 0!')
##    else:
##        print(x%y)
##elif z == 'pow':
##    print(x**y)    
##elif z == 'div':
##    if y == 0:
##        print('Деление на 0!')
##    else:
##        print(x//y)



##import math
##n = input()
##
##if n == 'треугольник':
##    a = float(input())
##    b = float(input())
##    c = float(input())
##    pp = (a+b+c)/2
##    s = math.sqrt(pp*(pp-a)*(pp-b)*(pp-c))
##    print(s)
##elif n == 'прямоугольник':
##    a = float(input())
##    b = float(input())
##    print(a*b)
##
##if n == 'круг':
##    r = float(input())
##    print(r**2*3.14)


##a = int(input())
##b = int(input())
##c = int(input())
##
##if (a>=b) and (a>=c):
##    print(a)
##    (print(b), print(c)) if b<=c else (print(c), print(b))
##
##
##elif (b>=a) and (b>=c):
##    print(b)
##    (print(a), print(c)) if a<=c else (print(c), print(a))
##    
##elif (c>=b) and (c>=a):
##    print(c)
##    (print(b), print(a)) if b<=a else (print(a), print(b))

    

    
##while True:
##    b = "программист"
##    a = int(input())
##    if a%100 in [11,12,13,14]:
##        print(a, b+"ов") 
##    elif(a%10==1):
##        print(a, b)       
##    elif a%10 in [2, 3, 4]:
##        print(a, b+"а")
##    elif a%10 in [0,5,6,7,8,9]:    
##        print(a, b+"ов")
##    elif (a=="break"):
##        break    



##while True:
##    a = input()
##    b = int(a[0])+int(a[1])+int(a[2])
##    c = int(a[3])+int(a[4])+int(a[5])
##    print("Счастливый") if c == b else print("Обычный")
##    if (a=="b"): break


##i = 0
##while i < 5:
##    print('*')
##    if i % 2 == 0:
##        print('**')
##    if i > 2:
##        print('***')
##    i = i + 1


##a = int(input())
##b = int(input())
##x = 0
##y = 0
##
##if(a>b):
##    x = a
##    y = b
##else:
##    x = b
##    y = a
##c = 0
##while True:
##    c = x%y
##    x = y
##    y = c
##    if(c == 0):
##        break
##print(int((a*b)/x))

##while True:
##    a = int(input())
##    if(a<10):
##        continue
##    elif(a>100):
##        break
##    else:
##        print(a)

##a = int(input())
##b = int(input())
##c = int(input())
##d = int(input())
##print('\t', c, d)
##for j in range(a, b+1):
##    print(j, '\t', j*c, j*d)



##a = int(input())
##b = int(input())
##c = int(input())
##d = int(input())
##lst = list(range(c, d+1))
##k=0
##print('\t', end='')
##while(k<len(lst)):
##    if(k==lst[-1]):
##        print(lst[k], '\n')
##    print(lst[k], end=' ')
##    k+=1
##  
##for j in range(a, b+1):
##      print('\n', j, end=" ")
##      i=0
##      while(i<len(lst)):
##          if(i==lst[-1]):
##              print(j*lst[i])
##          print(j*lst[i], end=' ')
##          i+=1


##a = int(input())
##b = int(input())
##lst = []
##for i in range(a, b+1):
##    if(i%3==0):
##        lst.append(i)
##print(lst)        
##res = sum(lst)/len(lst)
##print(res)

##a = input()
##a = a.lower()
##res = a.count("g")+a.count("c")
##res = (res/len(a))*100
##print(res)

##s = 'abcdefghijk'
##print(s[3:6])
##print(s[:6])
##print(s[3:])
##print(s[::-1])
##print(s[-3:])
##print(s[:-6])
##print(s[-1:-10:-2])

##a = input()
##res = []
##i = 0
##var = 1
##if(len(a) == 1):
##        res.append(a)
##        res.append(str(var))
##else:
##    while(i < len(a)-1):
##    #print(a[i])
##    #print(i)
##    
##        if(i == len(a)-2): #если это уже конец
##            if(a[i] == a[i+1]):
##                res.append(a[i])
##                var += 1
##                res.append(str(var))
##                break
##            elif(a[i] != a[i+1]):
##                res.append(a[i])
##                res.append(str(var))
##                res.append(a[i+1])
##                res.append("1")
##                break
##        if(a[i] == a[i+1]):
##            var += 1
##        elif(a[i] != a[i+1]):
##            res.append(a[i])
##            res.append(str(var))
##            var = 1
##     #   print(res)
##        i += 1
##
##res = ''.join(res)
##print(res)

##a = [int(i) for i in input().split()]
##print(sum(a))

##a = [int(i) for i in input().split()]
##if(len(a)==1):
##        print(a[0])
##else:        
##        a.append(a[0]), a.insert(0, a[len(a)-2])
##        for i in range(1, len(a)-1):
##                print(a[i-1]+a[i+1], end=' ')

#00233448
##a = [str(i) for i in input().split()]
##a.sort()
##a = ''.join(a)
##i = 0
##if(len(a)==1): print(a)
##else:
##        while(i <= len(a)-1):
##
##                var = a.count(a[i])
##                if(var > 1):
##                        print(int(a[i]), end=" ")
##                        i += var
##                else:
##                        i += 1
#4 8 0 3 4 2 0 3
#1 1 2 2 3 3

##a = [int(i) for i in input().split()]
##a.sort()
##k = 0
##while(len(a) > 1):
##        if(a[0]==a[1]):
##                del a[1]
##                k=+1
##        else:
##                if(k!=0):
##                        print(a[0], end=" ")
##                        del a[0]
##                        k=0
##                else:
##                        del a[0]
##                        k=0
##if(k!=0):print(a[0])                

##a = []
##while(True):
##        b = int(input())
##        a.append(b)
##        if(sum(a)==0):
##                break       
##a = [j**2 for j in a]
##print(sum(a))        

##done = False
##while not done:
##        a = int(input())
##        b=a
##        for i in range(1, b):
##                while not done:
##                        j = 
##                        print(i, end=' ')
##                        while(j!=0):
##                                print(i, end=' ')
##                                j-=1
##                                a-=1
##                                print(a, j)
##                                if(a==0):
##                                        done = True
##                                        break
##                
                
                
#a, b, c = (int(i) for i in input().split())      
        
##a = int(input())
##if(a==0) or (a==1):print(a)
##else:
##        done = True
##        
##        i = 1
##        j = i
##        print(i, j)
##        while(done):
##                b=a
##                c=1
##                print(i, j)
##                while(j!=0):
##                        if(c<=a):
##                                print("!", i),
##                                i+=1
##                                j-=1
##                                c+=1
##                                print("остаток", i, j, c)


##a = int(input())
##if(a==0) or (a==1):print(a)
##else:
##        done = True
##        while(done):
##                b=a
##                c=1
##                for i in range(1, b+1):
##                        j = i
##                        while(j!=0):
##                                if(c<=a):
##                                        print(i, end=' '),
##                                        j-=1
##                                        c+=1


##a = [int(i) for i in input().split()]
##b = int(input())
##res = True
##for i in range(0, len(a)):
##        if(a[i]==b):
##                print(i, end=" ")
##                res = False
##if(res==True):print("Отсутствует")        

#функции

##def f(n):
##    return n * 10 + 5
##
##res = f(f(f(10)))
##print(res)

        
##def f(x):
##        if(x<=-2): return 1-(2+x)**2
##        elif(x>-2 and x<=2): return -(x/2)
##        elif(x>2): return (x-2)**2+1
                                
def modify_list(l):
        l=[i if i%2==0 else l.remove(i) for i in l ]
        #l=[(i/2) for i in l]
        for i in l:
                i = i/2
lst = [1, 2, 3, 4, 5, 6]
modify_list(lst)
print(lst)         

        

                
                        
                        
                        
