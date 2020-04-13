import csv


# first example using reader/writer 
# with open("names.csv","r") as csv_file:
#     csv_content= csv.reader(csv_file)
#     with open("onlynames.csv","w") as csv_file2:
#         csv_content2= csv.writer(csv_file2,delimiter=";")
#         for line in csv_content:
#          csv_content2.writerow(line)

# second exemple using dictreader/dictwriter

with open("names.csv","r") as csv_file:
    csv_content= csv.DictReader(csv_file)
    with open("onlynames.csv","w") as csv_file2:
        fieldnames=["first_name","last_name"]
        csv_content2= csv.DictWriter(csv_file2,fieldnames=fieldnames,delimiter=";")
        for line in csv_content:
            
            # csv_content2.writerow({"first_name":line["first_name"],"last_name":line["last_name"]},)
        #  or we can 
            del line["email"]
            csv_content2.writerow(line)


