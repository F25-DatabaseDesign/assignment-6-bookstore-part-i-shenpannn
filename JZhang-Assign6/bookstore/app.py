from flask import Flask, render_template, request, redirect, url_for, make_response

# instantiate the app
app = Flask(__name__)

# Create a list called categories. The elements in the list should be lists that contain the following information in this order:
#   categoryId
#   categoryName
#   An example of a single category list is: [1, "Biographies"]

# Create a list called books. The elements in the list should be lists that contain the following information in this order:
#   bookId     (you can assign the bookId - preferably a number from 1-16)
#   categoryId (this should be one of the categories in the category dictionary)
#   title
#   author
#   isbn
#   price      (the value should be a float)
#   image      (this is the filename of the book image.  If all the images, have the same extension, you can omit the extension)
#   readNow    (This should be either 1 or 0.  For each category, some of the books (but not all) should have this set to 1.
#   An example of a single category list is: [1, 1, "Madonna", "Andrew Morton", "13-9780312287863", 39.99, "madonna.png", 1]

categories = [
    [1, "Pizza"],
    [2, "Steak"],
    [3, "Bartending"],
    [4, "Desserts"]
]

books = [
    # Pizza 
    [1, 1, "Color & Cook Pizza", "Monica Wellington", "9780486471143", 3.21, "Color & Cook Pizza.jpg", 1],
    [2, 1, "The Pizza Express Cook Book", "Peter Boizot", "9780241130773", 15.23, "The Pizza Express Cook Book.jpg", 0],
    [3, 1, "The Best Pizza Recipes in America", "Don Gwaltney", "9780963959133", 27.50, "The Best Pizza Recipes in America.jpg", 1],
    [4, 1, "Any Way You Slice It", "Nancy Krulik", "9780448432045", 18.50, "Any Way You Slice It.jpg", 0],

    # Steak 
    [5, 2, "Steak: The Whole Story", "Tim Hayward", "9781837831005", 21.20, "Steak The Whole Story.jpg", 1],
    [6, 2, "Steak & Sides", " Jamie Purviance", "9780376020338", 15.99, "Steak & Sides.jpg", 0],
    [7, 2, "The Book of Steak: Cooking for Carnivores", "Parragon Books", "9781680524116", 16.99, "The Book of Steak Cooking for Carnivores.jpg", 1],
    [8, 2, "Steaks, Chops, Roasts and Ribs", "Carl Tremblay", "9780936184784", 14.50, "Steaks, Chops, Roasts and Ribs.jpg", 0],

    # Bartending 
    [9, 3, "Bartending for Dummies", "Ray Foley", "9780470050569", 0.99, "Bartending for Dummies.jpg", 1],
    [10, 3, "Bartending 101: The Basics of Mixology", "Harvard Student Agencies Inc", "9780312349066", 0.99, "Bartending 101 The Basics of Mixology.jpg", 0],
    [11, 3, "A Beginner's Guide to Bartending", "Gilbert Chediak", "9798343440300", 10.46, "A Beginner's Guide to Bartending.jpg", 1],
    [12, 3, "Coconut Jon's Bartending Basics", "Jon Senn", "9781794761988", 1.73, "Coconut Jon's Bartending Basics.jpg", 0],

    # Desserts 
    [13, 4, "Desserts", "Caroline Bretherton", "9781465438027", 6.88, "Desserts.jpg", 1],
    [14, 4, "Bravetart: Iconic American Desserts", "Stella Parks", "9780393239867", 7.34, "Bravetart Iconic American Desserts.jpg", 0],
    [15, 4, "Sweet Enough: A Dessert Cookbook", "Alison Roman", "9781984826398", 11.37, "Sweet Enough A Dessert Cookbook.jpg", 1],
    [16, 4, "Pure Dessert", "Alice Medrich", "9781579652111", 1.39, "Pure Dessert.jpg", 0]
]

# set up routes
@app.route('/')
def home():
    # Link to the index page. Pass the categories as a parameter
    return render_template('index.html', categories=categories)

@app.route('/category')
def category():
    # Store the categoryId passed as a URL parameter into a variable
    category_id = request.args.get('categoryId', type=int)

    # If no categoryId given, go back to home
    if category_id is None:
        return redirect(url_for('home'))

    # Create a new list called selected_books containing books in that category
    selected_books = [book for book in books if book[1] == category_id]

    return render_template(
        'category.html',
        selectedCategory=category_id,
        categories=categories,
        books=selected_books
    )

@app.route('/search', methods=['POST'])
def search():
    # Get search term from the form
    term = request.form.get('search', '').strip().lower()

    matched_books = [book for book in books if term in book[2].lower()]

    return render_template(
        'category.html',
        selectedCategory=None,   
        categories=categories,
        books=matched_books
    )

@app.errorhandler(Exception)
def handle_error(e):
    """
    Output any errors - good for debugging.
    """
    return render_template('error.html', error=e) # render the edit template


if __name__ == "__main__":
    app.run(debug = True)
