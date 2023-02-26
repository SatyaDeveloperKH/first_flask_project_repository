from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': '$1500'
  },
  {
    'id': 2,
    'title': 'Frontend Developer',
    'location': 'Phnom Penh, Cambodia',
    'salary': '$1200'
  },
  {
    'id': 3,
    'title': 'Backend Developer',
    'location': 'London, England',
    'salary': '$1700'
  },
  {
    'id': 4,
    'title': 'Project Manager',
    'location': 'Tokyo, Japan',
    'salary': '$2400'
  }
]

@app.route("/")
def hello():
  return render_template('home.html', jobs=JOBS)

@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

