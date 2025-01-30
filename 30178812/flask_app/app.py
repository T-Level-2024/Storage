from flask import Flask, render_template, request, jsonify, redirect
import requests

username = "jhon"

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Rendering index.html

@app.route('/about')
def about():
    return render_template('about.html')  # Rendering about.html

@app.route('/user/<name>')  
def user(name):
    return render_template('user.html', username=name)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello, {name}!"
    return render_template('form.html')

@app.route('/profile/<username>')  
def profile(username):
    return f"User: {username}"

@app.route('/api/data')
def get_data():
    data = {"name": "Flask", "version": "2.0"}
    return jsonify(data)  # Returns JSON response

students = [
    {"id": 1, "name": "Alice", "age": 20},
    {"id": 2, "name": "Bob", "age": 22}
]

# API Route to get all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

# API Route to get a single student by ID
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = next((s for s in students if s["id"] == student_id), None)
    return jsonify(student) if student else jsonify({"error": "Student not found"}), 404

# API Route to add a new student
@app.route('/students', methods=['POST'])
def add_student():
    new_student = request.json
    students.append(new_student)
    return jsonify(new_student), 201

# API Base URL
BASE_URL = "http://127.0.0.1:5000"

# Fetch all students
#response = requests.get(f"{BASE_URL}/students")
#print("Students List:", response.json())

# Fetch a single student by ID
student_id = 1
#response = requests.get(f"{BASE_URL}/students/{student_id}")
#print("Student Details:", response.json())

# Add a new student
new_student = {"id": 3, "name": "Charlie", "age": 23}
#response = requests.post(f"{BASE_URL}/students", json=new_student)
#print("New Student Added:", response.json())

books = [
        {"id":1, "name":"The Gathering Storm"}, 
        {"id":2, "name":"Their Finest Hour"}, 
        {"id":3, "name":"The Grand Alliance"}, 
        {"id":4, "name":"The Hinge of Fate"}, 
        {"id":5, "name":"Closing the Ring"}, 
        {"id":6, "name":"Triumph and Tragedy"}
        ]

@app.route('/books', methods=["GET"])
def get_books():
    return jsonify(books)

@app.route('/books/<int:bookid>', methods=["GET"])
def get_book(bookid):
    return jsonify(next((b for b in books if b["id"] == bookid), None)) if next((b for b in books if b["id"] == bookid), None) else jsonify({"error", "Book not found"})

@app.route('/books/new', methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        books.append({"id":books[-1]["id"]+1, "name":request.form["book"]})
        return redirect(BASE_URL+"/books", code=302)
    return render_template("book.html")

if __name__ == '__main__':
    app.run(debug=True)