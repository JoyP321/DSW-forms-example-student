from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/response", methods=['POST','GET'])
def render_response():
    response = ""
    if request.method == 'POST' :
        favorite_color = request.form['color']
        if favorite_color.lower() == "orange":
            response = "Orange is my favorite color too!"
        else:
            response = favorite_color + " is not my favorite color :("
    return render_template('response.html', responseFromServer = response)
    
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
