<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for, flash, url_for,session
=======
from flask import Flask, render_template, request, redirect, url_for, flash, url_for
>>>>>>> e9666896916be3222315054f4c52795ea9a2160b

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
<<<<<<< HEAD
from flask_session import Session

=======
>>>>>>> e9666896916be3222315054f4c52795ea9a2160b

#Form Class
class Log_Reg_Form(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField('Submit')

app  = Flask(__name__)
<<<<<<< HEAD
app.config['SECRET_KEY'] = "Test-Key"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
=======
app.config['SECRET_KEY'] = "Test-Key" 
>>>>>>> e9666896916be3222315054f4c52795ea9a2160b

crrnt_Username = ''
crrnt_Password = ''

<<<<<<< HEAD
Mangolist =  ['มะมวงอกร่อง','มะม่วงมัน','มะม่วงสุก','มะม่วงแรด']

account = {'username':[],'password':[]}

update = True

=======
account = {'username':[],'password':[]}

>>>>>>> e9666896916be3222315054f4c52795ea9a2160b
@app.route('/')
def HomeCustomer():
    crrnt_Username = ''
    crrnt_Password = ''
    return render_template("HomeCustm.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    global account
    global crrnt_Username
    global crrnt_Password
<<<<<<< HEAD
    global session
=======
>>>>>>> e9666896916be3222315054f4c52795ea9a2160b
    if request.method == 'POST':
        # Create an object called "form" to use LoginForm class
        form = Log_Reg_Form()
        username = form.username.data
        password = form.password.data
        

        print(username,password)

        ##แก้ให้เอาไปเช็คในฐานข้อมูลได้ สู้ๆครับ
        Corectly = str(username) in account['username'] and str(password) == str(account['password'][account['username'].index(str(username))])
        if  Corectly:
            print(str(account['password'][account['username'].index(str(username))]))
            crrnt_Username = username
            crrnt_Password = password
<<<<<<< HEAD
            session["name"] = crrnt_Username
            return redirect(url_for('HomeSaler'))
        else:
            print('fail login')
=======
            return redirect(url_for('HomeSaler'))
        else:
>>>>>>> e9666896916be3222315054f4c52795ea9a2160b
            return redirect(url_for('login'))

    #method คือ GET
    return render_template("login.html")

@app.route('/register' ,methods=['GET', 'POST'])
def register():
    global account
    global crrnt_Username
    global crrnt_Password
    if request.method == 'POST':
        # Create an object called "form" to use LoginForm class
        form = Log_Reg_Form()
        username = form.username.data
        password = form.password.data
        Confm_password = request.form['Confirmpassword']

        print(username,password,Confm_password)

        ##แก้ให้เอาไปเช็คในฐานข้อมูลได้ สู้ๆครับเย็ดหี
        Used = str(username) in account['username']
        if not Used and password == Confm_password:
            print('next')
            account['username'].append(username)
            account['password'].append(password)
            return redirect(url_for('login'))
        else:
<<<<<<< HEAD
            print('fail regiter')
=======
>>>>>>> e9666896916be3222315054f4c52795ea9a2160b
            return redirect(url_for('register'))

    return render_template("register.html") 


@app.route('/HomeSaler')
def HomeSaler():
<<<<<<< HEAD
    global Mangolist
    global update
    global account
    global crrnt_Username
    global crrnt_Password
    global session
    if session["name"] == None:
        return redirect("/")
    
    if update:
        print(update)
        print(Mangolist[-1])
        update = False
        return render_template("HomeSaler.html", Mangolist=Mangolist ,crrnt_Username=session["name"])

    ##สมมมติเอาว่าเป็นงี้
    #Mangolist =  ['มะมวงอกร่อง','มะม่วงมัน','มะม่วงสุก','มะม่วงแรด']

    print(crrnt_Username)
    return render_template("HomeSaler.html", Mangolist=Mangolist ,crrnt_Username=session["name"])

@app.route('/Profile')
def Profile():
    
    global account
    global crrnt_Username
    global session
    if session["name"] == None:
        return redirect("/")
    return render_template("Profile.html",crrnt_Username=session["name"])

@app.route('/NewProduct' ,methods=['GET', 'POST'])
def NewProduct():
    global session
    global update
    if session["name"] == None:
        return redirect("/")
=======
    global account
    global crrnt_Username
    global crrnt_Password
    ##สมมมติเอาว่าเป็นงี้
    Mangolist =  ['มะมวงอกร่อง','มะม่วงมัน','มะม่วงสุก','มะม่วงแรด']
    print(crrnt_Username)
    return render_template("HomeSaler.html", Mangolist=Mangolist ,crrnt_Username=crrnt_Username)

@app.route('/Profile')
def Profile():
    global account
    global crrnt_Username
    global crrnt_Password
    return render_template("Profile.html",crrnt_Username=crrnt_Username)

@app.route('/NewProduct' ,methods=['GET', 'POST'])
def NewProduct():
>>>>>>> e9666896916be3222315054f4c52795ea9a2160b
    if request.method == 'POST':
        product_name = request.form['product_name']
        source_type = request.form['source_type']
        source_name = request.form['source_name']
        # ดำเนินการเก็บข้อมูลในฐานข้อมูลหรือประมวลผลต่อไป
<<<<<<< HEAD
        Mangolist.append(product_name+' By : '+session["name"])
        update = True
=======
>>>>>>> e9666896916be3222315054f4c52795ea9a2160b

        print(product_name,source_type,source_name)
        return redirect(url_for('ShowQR'))

    return render_template("NewProduct.html")

@app.route('/ScanQR',methods=['GET', 'POST'])
def ScanQR():
    if request.method == 'POST':
        code = request.form['QRmes']
        redirect(url_for(str('ShowQR/'+code)))
    return render_template("ScanQR.html")

@app.route('/ShowQR')
def ShowQR():
<<<<<<< HEAD
    global session
    if session["name"] == None:
        return redirect("/")
    return render_template("ShowQR.html")

@app.route("/logout")
def logout():
    session["name"] = None
    global crrnt_Username
    global crrnt_Password
    crrnt_Username = ''
    crrnt_Password = ''
    return redirect("/")

=======
    return render_template("ShowQR.html")

>>>>>>> e9666896916be3222315054f4c52795ea9a2160b
if __name__ == "__main__":
    app.run(debug = True)