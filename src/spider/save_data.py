'''
Created on 2020年10月27日

@author: MR.Tree
'''
import pyhdb
from spider import database_info as database
# 将excel数据写入hana 门店信息
def save_data(list_address):
    #连接数据库
    conn = pyhdb.connect(host =  database.info["host"],
                                 port = database.info["port"],
                                 user = database.info["user"],
                                 password = database.info["password"])
    cursor = conn.cursor()
    #print("连接到HANA!")
    
    sql = 'insert into CONFIG.ZPOI_LAT_LNT(UID,BRAND_CODE,BRAND,NAME,PROVINCE,CITY,AREA,ADDRESS,LAT,LNG,UPDAT)\
           values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,CURRENT_TIMESTAMP)'
    sql2 = 'delete from CONFIG.ZPOI_LAT_LNT where UID=%s and 1=%s'
    try:
        i = len(list_address)
        for num in range(i):
            co1 = list_address[num].split(',')[0]
            co2 = list_address[num].split(',')[1]
            co3 = list_address[num].split(',')[2]
            co4 = list_address[num].split(',')[3]
            co5 = list_address[num].split(',')[4]
            co6 = list_address[num].split(',')[5]
            co7 = list_address[num].split(',')[6]
            co8 = list_address[num].split(',')[7]
            co9 = list_address[num].split(',')[8]
            co10 = list_address[num].split(',')[9]
            par=(co1,co10,co2,co3,co4,co5,co6,co7,co8,co9)
            par_d=co1,'1'
            print(par,par_d)
            cursor.execute(sql2,par_d)
            cursor.execute(sql,par)
        conn.commit()
        print( '----sql执行成功----')
    except Exception as e:
        print("----sql异常-->"+str(e))
        conn.rollback()
        conn.commit()
