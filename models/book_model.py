from db import get_connection

def fetch_books_by_subcategory(subcategory):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        query = """
        SELECT id, title, price, image
        FROM books
        WHERE subcategory = %s
        """
        cursor.execute(query, (subcategory,))
        books = cursor.fetchall()
        return books

    except Exception:
        return None

    finally:
        cursor.close()
        conn.close()

def get_book_by_id(book_id):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        query = """
        SELECT id, title, price, image
        FROM books
        WHERE id = %s
        """
        cursor.execute(query, (book_id,))
        book = cursor.fetchone()
        return book

    except Exception:
        return None

    finally:
        cursor.close()
        conn.close()

