import sqlite3

# Simulating a simple login function with a SQL injection vulnerability
def check_user_login(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Unsafe SQL query that is vulnerable to SQL injection
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)

    user = cursor.fetchone()

    if user:
        return "Login successful!"
    else:
        return "Invalid username or password"

# Example usage of the vulnerable function
username = "admin"
password = "' OR '1'='1"  # This is an example of an SQL injection attack
print(check_user_login(username, password))
