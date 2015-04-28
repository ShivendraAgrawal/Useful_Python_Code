
Writing on csv , one row at a time
with open('filename.csv', 'wb') as fp:
    a = csv.writer(fp, delimiter=',')
    
    for: # Your logic           
    	a.writerow([])


Running code by itself
if __name__ == '__main__':

Input
search_for=raw_input("Enter what you want the count for : ")

ssh
ssh ags7kor@kor1046739.apac.bosch.com

oracle
import cx_Oracle as c
db= c.connect("usr","pass","ip:port/orcl")
cur=db.cursor()
d=cur.execute("SELECT * FROM table_name")
