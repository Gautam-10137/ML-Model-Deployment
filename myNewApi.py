from flask import Flask,request,jsonify
import joblib 
import pandas as pd

# Create FLASK App
app=Flask(__name__)

# Connect Post API call  --> predict() function    
@app.route('/predict',methods=['POST'])             # http://localhost:5000/predict
def predict():

    # GET json Request
    feat_data=request.json
    # Convert JSON to PANDAS DF( col names)
    df= pd.DataFrame(feat_data)
    df= df.reindex(columns=col_names)
    # Predict
    prediction=list(model.predict(df))
    
    return jsonify({'prediction':str(prediction)})

# Load  my MODEL and LOAD Column NAMES  when .py file runs
if __name__ =='__main__':
    model=joblib.load('final_model.pkl')
    col_names=joblib.load('col_names.pkl')
    app.run(debug=True)

