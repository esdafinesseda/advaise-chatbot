import sqlite3

# Connect to or create SQLite database
conn = sqlite3.connect('db/demo-co.db')
cursor = conn.cursor()

# Create the staff table
cursor.execute('''
    CREATE TABLE staff (
        name TEXT NOT NULL,
        role TEXT NOT NULL,
        experience INTEGER NOT NULL,
        contracts INTEGER NOT NULL           
    )
    '''
)

# Staff tuples
staff = [
    ('Kayla', 'project manager', 11, 1),
    ('Beneil', 'project manager', 20, 0),
    ('Meisha', 'diversity and inclusiveness researcher', 10, 0),
    ('Israel', 'diversity and inclusiveness researcher', 20, 1)   
]

# Populate the staff table
cursor.executemany('''
    INSERT INTO staff (name, role, experience, contracts) 
        VALUES (?, ?, ?, ?)
    ''', 
    staff
)

# Update db and disconnect
conn.commit()
conn.close()