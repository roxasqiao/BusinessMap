'''
Created on 2020年10月27日

@author: MR.Tree
'''
from spider import get_address  
from spider.configdata import query


if __name__ == '__main__':
    get = get_address.GetAdress()
    for item in query:
        print('--->',item['value'],item['key'])
        get.Part(item['key'],item['value'])
