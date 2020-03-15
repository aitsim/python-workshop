import csv
# test1
# f = open('port.csv',"r")
# print(f)  #object and mode ...
# for l in f:
#     print(l)


#test2
# total = 0
# with open('port.csv','r') as f:
#     headers = next(f) #skip the line pof the input
#     for l in f:
#         l = l.strip()
#         parts = l.split(",")
#         parts[0] = parts[0].strip('"')
#         parts[1] = int(parts[1])
#         parts[2] = float(parts[2])
#         total += parts[1]*parts[2]
#         print(parts)
#
#
# print('total cost :{:.3f}'.format(total))

#test3
#it clean the data even it contains date
# transform to array and clean
with open('port.csv','r') as f:
    rows = csv.reader(f)
    headers= next(rows)
    for row in rows:
        row[1] = int(row[1])
        row[2] = float(row[2])
        print(row)
