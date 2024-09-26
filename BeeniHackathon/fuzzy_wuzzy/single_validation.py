from flask import Flask, jsonify, request
from fuzzywuzzy import fuzz
import pandas as pd
import json

app = Flask(__name__)

@app.route('/candidate/check', methods=[ 'POST'])
def check_one():
    input_candidate = request.get_json()

    filepath = './data/recruitment_data1.csv' #change filepath
    #filepath = r'C:/Users/Beeline User/Documents/GLAIZA/repositories/BeeniHackathon/BeeniHackathon/fuzzy_wuzzy/data/recruitment_data1.csv' #change filepath
    df_file = pd.read_csv(rf'{filepath}', index_col = False)
    test = df_file.fillna('')

    #header = ['applicantId','firstName', 'lastName', 'birthDate', 'email', 'phoneNumber', 'address', 'skills']
    header = ['applicantId','applicationDate','firstName', 'lastName',
              'gender', 'birthDate', 'phoneNumber', 'email', 'address',
              'educationLevel', 'yearsOfExperience', 'jobTitle', 'status',
              'supplierName', 'customerName', 'skills']

    df = df_file[header]

    existing_candidates = df.to_dict(orient='records')

    applicantmax=df['applicantId'].max()+1

    # input_candidate = {'firstName': request_candidate["firstName"]
    #                  , 'lastName': request_candidate["lastName"]
    #                  , 'birthDate': request_candidate["birthDate"]
    #                  , 'email': request_candidate["email"]
    #                  , 'phoneNumber': request_candidate["phoneNumber"]
    #                  , 'address': request_candidate["address"]
    #                  , 'skills': request_candidate["skills"]}

    #0 - not considered, 1 - ratio, 2 - birthday, 3 - sort ratio, 4 - Wratio
    fuzzy_config = {'applicantId':0
                    ,'firstName': 1
                    , 'lastName': 1
                    , 'birthDate': 2
                    , 'email': 1
                    , 'phoneNumber': 1
                    , 'address': 4
                    , 'jobTitle': 0
                    , 'skills': 3
                    , 'gender': 0
                    , 'educationLevel': 0
                    , 'yearsOfExperience': 0
                    , 'supplierName': 0
                    , 'customerName': 0
                    , 'applicationDate': 0
                    , 'status': 0}

    min_treshold = 70
    result = []

    counter = 0
    for candidate in existing_candidates:
        total_score = 0
        for key, value in candidate.items():
            for input_key in input_candidate.keys():
                if input_key == key:                
                    if fuzzy_config[input_key] == 1: 
                        score = fuzz.ratio(str(value), str(input_candidate[key]))
                        total_score += score
                    elif fuzzy_config[input_key] == 3: 
                        score = fuzz.token_sort_ratio(str(value), str(input_candidate[key]))
                        total_score += score
                    elif fuzzy_config[input_key] == 4: 
                        score = fuzz.WRatio(str(value), str(input_candidate[key]))
                        total_score += score

        average_score = total_score / (len(input_candidate) - 8)

        if average_score >= 80:   
            for key, value in candidate.items():
                for input_key in input_candidate.keys():
                    if input_key == key:
                        if fuzzy_config[input_key] == 2:
                            score = fuzz.ratio(str(value), str(input_candidate[key]))
                            total_score += score
            average_score = total_score / (len(input_candidate) - 7)
        if average_score >= min_treshold: 
            counter += 1
            candidate.update({'Result ID':counter})
            candidate.update({'averageScore':average_score})
            result.append(candidate)
            df_result=pd.DataFrame(result)
            test2 = df_result.fillna('')
            #df_result=df_result[['applicantId','averageScore']]
            #merged_df = pd.merge(test2, test, left_on='applicantId',right_on='applicantId', how='left')
            merged_dict=test2.to_dict(orient='records')
            
    if counter==0:
        input_candidate_json = json.dumps(input_candidate)
        input_candidate_pd = json.loads(input_candidate_json)
        df_input = pd.DataFrame(input_candidate_pd, index=[0])
        df_input['applicantId']=df_file['applicantId'].max()+1
        df_input = df_input.reindex(columns=df_file.columns)
        df_input.to_csv(filepath, mode='a', columns=header, header=False, index=False)
        merged_dict={}
    
    return merged_dict
    #return merged_dict.to_json(orient='records')

# for saving data    
@app.route('/candidate/submit', methods=[ 'POST']) #change route
def save_record():
    input = request.get_json()
    df_input=pd.read_json(input)
    filepath = './data/recruitment_data1.csv' #change filepath
    df_file=pd.read_csv(filepath)
    df_input['applicantId']=df_file['applicantId'].max()+1
    df_input = df_input.reindex(columns=df_file.columns)
    df_input.to_csv(filepath, mode='a', columns=header, header=False)
    return jsonify({'message': 'New candidate saved successfully!'})

@app.route('/candidate/listview') #change route
def read_all_record(): #if we want a table of all candidates
    #filepath = r'D:/npax/BeeniHackathon/BeeniHackathon/fuzzy_wuzzy/data/recruitment_data1.csv' #change filepath
    filepath = './data/recruitment_data1.csv' #change filepath
    df_file=pd.read_csv(filepath)
    print(df_file)
    
    dict_file=df_file.to_dict(orient='records')
    print(type(dict_file))
    
    json_file=df_file.to_json(orient='records')
    print(type(json_file))
    return json_file