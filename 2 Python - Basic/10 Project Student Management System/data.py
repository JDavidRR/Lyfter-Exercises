import csv

def import_database_csv(file_path):
    with open(file_path,"r",encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)

def export_database_csv(file_path,list_param):
    with open(file_path,"w",encoding="utf-8", newline="") as file:
        headers = list_param[0].keys()
        writer = csv.DictWriter(file,fieldnames=headers)
        writer.writeheader()
        writer.writerows(list_param)

