import sqlite3

def setup_database():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        name TEXT,
        subject TEXT,
        grade INTEGER
    )
    ''')
    
    cursor.execute('DELETE FROM students')
    
    students_data = [
        ('Alice', 'Math', 85),
        ('Alice', 'Science', 78),
        ('Bob', 'Math', 92),
        ('Bob', 'Science', 88),
        ('Charlie', 'Math', 76),
        ('Charlie', 'Science', 82)
    ]
    
    cursor.executemany('INSERT INTO students VALUES (?, ?, ?)', students_data)
    conn.commit()
    conn.close()

def execute_query(sql):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.close()
        return results, None
    except Exception as e:
        conn.close()
        return None, str(e) 