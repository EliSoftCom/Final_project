import os

ENDREC = "endrec."
RECSEP = "=>"

def update_document_id(new_id):
    with open(os.getcwd() + "\count\count.txt", "w") as fd:
        fd.write(new_id + "\n")

def retrieve_document_id():
    with open(os.getcwd() + "\count\count.txt", "r") as fd:
        return fd.readline().strip()
    


def storeDbase(db):
    "сохраняет базу данных в файл"
    with open(os.getcwd() + "\\user_db\\user_db.txt", "a") as us_db:
        key_db = list(db.keys())[0]
        print(key_db, file= us_db)
        for (name, value) in db[key_db].items():
            print(name + RECSEP + repr(value), file=us_db)
            print(ENDREC, file=us_db)
    