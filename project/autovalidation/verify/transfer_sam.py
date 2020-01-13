import json
import pymysql


# 提前分析涉及的所有功能及搭配
def main():
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='123456', port=3306, db='cdnw', charset='utf8')
    cur = conn.cursor()
    sql = 'select sam from `oui`'
    cur.execute(sql)
    sam_list = cur.fetchall()
    conn.commit()
    conn.close()
    for sam in sam_list:
        #sam_dict = json.loads(sam[0])
        sam_dict = eval(sam[0])  # 将str转换成dict
        for rule in sam_dict:
            print(type(rule))
            print(rule)
            # data = json.loads(rule)
            # print(type(data))
            # print(data)
            for item in rule:
                if "actionid" in item:
                    print(item['actionid'])
                if "conditionid" in item:
                    print(item['conditionid'])


if __name__ == '__main__':
    main()