#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Function to print n natural no's using while loop

def nat(x):
    counter = 1
    while counter <= x:
        print(counter, end=" ")
        counter = counter +1
    return
nat(20)


# In[2]:


# Function to print n natural no's

def nat(x):
    for counter in range(1, x+1):
        print(counter, end=" ")
    return
nat(10)


# In[3]:


# Function to Identify the greatest of 3 numbers

def grt(x,y,z):
    if x>y and x>z:
        print(x, "is big number")
    elif y>z:
        print(y, "is big number")
    else:
        print(z, "is big number")
grt(-1,0,-3)


# In[4]:


# Function to count the digits in a number

def dig(x):
    x=int(input("enter a number"))
    return len(str(x))

dig("x")


# In[5]:


#leap year
def leap(s):
    if s%400==0 or (s%100!=0 and s%4==0):
        return True
    else:
        return False
leap(1947)


# In[13]:


#print using function print num div by6 
#and not a factor of 100 in given range
def printnum(a,b):
    for i in range(a,b):
        if i%6==0 and 100%i!=0:
            print(i,"is divi by 6")
        else:
            print("not")
printnum(90,120)





# In[17]:


#cubes avg of even no
def avgn(a,b):
    d=0
    sum=0
    for i in range(a,b):
        if i%2==0:
            c=i**3
            d=d+1
            sum=sum+c
    avg=sum/d
    print(avg)
avgn(2,5)
    
            


# In[26]:


#calculate factorial of given no
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        print(fact)  
factorial(5)


# In[31]:


#function to generate list of factors for given no
#12-->1,2,3,4,6,12
n=int(input("Enter num: "))
def fact(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
            #print("factors",i)
    return count
fact(n)


# In[41]:


#if number is prime
def prim(n):
    def fact(a):
        count=0
        for i in range(1,a+1):
            if n%i==0:
                count=count+1
        return count
    x=fact(n)
    if x == 2:
        return "Prime"
    else:
        return "NotPrime"
        
prim(19)            


# In[57]:


#prime
def prime(n):
    flag=True
    for i in range(2,n//2+1):
        if n%i==0:
            flag=False
            return flag
    return flag
prime(4)
        
        


# In[10]:


#prime
def prime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count=count+1
            print(i)
        
    if count>2:
        print("not prime")
    else:
        print("prime")
prime(23)
    


# In[13]:


#sum prime
def prime(n,n1):
    count=0
    sums=0
    for j in range(n,n1+1):
        for i in range(1,j+1):
            if j%i==0:
                count=count+1
                #sums=sums+i
    #print(sums)    
    if count>2:
        print("not prime")
    else:
        print(j)
        print("prime")
prime(2,22)
    


# In[27]:


#print alternate values from range
#[500,550]
#(500,550)
def alternate(a,b):
    z=[]
    for i in range(a,b+1,2):
        print(i)
alternate(500,550)
def alternate(a,b):
    z=[]
    for i in range(a,b,2):
        print(i)
alternate(500,550)


# In[ ]:





# In[ ]:





# In[34]:


#print the reverseof range 
def revrange(a,b):
    for i in range(b,a,-1):
        print(i)
revrange(1,10)


# In[35]:


#pritn odd no reverse in range
def oddrever(a,b):
    for i in range(b,a,-1):
        if i%2!=0:
            print(i)
oddrever(1,10)
            
            
            
            
            
            


# In[37]:


#pritn sun of range
def sumrange(a,b):
    sums=0
    for i in range(a,b):
        sums=sums+i
    return sums
sumrange(1,4)
    
    


# In[42]:


#print avg of range
def sumrange(a,b):
    sums=0
    avg=0
    c=0
    for i in range(a,b+1):
        sums=sums+i
        c=c+1
    return sums//c
sumrange(1,5)
  


# In[47]:


#amstrong no
def amstrong(n):
    n=str(n)
    s=0
    for i in n:
        i=int(i)
        s=s+i**3
    if s==int(n):
        return True
    else:
        return False
amstrong(371)


# In[54]:


#odd amstrong nos
def oddamstrng(a,b):
    for i in range(a,b):
        if amstrong(i)==True and i%2!=0:
            print(i)
oddamstrng(100,377)


# In[63]:


# avg of factorial
def avgfact(a,b):
    fact=1
    sums=0
    c=0
    for i in range(a,b+1):
        fact=fact*i
        c=c+1
        sums=sums+fact
        print(fact)
    return sums/c
avgfact(1,5)


# In[57]:


#print tables in range
def tablerange(a,b,n):
    for i in range(a,b+1):
        print(n,"*",a,"=",n*i)
tablerange(100,102,10)


# In[78]:


#print leap year in range
def leapyear(a,b):
    for i in range(a,b):
        if (i%400==0) or (i%4==0 and i%100!=0):
            print(i)
leapyear(1919,2018)


# In[81]:


#calaulate days in given time period
def dayscount(a,b):
    daysleap=0
    daysnotleap=0
    for i in range(a,b+1):
        if i%400==0 or (i%4==0 and i%100!=0):
            daysleap=daysleap+366
            print(i,"the days count is 366 ")
        else:
            daysnotleap=daysnotleap+365
            print(i,"the days is 365")
    print("no of days leap years totoal is",daysleap)
    print("no of days not leap years totoal is",daysnotleap)
    
dayscount(2018,2019)


# In[85]:


#perfect no
def perfect(n):
    sums=0
    a=str(n)
    for i in a:
        b=int(i)
        sums=sums+b
    if sums==int(n):
        print("it is perfect no")
    else:
        print("not perfect no")
perfect(10)


# In[101]:


#function to calculate number of hours for given period 
#(11,1975,3,1999)
def hourscount(m1,y1,m2,y2):
    daysleap=0
    daysnotleap=0
    h=0
    h1=0
    for i in range(y1,y2+1):
        if i%400==0 or (i%4==0 and i%100!=0):
            daysleap=daysleap+366
            h=daysleap*24
            print(h)
            print(i,"the days count is 366 ")
        else:
            daysnotleap=daysnotleap+365
            h1=daysnotleap*24
            print(h1)
            print(i,"the days is 365")
   # print("total leap year hrs",totalh)
   # print("total notleap year hrs",totalh1)
hourscount(3,2019,3,2019)
            


# In[ ]:




