from db import get_connection

def create_order(name, email, phone, title, price):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        query = """
        INSERT INTO orders (name, email, phone, title, price)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(query, (name, email, phone, title, price))
        conn.commit()


        return cursor.lastrowid

    except Exception as e:
        print(e)
        return None

    finally:
        cursor.close()
        conn.close()
        
        
def get_order_by_id(order_id):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        query = """
        SELECT order_id, name, email, phone, title, price
        FROM orders
        WHERE order_id = %s
        """
        cursor.execute(query, (order_id,))
        order = cursor.fetchone()
        return order

    except Exception:
        return None

    finally:
        cursor.close()
        conn.close()
    
def get_orders():
    conn = get_connection()
    cursor = conn.cursor()

    try:
        query = """
        SELECT order_id, name, email, phone, title, price
        FROM orders
        """
        cursor.execute(query)
        order = cursor.fetchall()
        return order

    except Exception:
        return None

    finally:
        cursor.close()
        conn.close()    