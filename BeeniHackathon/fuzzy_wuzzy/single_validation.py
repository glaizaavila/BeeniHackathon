from flask import Flask, jsonify, request
from fuzzywuzzy import fuzz
import pandas as pd
import json

app = Flask(__name__)

@app.route('/check/singlecandidate', methods=[ 'POST'])
def check_one():
    request_candidate = request.get_json()

    filepath = './data/recruitment_data1.csv'
    df_file = pd.read_csv(rf'{filepath}')

    header = ['Applicant ID','First Name', 'Last Name', 'Date of Birth', 'Email', 'Phone Number', 'Address', 'Skillset']
    df = df_file[header]

    existing_candidates = df.to_dict(orient='records')

    input_candidate = {'First Name': request_candidate["firstname"]
                    , 'Last Name': request_candidate["lastname"]
                    , 'Date of Birth': request_candidate["birthdate"]
                    , 'Email': request_candidate["email"]
                    , 'Phone Number': request_candidate["phonenumber"]
                    , 'Address': request_candidate["address"]
                    , 'Skillset': request_candidate["skillset"]}

    fuzzy_config = {'ApplicantID':3
                    ,'First Name': 1
                    , 'Last Name': 1
                    , 'Date of Birth': 0
                    , 'Email': 1
                    , 'Phone Number': 1
                    , 'Address': 1
                    , 'Skillset': 2}

    min_treshold = 70
    result = []

    for candidate in existing_candidates:
        total_score = 0
        counter = 0
        for key, value in candidate.items():
            for input_key in input_candidate.keys():
                if input_key == key:
                    if fuzzy_config[input_key] == 1: 
                        score = fuzz.ratio(str(value), str(input_candidate[key]))
                        total_score += score
                    elif fuzzy_config[input_key] == 2: 
                        score = fuzz.token_sort_ratio(str(value), str(input_candidate[key]))
                        total_score += score
        counter += 1
        average_score = total_score / (len(input_candidate) - 1)

        if average_score >= 80:   
            for key, value in candidate.items():
                for input_key in input_candidate.keys():
                    if input_key == key:
                        if fuzzy_config[input_key] == 0:
                            score = fuzz.ratio(str(value), str(input_candidate[key]))
                            total_score += score
       
        if average_score >= min_treshold:   
            average_score = total_score / len(input_candidate)
            candidate.update({'Result ID':counter})
            candidate.update({'Average Score':average_score})
            result.append(candidate)
    json_result = json.dumps(result, indent=2)
    return json_result

# for saving data    
#@app.route('/check/singlecandidate', methods=[ 'POST']) #change route
def save_record():
    input = request.get_json()
    df_input=pd.read_json(input)
    filepath = r'C:\Users\MY PC\BeeniHackathon-1\BeeniHackathon\fuzzy_wuzzy\data\recruitment_data1.csv' #change filepath
    df_file=pd.read_csv(filepath)
    df_input['applicantId']=df_file['applicantId'].max()+1

    df_input = df_input.reindex(columns=df_file.columns)

    df_input.to_csv(filepath, mode='a', columns=header, header=False)
    return jsonify({'message': 'New candidate saved successfully!'})

#@app.route('/check/singlecandidate', methods=[ 'POST']) #change route
def read_all_record(): #if we want a table of all candidates
    filepath = r'C:\Users\MY PC\BeeniHackathon-1\BeeniHackathon\fuzzy_wuzzy\data\recruitment_data1.csv' #change filepath
    df_file=pd.read_csv(filepath)
    return jsonify(df_file)