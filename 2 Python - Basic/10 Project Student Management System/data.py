import csv


def import_database_csv(file_path):
    try:
        with open(file_path,"r",encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError as ex:
        print(f"Error: [FileNotFoundError] The file or database in path \"{file_path}\" doesn't exists\n{ex}\n")
        headers = ["Name", "Section", "Spanish", "English", "Social Studies", "Science"]
        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
        input("A new empty database file was created, hit enter to continue...")
        return []


def export_database_csv(file_path,list_param):
    with open(file_path,"w",encoding="utf-8", newline="") as file:
        headers = ["Name", "Section", "Spanish", "English", "Social Studies", "Science"]
        writer = csv.DictWriter(file,fieldnames=headers)
        writer.writeheader()
        writer.writerows(list_param)


