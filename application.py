
from flask import Flask, redirect, render_template, request, session
from flask_session import Session

# Configure app
app = Flask(__name__)

# Connect to database
db = SQL("sqlite:///store.db")

# Configure sessions
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def books():
    books = db.execute("SELECT * FROM books")
    return render_template("books.html",books=books)
    
@app.route("/cart",["POST","GET"])
def cart():
    if "cart" not in session:
        session["cart"] = []
    
    id = request.form.get("id")
    if id:
       session["cart"].append(id)
       
    books = db.execute("SELECT title FROM books WHERE id IN ?",session["cart"])
    return render_template("cart.html",books=books)
    


    
    
    
