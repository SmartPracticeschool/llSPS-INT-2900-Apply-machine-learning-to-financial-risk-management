import numpy as np
from flask import Flask, request, jsonify, render_template
from joblib import load
app = Flask(__name__)
model = load('svm.save')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/risk_prediction',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    x_dum = [[int(x) for x in request.form.values()]]  
    print(x_dum)
    x_test=[[x_dum[0][8],x_dum[0][5],x_dum[0][4],x_dum[0][3],x_dum[0][0],x_dum[0][1],x_dum[0][2],x_dum[0][6],x_dum[0][7]]]
    
    print(x_test)    
    #for purpose
    if(x_test[0][0]==12): #if radio
        x_test[0][0]=0      
        x_test[0].insert(1,0)
        x_test[0].insert(2,0)
        x_test[0].insert(3,0)
        x_test[0].insert(4,1)
        x_test[0].insert(5,0)
        x_test[0].insert(6,0)
    elif(x_test[0][0]==13): # if education
        x_test[0][0]=0
        x_test[0].insert(1,0)
        x_test[0].insert(2,1)
        x_test[0].insert(3,0)
        x_test[0].insert(4,0)
        x_test[0].insert(5,0)
        x_test[0].insert(6,0)
    elif(x_test[0][0]==14):
        x_test[0][0]=0
        x_test[0].insert(1,0)
        x_test[0].insert(2,0)
        x_test[0].insert(3,1)
        x_test[0].insert(4,0)
        x_test[0].insert(5,0)
        x_test[0].insert(6,0)
    elif(x_test[0][0]==15):
        x_test[0][0]=1
        x_test[0].insert(1,0)
        x_test[0].insert(2,0)
        x_test[0].insert(3,0)
        x_test[0].insert(4,0)
        x_test[0].insert(5,0)
        x_test[0].insert(6,0)
    elif(x_test[0][0]==16):
        x_test[0][0]=0
        x_test[0].insert(1,0)
        x_test[0].insert(2,0)
        x_test[0].insert(3,0)
        x_test[0].insert(4,0)
        x_test[0].insert(5,0)
        x_test[0].insert(6,0)
    elif(x_test[0][0]==17):
        x_test[0][0]=0
        x_test[0].insert(1,1)
        x_test[0].insert(2,0)
        x_test[0].insert(3,0)
        x_test[0].insert(4,0)
        x_test[0].insert(5,0)
        x_test[0].insert(6,0)
    elif(x_test[0][0]==18):
        x_test[0][0]=0
        x_test[0].insert(1,0)
        x_test[0].insert(2,0)
        x_test[0].insert(3,0)
        x_test[0].insert(4,0)
        x_test[0].insert(5,1)
        x_test[0].insert(6,0)
    elif(x_test[0][0]==19):
        x_test[0][0]=0
        x_test[0].insert(1,0)
        x_test[0].insert(2,0)
        x_test[0].insert(3,0)
        x_test[0].insert(4,0)
        x_test[0].insert(5,0)
        x_test[0].insert(6,1)
        
    print(x_test)
    #for checking account
    if(x_test[0][7]==9):
        x_test[0][7]=0
        x_test[0].insert(8,0)

    elif(x_test[0][7]==10):
        x_test[0][7]=1
        x_test[0].insert(8,0)
    
    elif(x_test[0][7]==11):
        x_test[0][7]=0
        x_test[0].insert(8,1)
    print(x_test)     
    #for saving account
    if(x_test[0][9]==5):
        x_test[0][9]=0
        x_test[0].insert(10,0)
        x_test[0].insert(11,0)
    elif(x_test[0][9]==6):
        x_test[0][9]=1
        x_test[0].insert(10,0)
        x_test[0].insert(11,0)
    elif(x_test[0][9]==7):
        x_test[0][9]=0
        x_test[0].insert(10,1)
        x_test[0].insert(11,0)
    elif(x_test[0][9]==8):
        x_test[0][9]=0
        x_test[0].insert(10,0)
        x_test[0].insert(11,1)
    print(x_test)
    #for housing
    
    if(x_test[0][12]==2):
        x_test[0][12]=1
        x_test[0].insert(13,0)
    elif(x_test[0][12]==3):
        x_test[0][12]=0
        x_test[0].insert(13,1)
    elif(x_test[0][12]==4):
        x_test[0][12]=0
        x_test[0].insert(13,0)
    
    
        
    
    print(x_test)
    
    prediction = model.predict(x_test)
    print(prediction)
    if prediction[0]==0:
        output='Bad'
    
    elif prediction[0]==1:
        output='Good'
    
    else:
        output="Error in model"
    
    return render_template('index.html', prediction_text='Risk Level: {}'.format(output))
'''
@app.route('/predict_api',methods=['POST'])
def predict_api():
   
    For direct API calls trought request
   
    data = request.get_json(force=True)
    prediction = model.y_predict([np.array(list(data.values()))])
    output = prediction[0]
    return jsonify(output)
'''
if __name__ == "__main__":
    app.debug = True
    app.run(port=7000)