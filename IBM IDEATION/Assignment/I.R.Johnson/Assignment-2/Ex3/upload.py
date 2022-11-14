
from flask import *  
app = Flask(__name__)  
 
@app.route('/')  
def upload():  
    return render_template("ResumeUpload.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        f = request.files['file']  
        f.save(f.filename)  
        return render_template("success.html", name = f.filename,a=email,b=name,c=phone)  
  
if __name__ == '__main__':  
    app.run(debug = True)  
 
