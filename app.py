from flask import Flask,render_template,request
import joblib,re

app = Flask(__name__)


bow_job = joblib.load('./models/countvectorizer.lb')
model =  joblib.load('./models/multinomialnaivebayes.lb')

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/predict', methods=["GET","POST"])
def predict():
    if request.method == "POST":
        email = request.form.get('email', '')
        email = email.lower()
        email = re.sub(r'[^a-zA-Z ]', '', email)

        email_transformed = bow_job.transform([email])
        predict = model.predict(email_transformed)[0]

        labels = {'1': "SPAM", '0': "HAM"}
        output = labels.get(str(predict))


        return render_template("show.html", prediction = output)
    
   


if __name__ == '__main__':
    app.run(debug=True)