from database import Database
from school import School


db = Database()
db.connect()


db.execute('''
CREATE TABLE IF NOT EXISTS schools (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    location TEXT
)
''')

print("Testing basic insert and find_all:")

school1 = School(name='Flatiron School', location='New York')
school1.save(db)

school2 = School(name='General Assembly', location='San Francisco')
school2.save(db)


schools = School.find_all(db)
for school in schools:
    print(f"School: {school.name}, Location: {school.location}")

print("\nTesting update functionality:")

school1.location = 'Brooklyn'
school1.save(db)

schools = School.find_all(db)
for school in schools:
    print(f"Updated School: {school.name}, Location: {school.location}")

print("\nTesting with empty database (after deleting records):")

db.execute("DELETE FROM schools")

schools = School.find_all(db)
print(f"Number of schools after deletion: {len(schools)}")

print("\nTesting edge case: saving with missing required field (name)")
try:
    school3 = School(location='Chicago')  
    school3.save(db)
except Exception as e:
    print(f"Error as expected: {e}")

print("\nTesting database connection handling:")

db.close()
try:
    school4 = School(name='Test School', location='Test Location')
    school4.save(db)
except Exception as e:
    print(f"Error after closing DB: {e}")

print("All tests completed.")
