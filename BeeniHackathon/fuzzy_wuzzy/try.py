from flask import Flask, jsonify, request
import pandas as pd
import json

@app.route('/check/singlecandidate', methods=[ 'POST']) #change route
def save_record():
    input = request.get_json()
    input_df=pd.read_json(input)
    
    filepath = r'C:\Users\MY PC\BeeniHackathon-1\BeeniHackathon\fuzzy_wuzzy\data\recruitment_data1.csv'
    df_file=pd.read_csv(filepath)

    df_input = df_input.reindex(columns=df_file.columns)
    df_input.to_csv(filepath, mode='a', columns=header, header=False)
return jsonify({'message': 'New candidate saved successfully!'})

