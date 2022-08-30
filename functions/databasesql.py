# import pymysql
# db=pymysql.connect(host='localhost',user='root',passwd='root',db='admission')
# # prepare cursor object using cursor()method
# cur1=db.cursor()
# sql="create table sales (id int,pname varchar(20))"
# cur1.execute(sql)
# db.commit()


# insert values to that table sales
# import pymysql
# db=pymysql.connect(host='localhost',user='root',passwd='root',db='admission')
# # prepare cursor object using cursor()method
# cur1=db.cursor()
# sql="insert into sales values(111,'fridge')"
# cur1.execute(sql)
# db.commit()
# import pymysql
# db=pymysql.connect(host='localhost',user='root',passwd='root',db='admission')
# # prepare cursor object using cursor()method
# cur1=db.cursor()
# sql="update sales set id=123 where id=111"
# cur1.execute(sql)
# db.commit()

# select quary execution     fetchall(), used to fetch all the records
# import pymysql
# db=pymysql.connect(host='localhost',user='root',passwd='root',db='admission')
# # prepare cursor object using cursor()method
# cur1=db.cursor()
# sql="select * from admission"
# cur1.execute(sql)
# rows=cur1.fetchall()    #used for all rows print
# for i in rows:              #for loop using for one by one execution
#     print(i[0],i[1])
# db.commit()


# select quary fetchone()
# import pymysql
# db=pymysql.connect(host='localhost',user='root',passwd='root',db='admission')
# # prepare cursor object using cursor()method
# cur1=db.cursor()
# sql="select * from admission"
# cur1.execute(sql)
# rows=cur1.fetchone()
# print('name')
# if rows:
#     print(rows[0],rows[1])
# for i in rows:
#     print(i[0])
# db.commit()



# new table student one( work)
# import pymysql
# db=pymysql.connect(host='localhost',user='root',passwd='root',db='db1')
# # prepare cursor object using cursor()method
# cur1=db.cursor()
# sql="insert into student1 values(501,'R.jain',98,'M',111)"
# cur1.execute(sql)
# db.commit()
import pymysql
db=pymysql.connect(host='localhost',user='root',passwd='root',db='db1')
# prepare cursor object using cursor()method
# cur1=db.cursor()
# sql="insert into student1 values(983,'Sneha Aggerwal',80,'F',222)"
# cur1.execute(sql)
# db.commit()
# display all student information?
# cur1=db.cursor()
# sql="select * from student1"
# cur1.execute(sql)
# rows=cur1.fetchall()
# print('adno name average sex scode ')#used for all rows print
# for i in rows:              #for loop using for one by one execution
#     print(i[0],i[1],i[2],i[3],i[4])
# db.commit()


# # display rohan saini's information?
# cur1=db.cursor()
# sql="select * from student1 where adno=935"
# cur1.execute(sql)
# rows=cur1.fetchall()    #used for all rows print
# for i in rows:              #for loop using for one by one execution
#     print(i[0],i[1],i[2],i[3],i[4])
# db.commit()
# #

# display number of students in the table?
# cur1=db.cursor()
# sql="select count(*) from student1"
# cur1.execute(sql)
# rows=cur1.fetchall()
# print('count')#used for all rows print
# for i in rows:              #for loop using for one by one execution
#     print(i[0])
# db.commit()


#  display number of students in each sex
# cur1=db.cursor()
# sql="select sex,count(*) from student1 group by sex"
# cur1.execute(sql)
# rows=cur1.fetchall()
# print('count')#used for all rows print
# for i in rows:              #for loop using for one by one execution
#     print(i[0],i[1])
# db.commit()


# display students information in accending order using name
# cur1=db.cursor()
# sql="select * from student1 order by name asc"
# cur1.execute(sql)
# rows=cur1.fetchall()
# print('count')#used for all rows print
# for i in rows:              #for loop using for one by one execution
#     print(i[0],i[1],i[2],i[3],i[4])
# db.commit()

# display student information in descenting order using aversge?
# cur1=db.cursor()
# sql="select * from student1 order by average desc"
# cur1.execute(sql)
# rows=cur1.fetchall()
# print('count')#used for all rows print
# for i in rows:              #for loop using for one by one execution
#     print(i[0],i[1],i[2],i[3],i[4])
# db.commit()

# display student's name starting with letter k?
# cur1=db.cursor()
# sql="select name from student1 where name like 'k%'"
# cur1.execute(sql)
# rows=cur1.fetchall()
# print('names start with k')#used for all rows print
# for i in rows:              #for loop using for one by one execution
#     print(i[0])
# db.commit()


# display students information whose name ends with 'l'?
cur1=db.cursor()
sql="select * from student1 where name like '%l'"
cur1.execute(sql)
rows=cur1.fetchall()
print('names end with l')#used for all rows print
for i in rows:              #for loop using for one by one execution
    print(i[0],i[1],i[2],i[3],i[4])
db.commit()







