import duckdb

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


