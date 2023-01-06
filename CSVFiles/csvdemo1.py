import csv

# read csv files
with open("C:\\Users\\VARUN\\Desktop\\Varun_Personal\\Automation_API\\CSVFiles\\csvdata.csv") as f1:
    csvreader = csv.reader(f1, delimiter=',')
    print(csvreader)  # <_csv.reader object at 0x0313F070>
    # print(list(csvreader)) # [['name', 'status'], ['varun', 'approved'], ['tarun', 'approved'], ['karun', 'rejected'], ['narun', 'rejected']]

    names=[]
    status=[]


    for row in csvreader:
        names.append(row[0])
        status.append(row[1])

print(names)
print(status)

# ['name', 'varun', 'tarun', 'karun', 'narun']
# ['status', 'approved', 'approved', 'rejected', 'rejected']

nameindex=names.index('varun')
print(nameindex)  # 1

loanstatus=status[nameindex]

print('Varun status is '+loanstatus) # Varun status is approved



