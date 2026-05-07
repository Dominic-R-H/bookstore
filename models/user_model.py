from db import get_connection

def get_user_by_email(email):
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE email = %s"
    cursor.execute(query, (email,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user


def create_user(name, phone, email, password):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        query = """
        INSERT INTO users (name, phone, email, password)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(query, (name, phone, email, password))
        conn.commit()

        return True

    except Exception:
        return False

    finally:
        cursor.close()
        conn.close()


def get_user_by_id(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        query = "SELECT * FROM users WHERE id = %s"
        cursor.execute(query, (user_id,))
        user = cursor.fetchone()
        return user 
    except Exception:
        return None
    finally:
        cursor.close()
        conn.close()
        
        
        
        