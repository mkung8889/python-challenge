import os
import csv

csvpath = os.path.join("employee_data.csv")

with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    rows = []
    empid=[]
    name=[]
    dob=[]
    ssn=[]
    state=[]

    newheader=['Emp ID','First Name','Last Name','DOB','SSN','State']
    namesplit=[]
    dobsplit=[]
    ssnsplit=[]
    firstname=[]
    lastname=[]
    newdob=[]
    ssncensored=[]
    state_abbrev=[]

    for i, row in enumerate(csvreader):
        if i==0:
            header = i
        else:
            rows.append(row)
    
    for i in rows:
        empid.append(i[0])
        name.append(i[1])
        dob.append(i[2])
        ssn.append(i[3])
        state.append(i[4])

    for i in name:
        namesplit.append(i.split())
    for i in namesplit:
        firstname.append(i[0])
        lastname.append(i[1])
    
    for i in dob:
        dobsplit.append(i.split("-"))
    for i in dobsplit:
        year = i[0]
        month = i[1]
        day = i[2]
        newformat = month + "/" + day + "/" + year
        newdob.append(newformat)

    
    for i in ssn:
        ssnsplit.append(i.split('-'))
    for i in ssnsplit:
        censor = "***-**-"
        last4 = i[-1]
        ssncensored.append(censor+last4)
d = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

for i in state:
    for j in d:
        if i==j:
            state_abbrev.append(d[j])

new_employee_data = list(zip(empid,firstname,lastname,newdob,ssncensored,state_abbrev))
new_employee_data.insert(0,newheader)

with open('new_employee_data.csv', 'w',newline='') as csvfile:
    csvwriter = csv.writer(csvfile,delimiter=',')
    for i in new_employee_data:
        csvwriter.writerow(i)