from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def homepage():
        return render_template("index.html",title="Home Page")
@app.route("/Admin")
def Admin():
        return render_template("Admin.html",title="LOGIN")
@app.route("/User")
def User():
        return render_template("User.html",title="LOGIN")
@app.route("/Detail")
def Detail():
        return  render_template("Detail.html",title="Detail")
@app.route("/Contact1")
def Contact1():
        return  render_template("Contact1.html",title="Contact1")
@app.route("/Contact")
def Contact():
        return  render_template("Contact.html",title="Contact")
@app.route("/Cart")
def Cart():
        return  render_template("Cart.html",title="Cart")
@app.route("/Success")
def Success():
        return  render_template("Success.html",title="Success")
@app.route("/Items")
def Items():
        return  render_template("Items.html",title="Items")
@app.route("/About")
def About():
        return  render_template("About.html",title="About")
if __name__=="__main__":
        app.run(debug=True)
