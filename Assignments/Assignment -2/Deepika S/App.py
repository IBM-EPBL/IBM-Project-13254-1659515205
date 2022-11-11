from flask import *  
app = Flask(__name__)  
 
@app.route('/')  
def home ():  
    return render_template("index.html")  
 
 
 
@app.route('/validate', methods = ["POST"])  
def validate():  
    if request.method == 'POST':  
        return redirect(url_for("success"))  
    return redirect(url_for("login"))  
 
@app.route('/success')  
def success():  
    return "logged in successfully"  
  
if __name__ == '__main__':  
    app.run(debug = True)  