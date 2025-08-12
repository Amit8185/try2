import sqlite3

def sql_injection(user_input):
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    # Vulnerable: directly embedding user input in query
    query = "SELECT * FROM users WHERE name = '%s'" % user_input
    c.execute(query)
    return c.fetchall()
