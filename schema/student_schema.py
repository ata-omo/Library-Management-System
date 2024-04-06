def studentEntity(item)-> dict:
    return{
        "id" : str(item["_id"]),
        "name" : item["name"],
        "address" : item["address"],
        "age" : item["age"]
    }

def studentsEntity(entity) -> list:
    return [studentEntity(item) for item in entity]