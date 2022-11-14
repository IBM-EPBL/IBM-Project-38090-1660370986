from flask import Flask,render_template, request 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Ex1.html')
@app.route('/login', methods =["POST"])
def login():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        
        return render_template ("Ex1.html",x=name,y=email,z=phone)
    
    
if __name__==('__main__'):
    app.run(debug = True)

