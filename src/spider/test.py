'''
Created on 2020年11月4日

@author: MR.Tree
'''
from spider import configdata
from spider.configdata import query

for item in query:
    
    print(item['key'],item['value'])
