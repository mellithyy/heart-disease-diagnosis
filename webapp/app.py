from flask import Flask,render_template, request
import joblib
import numpy as np

app=Flask(__name__)

model= joblib.load('model/model.h5')

@app.route('/',methods= ['GET'])
def index():
    return render_template('index.html')


@app.route('/predict',methods= ['GET'])
def predict():
    all_data= request.args

    age_category    = int(all_data["age_category"])
    diabetic        = int(all_data["diabetic"])
    diff_walking    = int(all_data["diff_walking"])
    physical_health = int(all_data["physical_health"])
    stroke          = int(all_data["stroke"])
    smoking         = int(all_data["smoking"])
    kidney_disease  = int(all_data["kidney_disease"])
    skin_cancer     = int(all_data["skin_cancer"])
    gen_health      = int(all_data["gen_health"])


    data = [age_category, diff_walking, physical_health, diabetic, stroke, smoking, kidney_disease, skin_cancer, gen_health]

    prediction = model.predict(np.array(data).reshape(1,-1))[0]

    if prediction == 1:
        output = "(Positive) - You probably have a Heart Disease!"
    
    else:
        output = "(Negative) - Your Heart is Healthy!"

    return render_template('prediction.html', output= output)

### Running the App
if __name__=='__main__':
    app.run()