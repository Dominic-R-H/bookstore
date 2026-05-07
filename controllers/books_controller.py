from flask import Blueprint, render_template, request, session, url_for, redirect, jsonify
import models.book_model as book_model
import models.user_model as user_model

books = Blueprint('books', __name__)

# slug to sub category names
SUBCATEGORIES = {
    "infants": "Infants",
    "junior": "Junior",
    "young": "Young",
    "classic-novels": "Classic Novels",
    "fiction": "Fiction",
    "comic": "Comic",
    "crime-and-thriller": "Crime and Thriller"
}

# have separate page for each subcategory
@books.route('/books/<slug>')
def books_page(slug):
      
    logged_in = 'user_id' in session
    
    subcategory = SUBCATEGORIES.get(slug)
    if not subcategory:
        return 404
    
    return render_template('books.html', subcategory=subcategory, logged_in=logged_in)

    
@books.route('/api/books/<slug>', methods=['GET'])
def get_books_by_subcategory(slug):

    subcategory = SUBCATEGORIES.get(slug)
    if not subcategory:
        return jsonify({"error": "Missing subcategory"}), 400
    
    logged_in = 'user_id' in session
    
    response = {"logged_in": logged_in}
    
    books = book_model.fetch_books_by_subcategory(subcategory)
    if books:
        response['books'] = books
    else:
        response['books'] = []
        
    return jsonify(response)

