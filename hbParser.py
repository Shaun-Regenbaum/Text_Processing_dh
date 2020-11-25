import json
from bs4 import BeautifulSoup
import requests
# Function to get dafim
def get_dafim(soup_obj):
    dafim_select = soup_obj.find(id='cpMstr_ddlDafim')
    dafim_options = dafim_select.find_all('option')
    temp_dafim = []
    for option in dafim_options:
        temp_dafim.append(option['value'])
    return temp_dafim


addr = "https://hebrewbooks.org/shas.aspx?mesechta=9&daf=5&format=text"

r = requests.get(addr)
print(r.status_code)
soup = BeautifulSoup(r.text, 'lxml')

for tag in soup.findAll(True):
    del tag["style"]

# a = str(soup.find(class_="shastext4")).split("\r\n")
# print(a[2])

# print(str(soup.find(class_="shastext2")).split('\r\n'))

# print(str(soup.find(class_="shastext3")).split('\r\n'))

print(str(soup.find(id="cpMstr_ddlMesechtas")).split('\r\n'))



# going through all masechtas
# for i in range(1,38):
#     masechta_data = {}

#     #getting the urls for all the dafim in the given masechta
#     urls = []
#     dafim_ids = []

#     #using the first daf to get the rest of them
#     url = (
#         "https://hebrewbooks.org/shas.aspx?mesechta=" +
#         str(i) +
#         "&daf=2&format=text"
#     )
#     r = requests.get(url)
#     soup = BeautifulSoup(r.text, 'lxml')
#     dafim = get_dafim(soup)

#     for daf in dafim:
#         urls.append(
#         "https://hebrewbooks.org/shas.aspx?mesechta=" +
#         str(i) +
#         "&daf=" +
#         str(daf) +
#         "&format=text"
#         )
#         dafim_ids.append(daf)
   
#     j = 0
#     for url in urls:
#         r = requests.get(url)
#         print(r.status_code)
#         soup = BeautifulSoup(r.text, 'lxml')
     
#         for tag in soup.findAll(True):
#             del tag["style"]

#         single_page = {
#             "mainText": str(soup.find(class_="shastext2")).split('\r\n'),
#             "rashiText": str(soup.find(class_="shastext3")).split('\r\n'),
#             "tosafotText": str(soup.find(class_="shastext4")).split('\r\n')
#         }

        
#         with open(
#             'A:\Programming\Text Processing\Text\\'+
#             str(i)+
#             '_'+
#             str(dafim_ids[j])+
#             '.txt', 'w') as outfile:
#             json.dump(single_page, outfile)

        
#         j = j + 1





    
    


