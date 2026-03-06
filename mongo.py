from pymongo import MongoClient

# 1. Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# 2. Create / Use Database
db = client["College"]

# 3. Create / Use Collection
students = db["students"]

# CREATE
students.insert_one({
    "name": "Ishika",
    "branch":"CSE",
    "year": "2"
})
print("CREATE: Data inserted")

# READ
print("\nREAD: Student Records")
for student in students.find({}, {"_id": 0}):
    print(student)

# UPDATE
students.update_one(
    {"name": "Ishika"},
    {"$set": {"year": 3}}
)
print("\nUPDATE: Data updated")

# READ AFTER UPDATE
print("\nREAD AFTER UPDATE:")
for student in students.find({}, {"_id": 0}):
    print(student)

# DELETE
students.delete_one({"name": "Ishika"})
print("\nDELETE: Data deleted")

# FINAL READ
print("\nFINAL DATA:")
for student in students.find({}, {"_id": 0}):
    print(student)
