def ex1_8_7():
        x = int(input())
        hours = x//60
        min = x/60 - hours 
        min *= 60
        print(hours)
        print(round(min))

def ex1_8_8: #to count min of sleep
        x = int(input())
        h = int(input())
        m = int(input())

        start = (h*60 + m)
        finish = start + x
        hours = finish //60
        min = (finish/60-hours)*60
        print(hours)
        print(round(min))

def ex1_9_7:
        x = 5
        y = 10
        print(y > x * x or y >= 2 * x and x < y)


def ex1_10_5: # to check is amount of sleep is ok
        a = int(input())
        b = int(input())
        h = int(input())
        if (h > b):
            print ('Too much')
        elif h >= a:
            print('It is ok')
        elif (h < a):
            print('Too little')    
    

def ex1_10_6: #to check if year is leap
        y = int(input())
        if ((y%100 == 0) and (y%400 == 0)):
            print('Leap year')
        elif ((y%4)==0 and (not(y%100 == 0) and not(y%400 == 0))):
            print('Leap year')
        else:
            print('Not leap year')

def ex1_12_1: #Heron's formula
        import math
        x = int(input())
        y = int(input())
        z = int(input())
        pp = (x+y+z)/2
        s = math.sqrt(pp*(pp-x)*(pp-y)*(pp-z))
        print(s)


def ex1_12_2: #to check if input fits intervals (−15,12]∪(14,17)∪[19,+∞)(−15,12]∪(14,17)∪[19,+∞)
        x = int(input())
        if((x > -15 and x <= 12) or (x > 14 and x < 17) or (x >= 19)):
            print('True')
        else:
            print('False')
#####
def ex1_12_3: #calculator
        x = float(input())
        y = float(input())
        z = input()
        if z == '+':
            print(x + y)
        elif z == '-':
            print(x-y)
        elif z == '*':
            print(x*y)
        elif z == '/':
            if y == 0:
                print('Division on 0!')
            else:    
                print(x/y)
        elif z == 'mod':
            if y == 0:
                print('Division on 0!')
            else:
                print(x%y)
        elif z == 'pow':
            print(x**y)    
        elif z == 'div':
            if y == 0:
                print('Division on 0!')
            else:
                print(x//y)
#example of input:
#               5.0
#               0
#               mod
#####

def ex1_12_4: #to get square of figure
        import math
        n = input()

        if n == 'triangle':
            a = float(input())
            b = float(input())
            c = float(input())
            pp = (a+b+c)/2
            s = math.sqrt(pp*(pp-a)*(pp-b)*(pp-c))
            print(s)
        elif n == 'rectangle':
            a = float(input())
            b = float(input())
            print(a*b)

        if n == 'circle':
            r = float(input())
            print(r**2*3.14)

#sample
#input:
#            rectangle
#            4
#            10
####

def ex1_12_5:  #to print max, median and then min number out of input      
        a = int(input())
        b = int(input())
        c = int(input())
        if (a>=b) and (a>=c):
            print(a)
            (print(b), print(c)) if b<=c else (print(c), print(b))
        elif (b>=a) and (b>=c):
            print(b)
            (print(a), print(c)) if a<=c else (print(c), print(a))
        elif (c>=b) and (c>=a):
            print(c)
            (print(b), print(a)) if b<=a else (print(a), print(b))

    
def ex1_12_6: #to get the right ending of a word "programmist"
              #depending of what kind of sing. or plural the word is (russian issue)
        while True:
            b = "programmist"
            a = int(input())
            if a%100 in [11,12,13,14]:
                print(a, b+"ov") 
            elif(a%10==1):
                print(a, b)       
            elif a%10 in [2, 3, 4]:
                print(a, b+"a")
            elif a%10 in [0,5,6,7,8,9]:    
                print(a, b+"ov")
            elif (a=="break"):
                break    


def ex1_12_7: #to check if a ticket "happy" or "general" (russian cultural issue)
        while True:
            a = input()
            b = int(a[0])+int(a[1])+int(a[2])
            c = int(a[3])+int(a[4])+int(a[5])
            print("Happy") if c == b else print("General")
            if (a=="b"): break

def ex2_1_9: #to check how many * will pe printed
        i = 0
        while i < 5:
            print('*')
            if i % 2 == 0:
                print('**')
            if i > 2:
                print('***')
            i = i + 1
def ex2_1_1: #to count all input before 0
        b = 0
        while True:
            a = int(input())
            b = b + a
            if (a == 0):
                print(b)
                break

def ex2_1_12: #to find GCD
        a = int(input())
        b = int(input())
        x = 0
        y = 0

        if(a>b):
            x = a
            y = b
        else:
            x = b
            y = a
        c = 0
        while True:
            c = x%y
            x = y
            y = c
            if(c == 0):
                break
        print(int((a*b)/x))

def ex2_2_4: #to print all input numbers if
             #they are more than 10. if number is more than 100 stop program
             #and print   
        while True:
            a = int(input())
            if(a<10):
                continue
            elif(a>100):
                break
            else:
                print(a)
def ex2_3_3: #to print table of multiplication for
             # all numbers of [a;b] on all number of [c;d][c;d]

        a = int(input())
        b = int(input())
        c = int(input())
        d = int(input())
        lst = list(range(c, d+1))
        k=0
        print('\t', end='')
        while(k<len(lst)):
            if(k==lst[-1]):
                print(lst[k], '\n')
            print(lst[k], end=' ')
            k+=1
          
        for j in range(a, b+1):
              print('\n', j, end=" ")
              i=0
              while(i<len(lst)):
                  if(i==lst[-1]):
                      print(j*lst[i])
                  print(j*lst[i], end=' ')
                  i+=1

#sample
#input:
##                 7
##                 10
##                 5
##                 6
#output:
##                5	6
##        7	35	42
##        8	40	48
##        9	45	54
##        10	50	60                  
####

def ex2_3_7: #to print median of all numbers of [a, b]                  
        a = int(input())
        b = int(input())
        lst = []
        for i in range(a, b+1):
            if(i%3==0):
                lst.append(i)
        print(lst)        
        res = sum(lst)/len(lst)
        print(res)

def ex2_4_3: #to print percentage of guanin(g) and cytosine(c)
        a = input()
        a = a.lower()
        res = a.count("g")+a.count("c")
        res = (res/len(a))*100
        print(res)
def ex2_4_5: #cool example of how strings work
        s = 'abcdefghijk'
        print(s[3:6])
        print(s[:6])
        print(s[3:])
        print(s[::-1])
        print(s[-3:])
        print(s[:-6])
        print(s[-1:-10:-2])

def ex2_4_7: #to cut a long story short: aaaabbcaa -> a4b2c1a2
        a = input()
        res = []
        i = 0
        var = 1
        if(len(a) == 1):
                res.append(a)
                res.append(str(var))
        else:
            while(i < len(a)-1):    
                if(i == len(a)-2): #if it is the end
                    if(a[i] == a[i+1]):
                        res.append(a[i])
                        var += 1
                        res.append(str(var))
                        break
                    elif(a[i] != a[i+1]):
                        res.append(a[i])
                        res.append(str(var))
                        res.append(a[i+1])
                        res.append("1")
                        break
                if(a[i] == a[i+1]):
                    var += 1
                elif(a[i] != a[i+1]):
                    res.append(a[i])
                    res.append(str(var))
                    var = 1
             #   print(res)
                i += 1

        res = ''.join(res)
        print(res)

def ex2_5_9: #to test .split() function
        a = [int(i) for i in input().split()]
        print(sum(a))

def ex2_5_10: #to print sum of neighbors for all elements
        a = [int(i) for i in input().split()]
        if(len(a)==1):
                print(a[0])
        else:        
                a.append(a[0]), a.insert(0, a[len(a)-2])
                for i in range(1, len(a)-1):
                        print(a[i-1]+a[i+1], end=' ')

#sample
#input:
##                      1 3 5 6 10
#output:
##                      13 6 9 15 7
####

def ex2_5_11:                        
        a = [int(i) for i in input().split()]
        a.sort()
        k = 0
        while(len(a) > 1):
                if(a[0]==a[1]):
                        del a[1]
                        k=+1
                else:
                        if(k!=0):
                                print(a[0], end=" ")
                                del a[0]
                                k=0
                        else:
                                del a[0]
                                k=0
        if(k!=0):print(a[0])                

a = []
while(True):
        b = int(input())
        a.append(b)
        if(sum(a)==0):
                break       
a = [j**2 for j in a]
print(sum(a))        

done = False
while not done:
        a = int(input())
        b=a
        for i in range(1, b):
                while not done:
                        j = 
                        print(i, end=' ')
                        while(j!=0):
                                print(i, end=' ')
                                j-=1
                                a-=1
                                print(a, j)
                                if(a==0):
                                        done = True
                                        break
                
                
                
a, b, c = (int(i) for i in input().split())      
        
a = int(input())
if(a==0) or (a==1):print(a)
else:
        done = True
        
        i = 1
        j = i
        print(i, j)
        while(done):
                b=a
                c=1
                print(i, j)
                while(j!=0):
                        if(c<=a):
                                print("!", i),
                                i+=1
                                j-=1
                                c+=1
                                print("reminder", i, j, c)


a = int(input())
if(a==0) or (a==1):print(a)
else:
        done = True
        while(done):
                b=a
                c=1
                for i in range(1, b+1):
                        j = i
                        while(j!=0):
                                if(c<=a):
                                        print(i, end=' '),
                                        j-=1
                                        c+=1


a = [int(i) for i in input().split()]
b = int(input())
res = True
for i in range(0, len(a)):
        if(a[i]==b):
                print(i, end=" ")
                res = False
if(res==True):print("not here")        



def f(n):
    return n * 10 + 5

res = f(f(f(10)))
print(res)

        
def f(x):
        if(x<=-2): return 1-(2+x)**2
        elif(x>-2 and x<=2): return -(x/2)
        elif(x>2): return (x-2)**2+1
                                
def modify_list(l):
        [i if l.count(i)==1 else l.remove(i) for i in l]
        print('repeted elem are deleted', l)
        [i if i%2==0 else l.remove(i) for i in l]        
        print(l)
##        for j in range(0, len(l)):
##                l[j] = int(l[j]/2)
                
lst = [3, 1]
modify_list(lst)
print(lst)         

        
def modify_list1(l):
        ll = []
        [i if l.count(i)==1 else l.remove(i) for i in l]
        for i in l:
                if(i%2==0):
                        ll.append(i/2)
                        l.remove(i)
                else:l.remove(i)
        for i in range(0, len(ll)):
                 l.append(ll[i])

lst = [3, 1]
modify_list1(lst)
print('2nd', lst)         



def update_dictionary(d, a, b):
        if a in d: append()

a = input().lower().split()
s = set(a)
for i in s:
        print(i, a.count(i))

import re
with open('file.txt','r') as inf, open('abc.txt', 'w') as out:
        a = inf.readline()
        a = re.split('(\d+)',a)
        for i in a:
                count = i
                if count.isdigit():
                        count = int(count)
                        while(count>0):
                                out.write(letter)
                                count = count -1
                                #print(count, end=' ')
                else:
                        letter = i

with open('file.txt','r') as inf, open('abc.txt', 'w') as out:
        a = ''
        for line in inf: a += line.strip()
        a = a.lower().split()
        s = set(a)
        l = []
        for i in s:
                l.append(a.count(i))
        m = max(l)
        idx = 0
        index = []
        for i in l:
                if i==m: index.append(idx)
                idx += 1
        print(l, index)
        themax = ''
        for q in index:
                if list(s)[q] > themax:
                        themax = list(s)[q]
                        
        print(themax, m)
        res = str(themax) + " " + str(m)
        out.write(res)
                

        

a = input().lower().split()
s = set(a)
for i in s:
        print(i, a.count(i))


with open('file.txt','r') as inf, open('abc.txt', 'w') as out:
        median = [0, 0, 0]
        amount_of_students = 0
        for line in inf:
                amount_of_students += 1
                a = line.strip().split(";")
                a=[int(x) for x in a if x.isdigit()]
                median = list(map(lambda x, y:x+y, median, a))
                #print(sum(a)/len(a))
                out.write(str(sum(a)/len(a))+'\n')
                
        for i in median:
                a = str(i/amount_of_students)
                print(i/amount_of_students)
                out.write(a + ' ')
                
        
                
import math
r = float(input())
print(2*math.pi*r)                
                
                
import sys

for i in range(1,len(sys.argv)):
    print (sys.argv[i])

import requests
with open('file.txt','r') as inf:
        param = inf.readline().strip()
        txt = requests.get(param).text
        lines = 0
        print(txt.count("\n"))

import requests

with open('file.txt','r') as inf:
        param = inf.readline().strip()
        url = requests.get(param).text
        print("первый файл" + url)
        idx = 0
        while not "We" in url:
              idx += 1
              print(idx, end=' ')
              url.strip()
              url = 'https://stepic.org/media/attachments/course67/3.6.3/' + str(url)
              print(url)
              url = requests.get(url).text
              
        print(url)      

games = {}
score = {}
games["score"] = score

n = int(input()) 
for x in range(1, n+1):
        line = input().split(';')
        for i in range(0, len(line) , 2):
                if line[i] in games:
                        games[line[i]].append(line[i+1])
                else:
                        games[line[i]] = [line[i+1]]
                        score[line[i]] = [0, 0, 0, 0, 0]
        
        if(line[1]<line[3]):
                score[line[0]][3] +=1
                score[line[2]][1] +=1
        elif(line[1]>line[3]):
                score[line[0]][1] +=1
                score[line[2]][3] +=1
        else:
                score[line[0]][2] +=1
                score[line[2]][2] +=1
        #print(score)

for y in score:
        score[y][0] = len(games[y])

for l in score:        
        team = score[l]
        team[4] = team[1]*3 + team[2]*1
for res in score:
        print(res, end=":")
        for resres in score[res]:
                print(resres, end=" ")
        print(end="\n")
                
bookA = {}
bookB = {}
encrypted = []
decrypted = []
a = list(input())
b = list(input())
c = list(input())
d = list(input())
for i in range(0,len(a)):
        bookA[a[i]]=b[i]
for l in range(0,len(b)):
        bookB[b[l]]=a[l]        
for j in c:
        #print(bookA[j], end=' ')
        encrypted.append(bookA[j])
for k in d:
        #print(bookB[k], end=' ')
        decrypted.append(bookB[k])
        
print(''.join(encrypted))
print(''.join(decrypted))
        
        


                
        



        
        
        
                
        
        
                
        
