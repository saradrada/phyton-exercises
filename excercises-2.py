#!/usr/bin/env python
# coding: utf-8

# # str

# In[2]:


help (str)


# In[5]:


s = "aaa,bbb,ccccc,dd"
str.split(s, ',')


# In[14]:


"%s, eggs and %s"%('spam', "SPAM")


# In[13]:


"{}, eggs and {}".format('spam', "SPAM")


# # list

# In[15]:


help (list)


# In[19]:


lista = [1,4,5,"hello",7]
lista.append(21)
print(lista)


# In[24]:


lista = [10,2,4,1]
lista.sort()
print(lista)


# In[26]:


lista = [1,4,5,"hello",7]
lista.remove(4)
print(lista)


# # dict

# In[27]:


services = {'ftp':21, 'ssh':22,'smtp':25,'http':80}
print(services.keys())


# In[36]:


print(services.items())


# In[35]:


print(services['ftp'])


# In[34]:


type(services)


# In[38]:


services['lista']=(1,2,3,4)
print(services)


# In[40]:


var = 4
a = str(var)
type(a)


# # Methods

# In[43]:


def append_element(some_list, element):
    return some_list.append(element)

list = [1,23,4]
append_element(list,5)
print(list)


# In[49]:


def k():
    a=1
    b=2
    c=7
    return a,b,c
e,f,g = k()
print(g)


# In[50]:


result = 0
for i in range(100):
    result += i

print(result)


# In[52]:


animals = ["dog","cat","mouse"]
for i in animals:
    print(i,end="/")
print("\n")
for i in animals:
    print(i)


# In[54]:


131/0


# In[60]:


try:
    print("[+] 1337/0 =" + str(1337/0))
except:
    print("[-]Error.")


# In[58]:


try:
    print("[+] 1337/0 =" + str(1337/0))
except Exception as e:
    print("[-]Error: " + str(e))


# In[62]:


print(input("Escriba su nombre: "))

