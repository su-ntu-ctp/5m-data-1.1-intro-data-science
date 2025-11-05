# Connect DuckDB Using Dbeaver

To open a DuckDB database in DBeaver, perform the following steps: 

1. Launch DBeaver and Create a New Connection:
    - Open DBeaver.
    - Click the "New Database Connection" button, or navigate to Database > New Database Connection in the menu bar.
2. Select DuckDB:
    - In the "Connect to a database" wizard, search for "DuckDB".
    - Select "DuckDB" from the list and click "Next".
3. Specify Database File Path:
    - In the "Connection Settings" window, locate the "Path" field.
    - Enter the full path to your DuckDB database file (e.g., C:\Users\YourUser\Documents\my_database.duckdb) or click the "Browse" button to navigate to and select the file.
4. Test and Finish Connection:
    - Optionally, click "Test Connection" to verify the connection.
    - Click "Finish" to create the connection.
5. Connect to the Database:
    - In the "Database Navigator" panel (usually on the left), locate your newly created DuckDB connection.
    - Double-click the connection to establish a connection to the database. A green tick icon will appear next to the connection name, indicating a successful connection.

You can now expand the connection in the Database Navigator to browse schemas, tables, and views within your DuckDB database and execute SQL queries.