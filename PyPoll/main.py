import os 
import csv
from collections import Counter
candidate=[]
percentage = []
winner=""

pyPoll_path='election_data.csv'
with open(pyPoll_path,newline='',encoding="UTF-8") as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')
    csv_header=next(csv_reader)
    for row in csv_reader:
        candidate.append(row[2])
    total=len(candidate)
    list_set=set(candidate)
    name_list=list(list_set)
    result=Counter(candidate)
    result_key = list(result.keys())
    result_value = list(result.values())
    for i in result_value:
        i = i / total * 100
        percentage.append(i)
    percentage=['%.3f' % elem for elem in percentage]
    
    max_percent=max(percentage)
    for i in range(len(percentage)):
        if max_percent==percentage[i]:
            winner=result_key[i]

    print("Election Results"),
    print("----------------------------------"),
    print(f"Total Votes: {total}"),
    print("----------------------------------"),
    print(f"{result_key[0]}: {percentage[0]}% ({result[result_key[0]]})"),
    print(f"{result_key[1]}: {percentage[1]}% ({result[result_key[1]]})"),
    print(f"{result_key[2]}: {percentage[2]}% ({result[result_key[2]]})"),
    print(f"{result_key[3]}: {percentage[3]}% ({result[result_key[3]]})"),
    print("-----------------------------------"),
    print(f"Winner: {winner}"),
    print("-----------------------------------")


f=open("pyPoll Result.txt","w",encoding="UTF-8") 
print("Election Results",file=f),
print("----------------------------------------",file=f),
print(f"Total Votes: {total}",file=f),
print(f"{result_key[0]}: {percentage[0]}% ({result[result_key[0]]})",file=f),
print(f"{result_key[1]}: {percentage[1]}% ({result[result_key[1]]})",file=f),
print(f"{result_key[2]}: {percentage[2]}% ({result[result_key[2]]})",file=f),
print(f"{result_key[3]}c: {percentage[3]}% ({result[result_key[3]]})",file=f),
print("-----------------------------------------",file=f),
print(f"Winner: {winner}",file=f),
print("-----------------------------------------",file=f),
f.close()