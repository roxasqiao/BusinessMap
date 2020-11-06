'''
Created on 2020年10月23日

@author: MR.Tree
'''
import requests
from spider import configdata
from spider.save_data import save_data
AK=configdata.AK

class GetAdress():
    def Seach_city(self,query,region):
        '''
        #按城市搜索    
        API:http://lbsyun.baidu.com/index.php?title=webapi/place-suggestion-api
        @input:
        query:输入建议关键字
        region:区域限制
        city_limit:取值为"true"，仅返回region中指定城市检索结果 
        '''
        url='http://api.map.baidu.com/place/v2/search?query=%s&region=%s\
        &page_size=20&page_num=1&city_limit=true&output=json&ak=%s'%(query,region,AK)
        res = requests.get(url)
        print(res.status_code)
        if res.status_code==200:
            val=res.json()
            print(val)
            if val['status']==0:
                retVal=val['results']
                num = val['num']
                for item in retVal:
                    if item['uid'] !='':
                        print(retVal.index(item)+1,item['name'],item['address'],item['location']['lng'],item['location']['lat'])
            else:
                retVal=None
            return retVal
        else:
            print('无法获取%s数据'%query)
            
    def Bounds(self,query_id,query,bounds):
        '''
                矩形查询
        '''
        url='http://api.map.baidu.com/place/v2/search?query=%s&page_size=20&bounds=%s&output=json&ak=%s'%(query,bounds,AK)
        try:
            res = requests.get(url)
            list_address=[]
            if res.status_code==200:
                val=res.json()
                if val['status']==0:
                    retVal=val['results']
                    num = val['total']
                    print(num)
                    #print(retVal)
                    for item in retVal:
                        '''
                        data = retVal.index(item),item['name'],item['province'],item['city'],item['area'],item['uid'],\
                        item['address'],item['location']['lng'],item['location']['lat']
                        '''
                        rdata = item['uid']+','+query+','+item['name']+','+item['province']+','+item['city']+','+item['area']+','+\
                        item['address']+','+str(item['location']['lat'])+','+str(item['location']['lng'])+','+query_id
                        #print(rdata)
                        list_address.append(rdata)
                    return list_address
                else:
                    retVal=None
                    #print('-->无法获取数据了')
                return retVal
            else:
                print('无法获取%s数据'%query)            
        except Exception as e:
            print("异常-->"+str(e))       
            
    def Part(self,query_id,query):
        '''
        切片循环
        '''
        left_bottom = [configdata.left_bottom[1],configdata.left_bottom[0]];  # 设置区域左下角坐标（百度坐标系）
        right_top = [configdata.right_top[1],configdata.right_top[0]]; # 设置区域右上角坐标（百度坐标系）
        part_n = configdata.part_n;  
        x_item = round((right_top[0]-left_bottom[0])/part_n,6);
        y_item = round((right_top[1]-left_bottom[1])/part_n,6);
        n = 0; # 切片计数器
        for i in range(part_n):
            for j in range(part_n):
                        left_bottom_part = [left_bottom[0]+i*x_item,left_bottom[1]+j*y_item]; # 切片的左下角坐标
                        right_top_part = [left_bottom[0]+(i+1)*x_item,left_bottom[1]+(j+1)*y_item]; # 切片的右上角坐标
                        n=n+1
                        bounds=str(left_bottom_part[0])+','+\
                               str(left_bottom_part[1])+','+\
                               str(right_top_part[0])+','+\
                               str(right_top_part[1])
                        print( '第',str(n),'个切片--->',bounds)
                        get_boun = GetAdress()
                        list_address=get_boun.Bounds(query_id,query, bounds)
                        if list_address !=None and len(list_address)!=0:
                            save_data(list_address)
                        
    
    
