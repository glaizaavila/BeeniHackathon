from fuzzywuzzy import fuzz
import pandas as pd
import json

filepath = r'C:\Users\MY PC\BeeniHackathon-1\BeeniHackathon\fuzzy_wuzzy\data\recruitment_data1.csv'

df_file = pd.read_csv(filepath)

header = ['applicantId','firstName', 'lastName', 'birthDate', 'email', 'phoneNumber', 'address', 'skills']

df = df_file[header]

existing_candidates = df.to_dict(orient='records')

applicantmax=df['applicantId'].max()+1

input_candidate = {'applicantId': int(applicantmax)
                    ,'firstName': 'Scott'
                   , 'lastName': 'Sheppard'
                   , 'birthDate': '8/31/1992'
                   , 'email': 'perezjanet@example.org'
                   , 'phoneNumber': '421-429-7655x39421'
                   , 'address': '597 Smith Point'
                   , 'skills': 'python, pandas'}

#0 - not considered, 1 - ratio, 2 - birthday, 3 - sort ratio, 4 - partial ratio
fuzzy_config = {'applicantId':0
                ,'firstName': 1
                , 'lastName': 1
                , 'birthDate': 2
                , 'email': 1
                , 'phoneNumber': 1
                , 'address': 1
                , 'skills': 3}

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
                elif fuzzy_config[input_key] == 3: 
                    score = fuzz.token_sort_ratio(str(value), str(input_candidate[key]))
                    total_score += score
    counter += 1
    
    average_score = total_score / (len(input_candidate) - 1)

    if average_score >= 80:   
        for key, value in candidate.items():
            for input_key in input_candidate.keys():
                if input_key == key:
                    if fuzzy_config[input_key] == 2:
                        score = fuzz.ratio(str(value), str(input_candidate[key]))
                        total_score += score
       
    if average_score >= min_treshold:   
        average_score = total_score / len(input_candidate)

        candidate.update({'Result ID':counter})
        candidate.update({'averageScore':average_score})
        result.append(candidate)
    
df_result=pd.DataFrame(result)
df_result=df_result[['applicantId','averageScore']]
merged_df = pd.merge(df_result, df_file, left_on='applicantId',right_on='applicantId', how='left')
merged_dict=merged_df.to_dict(orient='records')
print(merged_dict)