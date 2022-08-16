#importing sqlite3
import sqlite3
print('sqlite imported')
#connect to data base
conn = sqlite3.connect('student.db')
print('database successfull')
#create cursor
c = conn.cursor()
print('cursor successful')
#creating table
# c.execute("""
#           CREATE TABLE students_data(
#               first_name text,
#               last_name text,
#               email text
#             )
# """)
 #check
print('students_data table created succesfully')
#creating rows
student_list = [('Praise', 'Emmanuel', 'praise@gmail.com'),
                 ('Mariam', 'Adeoti', 'adetutumariam@gmail.com'),
                 ('Abubakar', 'Adisa', 'adisaabubakar@gmail.com'),
                 ]
#insert multiple rows into table
c.executemany('INSERT INTO students_data VALUES( ?,?,? )', student_list)
print('have inserted', c.rowcount, 'records to table students_data.')
#creating more rows
student_list = [ ('Adebisi',    'Afolabi',       'wasola.afolabi@yahoo.com'),
                 ('Adedoyin',   'Abass',         'doyinabass0@gmail.com'),
                 ('Awonaike',   'Tawakalitu',    'purpleduralumin@gmail.com'),
                 ('Babajide',   'Adesugba',      'jide_ade@hotmail.com'),
                 ('Bukola',     'Ajayi',         'bukolam.ajayi@gmail.com'),
                 ('Binta',      'Umar',          'ubinta63@yahoo.com'),
                 ('Christian',  'Uzondu',        'uzonduchristian2@gmail.com'),
                ]
#insert multiple rows into table
c.executemany('INSERT INTO students_data VALUES( ?,?,? )', student_list)
print('have inserted', c.rowcount, 'records to table students_data.')

c.execute("SELECT * FROM students_data")
#header
item = c.fetchall()
print('FIRST_NAME' + '\tLAST_NAME' + '\t\tEMAIL')
print('..........' + '\t.........' + '\t\t.....')

#looping through

for item in item:
 first_name, last_name, email = item
 print(f"{first_name:16}{last_name:16}{email:35}")

  
#1 ALTERING TO CHANGE NAME
#c.execute("ALTER TABLE students_data RENAME to students_info")
#check

print('Alter table to students_info successful')
#2 ALTERING COLUNM NAME
c.execute("ALTER TABLE students_info ADD COLUNM 'course'")
#check
print('course colunm added successfully')

#3 UPDATING STATEMENT
#c.execute(""" UPDATE students_info SET course = 'data_science' """)
#check


#c.execute("SELECT * FROM students_info")
#header
#item = c.fetchall()
#print('FIRST_NAME' + '\tLAST_NAME' + '\t\tEMAIL')
#print('..........' + '\t.........' + '\t\t.....')

#looping through

#for item in item:
print(item)
 #first_name, last_name, email = item
 #print(f"{first_name:16}{last_name:16}{email:35}")
 