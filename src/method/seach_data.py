'''
Created on 2020年10月27日

@author: MR.Tree
'''
import pyhdb
from spider import database_info as database
def SeachData():
    conn = pyhdb.connect(host =  database.info["host"],
                                 port = database.info["port"],
                                 user = database.info["user"],
                                 password = database.info["password"])
    cursor = conn.cursor()
    seachsql = 'select * from config.ZPOI_LAT_LNT where brand_code=%s and 1=%s limit 100'
    cursor.execute(seachsql,('zt_1',1))
    sdata = cursor.fetchall()
    finalDataLis=OrgData(sdata)
    return finalDataLis
    
def FilterData(code,minLat,maxLat,minLng,maxLng):
    tcode=code.split(',')
    in_p=', '.join(list(map(lambda x: "'%s'" % x,tcode)))
     #连接数据库
    conn = pyhdb.connect(host = '172.30.80.28',
                                 port = '30041',
                                 user = "HANA_DEV",
                                 password = "Admin001")
    cursor = conn.cursor()
    sql = 'select * from config.ZPOI_LAT_LNT where brand_code in (%s) and lat between to_char(%s) and to_char(%s) and lng between to_char(%s) and to_char(%s)'\
            % (in_p,minLat,maxLat,minLng,maxLng)
    print(sql)
    cursor.execute(sql)
    sdata = cursor.fetchall()
    return OrgData(sdata)

def OrgData(sdata):
    '''
            --数据解析
    '''
    num =len(sdata)
    total = str(num)
    print("--->>查询数据"+total)
    finalDataList=[]
    for i in range(num):
        title = sdata[i][3]
        lat = sdata[i][8]
        lng = sdata[i][9]
        address=sdata[i][7]
        finalData={'title':title,'lat':lat,'lng':lng,'address':address}
        finalDataList.append(finalData)
    #print(finalDataList)
    return finalDataList
#SeachData('zt_1,zt_2')
