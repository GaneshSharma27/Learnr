from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Landing Page

@app.route('/courses')
def courses():
    courses_data = [
        {"name": "Machine Learning", "learners": "384,624", "image": "images/ml.jpg"},
        {"name": "Python", "learners": "720,604", "image": "images/python.jpg"},
        {"name": "MERN Stack", "learners": "384,624", "image": "images/mern.jpg"},
        {"name": "UX Design", "learners": "500,654", "image": "images/ux.jpg"},
        {"name": "Java", "learners": "512,789", "image": "images/java.jpg"},
        {"name": "Power BI", "learners": "412,358", "image": "images/powerbi.jpg"},
        {"name": "Tableau", "learners": "305,124", "image": "images/tableau.jpg"},
        {"name": "Cooking", "learners": "672,593", "image": "images/cooking.jpg"},
        {"name": "Music", "learners": "150,024", "image": "images/music.jpg"}
    ]
    return render_template("courses.html", courses=courses_data)

@app.route('/courses/python')
def python():
    instructors = [
        {"name": "Jesse Lyu", "avatar": "/static/images/jesse.png"},
        {"name": "Harris Ali", "avatar": "/static/images/harris.png"},
        {"name": "Andrew Nyu", "avatar": "/static/images/andrew.png"},
        {"name": "Paul Graham", "avatar": "/static/images/paul.png"},
        {"name": "Jessica Li", "avatar": "/static/images/jessica.png"},
    ]
    instructor_names = ", ".join([i["name"] for i in instructors]) + "..."

    course_structure = [
        {"title": "Introduction", "description": "Python Tutorial Fundamentals"},
        {"title": "Introduction", "description": "Learn Python - FreeCodeCamp"},
        {"title": "Introduction", "description": "Python Fundamental One Shot"},
        {"title": "Variables & Data Types", "description": "Video"},
        # Add more as needed
    ]

    return render_template("python.html", instructors=instructors,
                           instructor_names=instructor_names,
                           course_structure=course_structure)

@app.route('/courses/python/video')
def course_video():
    return render_template("video.html")

if __name__ == '__main__':
    app.run(debug=True)
