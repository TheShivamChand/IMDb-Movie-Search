
# coding: utf-8

# In[58]:


from bs4 import BeautifulSoup
import requests
movies_title=[]
movies_rating=[]
movies_cast=[]
movies_id=[]

page1=requests.get("https://www.imdb.com/list/ls006266261/?page=1&sort=user_rating,desc&st_dt=&mode=detail")
soup1=BeautifulSoup(page1.content,'html5lib')


# In[59]:


for i in range(1,12):
    page1=requests.get("https://www.imdb.com/list/ls006266261/?page="+str(i)+"&sort=user_rating,desc&st_dt=&mode=detail")
    soup1=BeautifulSoup(page1.content,'html.parser')
    f=soup1.findAll('h3',class_="lister-item-header")
    for i1 in f:
        fe=i1.find('a').get_text()
        fe1=i1.find('a')['href'].split('/')[2]
        #print(fe1)
        movies_id.append(fe1)
        movies_title.append(fe)
#print(movies_title)
#print(len(movies_title))


# In[60]:


for i in range(1,12):
    page1=requests.get("https://www.imdb.com/list/ls006266261/?page="+str(i)+"&sort=user_rating,desc&st_dt=&mode=detail")
    soup1=BeautifulSoup(page1.content,'html.parser')
    rating = soup1.select("div.lister-item-content")
    for i in rating:
        x=(i.find('span','ipl-rating-star__rating').text).split()[0]
        #print(x)
        movies_rating.append(x)


# In[72]:


movies_cast=[]
for i in range(1,12):
    page1=requests.get("https://www.imdb.com/list/ls006266261/?page="+str(i)+"&sort=user_rating,desc&st_dt=&mode=detail")
    soup1=BeautifulSoup(page1.content,'html.parser')
    cast=soup1.select("div.lister-item-content")
    for i in range(len(cast)):
        x=(cast[i].findAll('p'))
        d=x[2].text
        idx=d.find("Stars:")
        pro=d[idx+6:]
        mlist=pro.split("\n")
        mlist="".join(mlist).strip().split(',')
        org_list=[]
        for i in mlist:
            org_list.append(i.strip())
        movies_cast.append(org_list)
        #print(org_list)


# In[77]:


final = []
for i in range(1000):
    mydict = {}
    mydict['id'] = movies_id[i]
    mydict['title'] = movies_title[i]
    mydict['rating']  = movies_rating[i]
    mydict['cast'] = movies_cast[i]
    final.append(mydict)


# In[78]:


final


# In[97]:


from pymongo import MongoClient 
  
try: 
    conn = MongoClient() 
    print("Connected successfully!!!") 
except:   
    print("Could not connect to MongoDB")
db = conn.database


# In[98]:


collection=db.test
for i in final:
    collection.insert_one(i)
    print(i)


# In[100]:


cursor = collection.find() 
for record in cursor: 
    print(record) 
    print()

