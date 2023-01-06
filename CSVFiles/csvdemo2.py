import csv

# write csv files
with open("C:\\Users\\VARUN\\Desktop\\Varun_Personal\\Automation_API\\CSVFiles\\csvdata.csv",mode='a') as f2:
    csvwriter=csv.writer(f2)
    csvwriter.writerow(["Bob","Approved"])
