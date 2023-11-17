import pymysql

# mysql에 연결하기
db=pymysql.connect(host='101.101.210.141', 
                   port=3306, 
                   user='study', 
                   passwd='study!@#$%', 
                   db='shj0318', 
                   charset='utf8')

# 커서 일단 만들고
cursor = db.cursor()

##### sql 작성하기

# # 테이블 만들기
# sql = '''
#     CREATE TABLE shj (
#         name varchar(20) NOT NULL,
#         math INT NULL,
#         english INT NULL,
#         PRIMARY KEY (name)
#     )
# '''

# # 값 넣기
# sql = '''
#     INSERT INTO shj (name, math, english)
#         VALUES('손효정', 100, 90)
# '''

# # 수정하기
# sql = '''
#     UPDATE shj
#        SET math = 95,
#            english = 80
#      WHERE name = "손효정"
# '''

# # 커서 실행하고
# cursor.execute(sql)

# # # 커밋하기 전엔 롤백 가능함
# # db.rollback()

# # 커밋해야 적용됨
# db.commit()

# # 끝나면 close해야함
# cursor.close()
# db.close()



# 조회하기
sql = '''
    SELECT *
      FROM shj
'''

# 조회는 commit 필요없음
cursor.execute(sql)
rs = cursor.fetchall()
print(rs)



