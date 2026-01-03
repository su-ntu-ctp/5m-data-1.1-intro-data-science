import duckdb
import os

if os.path.exists("test_duck.db"):
    print('There is already a file created. Exiting program.')
    print('To repeat the process delete the file test_duck.db')
    exit(0)


con = duckdb.connect("test_duck.db")

# CREATE SCHEMA
con.execute("CREATE SCHEMA lesson")

# CREATE TABLE
con.execute("""
    CREATE TABLE lesson.users (
        id INTEGER,
        name VARCHAR,
        email VARCHAR
    )
""")

# INSERT single row
con.execute("""
    INSERT INTO lesson.users (id, name, email)
    VALUES (1, 'John Doe', 'john.doe@gmail.com')
""")

# INSERT multiple rows
con.execute("""
    INSERT INTO lesson.users (id, name, email)
    VALUES (2, 'Jane Doe', 'jane.doe@gmail.com'),
           (3, 'John Smith', 'john.smith@gmail.com')
""")

# Close connection when done
con.close()

print("Database and table created successfully with sample data.")
print("Please use DBeaver or DBGate to check for 3 records.")


