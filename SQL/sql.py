import sqlite3
from employees import Employee

conn = sqlite3.connect(':memory:')

c = conn.cursor()

def insert_emp(emp):
    c.execute("INSERT INTO employees VALUES(?,?,?)",(emp.first,emp.last,emp.pay,))
    

def get_emps_by_name(lastName):
   if(lastName=='all'):
     with conn:
        c.execute("SELECT * FROM employees")
   else:
     with conn:
        c.execute("SELECT * FROM employees WHERE last=?",(lastName,)) # Remember placeholder Khan has comma at the end
   return c.fetchall()


def update_pay(emp,pay):
    with conn:
        c.execute("""UPDATE employees SET pay=?
        WHERE first = ? AND last = ?""",(pay,emp.first,emp.last))

def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = ? AND last = ?",(emp.first,emp.last))


emp_1 = Employee('Tahir', 'Tareen', 15000)
emp_2 = Employee('Saleem', 'Khan', 6000)

# print(emp_1.first)
# print(emp_1.last)
# print(emp_1.pay)
c.execute("""CREATE TABLE employees (
    first text,
    last text,
    pay integer
    )""")

insert_emp(emp_1)
insert_emp(emp_2)
emps = get_emps_by_name('Khan')
print(emps)

update_pay(emp_2, 95000)
# remove_emp(emp_1)

emps = get_emps_by_name('all')
print(emps)
conn.close()  