from flask import Flask
from flask import request
from fuzzywuzzy import fuzz
import pandas as pd
import json

app = Flask(__name__)

@app.route('/check/singlecandidate', methods=[ 'POST'])
def check_one():
    request_candidate = request.get_json()

    filepath = 'D:/npax/BeeniHackathon/BeeniHackathon/fuzzy_wuzzy/data/recruitment_data1.csv'
    df = pd.read_csv(rf'{filepath}')

    header = ['First Name', 'Last Name', 'Date of Birth', 'Email', 'Phone Number', 'Address', 'Job Title', 'Skillset']
    df = df[header]

    #df['Date of Birth'] = pd.to_datetime(['Date of Birth'], format='%m/%d/%Y')

    existing_candidates = df.to_dict(orient='records')

    input_candidate = {'First Name': request_candidate["firstname"]
                    , 'Last Name': request_candidate["lastname"]
                    , 'Date of Birth': request_candidate["birthdate"]
                    , 'Email': request_candidate["email"]
                    , 'Phone Number': request_candidate["phonenumber"]
                    , 'Address': request_candidate["address"]
                    , 'Job Title': request_candidate["jobtitle"]
                    , 'Skillset': request_candidate["skillset"]}

    fuzzy_config = {'First Name': 1
                    , 'Last Name': 1
                    , 'Date of Birth': 0
                    , 'Email': 1
                    , 'Phone Number': 1
                    , 'Address': 1
                    , 'Job Title': 1
                    , 'Skillset': 1}

    min_treshold = 50
    result = []

    for candidate in existing_candidates:
        total_score = 0
        counter = 0

        for key, value in candidate.items():
            for input_key in input_candidate.keys():
                if input_key == key:
                    # print(f'existing candidate: {key}, {value}')
                    # print(f'input candidate: {input_key}, {input_candidate[input_key]}')
                    
                    if fuzzy_config[input_key] == 0:
                        if value == input_candidate[key]:
                            score = 100
                        else: 
                            score = 0
                    elif fuzzy_config[input_key] == 1: 
                        score = fuzz.ratio(str(value), str(input_candidate[key]))
                    else:
                        score = fuzz.ratio(str(value), str(input_candidate[key]))
                    total_score += score
                    counter += 1
        
        average_score = total_score / len(input_candidate)

        if average_score >= min_treshold:      
            candidate.update({'Result ID':counter})
            candidate.update({'Average Score':average_score})
            result.append(candidate)
        
    json_result = json.dumps(result, indent=2)
    print(json_result)

    return json_result
    

