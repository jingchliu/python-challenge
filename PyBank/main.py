import os 
import csv
count=0
total=0
change=0
total_change=0

pyBank_path='budget_data.csv'
with open(pyBank_path,newline='',encoding="UTF-8") as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')
    csv_header=next(csv_reader)
    value = []
    month = []
    diff = []
    for row in csv_reader:
        month.append(row[0])
        value.append(int(row[1]))

    for element in value:
        total += element
        count = len(value)
    
    for i in range(len(value)-1):
        change = value[i+1] - value[i]
        diff.append(change)

    for element in diff:
        total_change += element
    average_change = total_change/(len(diff))

    inc_index=diff.index(max(diff))
    dec_index=diff.index(min(diff))
    inc_change = diff[inc_index]
    dec_change = diff[dec_index]
    inc_month = month[inc_index+1]
    dec_month = month[dec_index+1]


    print("Financial Analysis"),
    print("------------------------------------------------------------"),
    print(f"Total Months: {count}"),
    print(f"Total: ${total}"),
    print(f"Average Change: ${average_change}"),
    print(f"Greatest Increase in Profits: {inc_month} (${inc_change})"),
    print(f"Greatest Decrease in Profits: {dec_month} (${dec_change})")


f=open("pyBank Result.txt","w",encoding="UTF-8") 
print("Financial Analysis",file=f)
print("------------------------------------------------------------",file=f),
print(f"Total Months: {count}",file=f),
print(f"Total: ${total}",file=f),
print(f"Average Change: ${average_change}",file=f),
print(f"Greatest Increase in Profits: {inc_month} (${inc_change})",file=f),
print(f"Greatest Decrease in Profits: {dec_month} (${dec_change})",file=f)
f.close()

        
        
        
        
        

