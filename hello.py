from flask import Flask ,render_template,url_for ,request

app = Flask(__name__)

@app.route('/')
def home():
    return "<h2>Hello ,communities</h2>"

@app.route("/",methods =["GET"])
def welcome():
    return 'Welcome to my flask app by Dipayan Bhowal'

@app.route("/index",methods=["GET"])
def index():
    return render_template("index.html")

# varibale rule   
@app.route('/sucess/<int:score>')
def sucess(score):
    return" The person has passed and the score is:"+ str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return" The person has failed and the score is:"+ str(score)

@app.route('/calculate',methods =["GET","POST"])
def form():
    if request.method == "GET":
        return render_template("calculate.html")
    else:
        maths = float(request.form['maths'])
        science = float(request.form['science'])
        history = float(request.form['history'])

        average_marks = (maths + science + history)/3
        result = ""
        if average_marks < 50:
            result = "sucess"
        else:
            result = "fail"


        return render_template("results.html",result = average_marks)




if __name__ == "__main__":
    app.run(debug=True)