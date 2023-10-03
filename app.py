from flask import Flask, render_template,jsonify
app=Flask(__name__)

jobs=[
    {
        'id':1,
        'title':'Data Scientist',
        'location':'Bengaluru, India',
        'salary':'10,00,000'
    },
    {
        'id':2,
        'title':'Data Analyst',
        'location':'Delhi, India',
        'salary':'15,00,000'
    },
    {
        'id':3,
        'title':'Front End Engeeneer',
        'location':'Bengaluru, India',
        'salary':'12,00,000'
    },
    {
        'id':4,
        'title':'Full Stack Developer',
        'location':'Remote',
        'salary':'25,00,000'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html')

@app.route('/api/jobs')
def jobs_function():
    return jsonify(jobs)

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)
