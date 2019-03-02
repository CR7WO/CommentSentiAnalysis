import requests
import time
import re
import pymysql

def readWeiboID():
    connection = pymysql.connect(host="localhost", user="root", passwd="123456", db="sentiment", port=3306,
                             charset="utf8")
    cur = connection.cursor()
    cur.execute("select * from WeiboID ")
    result=cur.fetchall()
    for i in result:
        print(i[1])
    cur.close()
    connection.close()
    return result;

if __name__ == '__main__':
    IDs=readWeiboID();
    for id in IDs:
        p=0
        while p<100:
            url = "https://m.weibo.cn/api/comments/show?id="+id+"&page="+str(p)
            html = requests.get(url)
            print(html)
            p+=1
            try:
                for c in range(len(html.json()['data']['data'])):
                    data=html.json()['data']['data'][c]['text']
                    with open('comments.txt','a',encoding='utf-8') as f:
                        comments=''.join(re.findall('[\u4e00-\u9fa5]',data))
                        print(comments)
                        f.write(comments+'\n'*2)
            except:
                None