__author__ = 'shivendra'
import csv,timing,string
from collections import OrderedDict,Counter,defaultdict
from pprint import pprint
from datetime import datetime

#Takes csv filename and return the data in it.
def csvReader_coll(filename):
    columns = defaultdict(list)
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            for (k,v) in row.items():
                columns[k].append(v)
    notes=list(columns['Notes'])
    return notes


#Takes a text like 'AA', 'BW', 'ck' and returns the column number. (Numbering starts with 1)
def columnNumber(input_str):
    input_str=input_str.lower()
    total=0
    for i,j in enumerate(input_str):
        length=len(input_str[i+1:])
        total+=(string.lowercase.index(j)+1)*(26**length)
    return total

#Function to call columnNumbers with list of values. (Numbering starts with 0 in this case)
def call_columnNumbers():
    list_names=['b','v','aa','k','w']
    new_list=[]
    for i in list_names:
        new_list.append(columnNumber(i)-1)
    print new_list

#Takes csv filename and return the data in it.
def csvReader(filename):
    bccfile = open(filename,'rb')
    mail_sheet = csv.reader(bccfile,delimiter =',')
    raw_data = list(mail_sheet)
    return raw_data

#Takes a data in list form and the filename and writes the data to a 'csv' file
def csvWriter(List,filename):
    try:
        with open(filename+'.csv','wb') as File:
            writer = csv.writer(File,delimiter = ',')
            writer.writerows(List)
    except IOError:
        print "The file is open. Overwrite not possible. Another file is being created."
        with open(filename+'(1).csv','wb') as File:
            writer = csv.writer(File,delimiter = ',')
            writer.writerows(List)

#take list of lists as input (with first internal list as list of headers) and returns basic counts of unique values
def uniqueValues(data,show=20):
    data_dict_temp=OrderedDict()
    data_dict={}
    header=data[0]
    print "***** HEADERS *****\n"
    print header,"\n\n"
    data=data[1:]
    length=len(data)
    length=(length*(float(show)/100))

    for i,value in enumerate(header):
        data_dict_temp[i]=[]
    for row in data:
        for j,value in enumerate(row):
            data_dict_temp[j].append(value)
    for key in data_dict_temp:
        k=header[key]
        data_dict[k]={}
        data_dict[k]['value']=Counter(data_dict_temp[key])
        data_dict[k]['length']=len(Counter(data_dict_temp[key]))
    data_dict_temp={}

    print "/                FIELDS WITH                 /\n\n\n"
    print "=========================Less Unique Values================================\n\n"
    for key in data_dict:
        if data_dict[key]['length']<length:
            print key
            pprint(data_dict[key])
            print

    print "\n\n===========================Many Unique Values===============================\n\n"
    for key in data_dict:
        if data_dict[key]['length']>=length:
            print key
            pprint(data_dict[key])
            print
    # pprint(dict(data_dict))
def call_uniqueValues(filename,required_columns,flag=False):
    data=csvReader(filename)
    print "Number of rows = ",len(data)-1,"\n\n"
    # uniqueValues(data)
    filterd_data=[]

    if flag:
        for row in data:
            new_row=[]
            for j,element in enumerate(row):
                if j in required_columns:
                    new_row.append(element)

            filterd_data.append(new_row)
        data=filterd_data

    uniqueValues(data)

def find_same_rows(filename,required_columns,flag=False):
    data=csvReader(filename)
    print "Number of rows = ",len(data)-1,"\n\n"
    # uniqueValues(data)
    filterd_data=[]
    groups={}

    if flag:
        for row in data:
            new_row=[]
            for j,element in enumerate(row):
                if j in required_columns:
                    new_row.append(element)

            filterd_data.append(new_row)
        data=filterd_data

    count=0
    for row in data[1:]:
        found=False
        for i in groups:
            if groups[i][0]==row[1:]:
                groups[i].append(row[0])
                found=True
                break
        if found==False:
            groups[count]=[row[1:],row[0]]
            count+=1

    count=0
    for key in groups:
        if len(groups[key][1:])>2:
            count+=1
            print key
            print groups[key][0]
            print groups[key][1:],"\n"
    print "\nCount of groups = ",count

    count=0
    for key in groups:
        count+=len(groups[key][1:])
    print "\nTotal = ",count

if __name__ == '__main__':
    filename="C:\Users\\ags7kor\Desktop\Helpdesk_Closed_SqlDB.csv"
    req_col=[41]
    call_uniqueValues(filename,req_col,True)
