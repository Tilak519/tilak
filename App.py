from flask import flask,render_template,request,redirect
app=flask(__name__)
@app.route('/')
def home():
    return render_template('register.html')
    @app.route('/Success',methods=['GET','POST'])
    def Success():
    if request.method='POST'
    username=request.form['username']
    email=request.form['email']
    print("usernanme:{username},Email:{email}")
    return render_template('Success.html',username=username)
    else:
    return redirect(url_for('home'))
        if __name__=='__main__':
            app.run(host='0.0.0.0')