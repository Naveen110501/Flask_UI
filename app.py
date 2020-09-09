from flask import Flask,redirect,render_template,request,url_for
import sqlite3
app=Flask(__name__)
@app.route('/')
def index():
    return render_template("practice.html")

@app.route('/view',methods=["POST","GET"])
def view():
    if request.method=="POST":
        key=request.form["id"]
        try:
            conn=sqlite3.connect('C:\\Users\\HP\\Documents\\PythonWorks\\sqlite-tools-win32-x86-3330000\\manager.db')
            with conn:
                conn.row_factory=sqlite3.Row
                cur=conn.cursor()
                cur.execute('''select * from wallet where domain=? OR name=? OR weblink=?''',(key,key,key))
                rrr=cur.fetchall()
        except Exception as e:
            print("error: "+str(e))
        finally:
            return render_template( "practice.html",rows=rrr)

if __name__=="main":
    app.run(debug=True)