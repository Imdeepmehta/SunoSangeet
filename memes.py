import requests
# import lxml.html as lh
import json
import urllib

# a = requests.get('https://api.imgflip.com/get_memes')
# # print(a.text[url])
# b = json.loads(a.text)
# img_url_1 = b["data"]["memes"][0]["url"]
# data = []
# for i in b["data"]["memes"]:
#     data.append(i)

# print(da)
# # img_url = 'https://api.imgflip.com/popular_meme_ids'

# # page=requests.get(img_url)

# # doc = lh.fromstring(page.content)
# # # print(doc)

# # tr_elements = doc.xpath('//tr')
# # # print(tr_elements)


# # #Create empty list
# # col=[]
# # i=0
# # #For each row, store each first element (header) and an empty list
# # for t in tr_elements[0]:
# #     i+=1
# #     name=t.text_content()
# #     # print('%d:"%s"'%(i,name))
# #     col.append((name,[]))

# # # print(col)


# # for j in range(1,len(tr_elements)):
# #     #T is our j'th row
# #     T=tr_elements[j]
# #     #i is the index of our column
# #     i=0
    
# #     #Iterate through each element of the row
# #     for t in T.iterchildren():
# #         data=t.text_content() 
# #         #Check if row is empty
# #         if i>0:
# #         #Convert any numerical value to integers
# #             try:
# #                 data=int(data)
# #             except:
# #                 pass
# #         #Append the data to the empty list of the i'th column
# #         col[i][1].append(data)
# #         #Increment i for the next column
# #         i+=1
# # # print(type(col))
# # id,name,altName = list(col[0])[1],col[1],col[2]

# # # print(id)
# # print(len(id))

# # def  get_100_id():
# #     print("I'm function")
# #     new_id = str(id)
    
# #     return new_id

# # s=get_100_id()
# # print(s)

url = "https://api.imgflip.com/caption_image"
data ={
    'template_id': 112126428,
    'username': 'VivekAsCoder', 
    'password':"9354085897", 
    'text0':'hey1',
    'text1':'hey2',
    'text2':'hey3',
    }

a = requests.post(url, data=data).json()
im_url = a["data"]["url"]
print(a["data"]["url"])
# urllib.urlretrieve(im_url, "00000001.jpg")
f = open('00000001.jpg','wb')
f.write(requests.get(im_url).content)
f.close()