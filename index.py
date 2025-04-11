from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/class', methods=['GET', 'POST'])
def redirectt():
    if request.method == 'POST':
        print('test')
        return redirect("https://classroom.google.com/w/Njg4NjM4NTM0OTMy/t/all")
    

if __name__ == '__main__':
    app.run(debug=True)
