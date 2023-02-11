import numpy as np
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup
import math

print('getting')
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'}
Catagory = ['economy', 'sports' , 'culture' , 'politics']
news = pd.DataFrame(columns=['url' , 'news'] , index = range(0 ,(len(Catagory)*60*18) ))#

j=0
for cat in Catagory:
    for page in range(1, 60+1):#
        url = 'https://www.farsnews.ir/'+ str(cat)+'?p='+ str(page)
        content = requests.get(url,  headers=headers )
        soup = BeautifulSoup(content.text , 'html.parser')
        for n in range(0,len(soup.select('.align-items-start'))):
            try:
                url2 = 'https://www.farsnews.ir' + re.findall(r'href=\"(.*?)\" target' , str(soup.select('.align-items-start')[n]))[0]
                news['url'][j] = url2
                
                content2 = requests.get(url2,  headers=headers )
                soup2 = BeautifulSoup(content2.text , 'html.parser')
                try:
                    soup2.select('.rtejustify')
                    lead = str()
                    for l in range(0, len(soup2.select('.rtejustify'))):
                        a = soup2.select('.rtejustify')[l].text.strip()
                        lead = lead  + a
                    news['news'][j] = lead
                except:
                    pass
                
                
                j+=1
              
            except:
                pass
            

            
news.to_csv('news.csv' , index=False, encoding='utf-8')
print('end')