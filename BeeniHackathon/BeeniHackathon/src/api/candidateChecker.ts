import { mande } from "mande";
import type { CandidateRequest, CandidateResponse } from "@/interfaces/candidate.ts";

const api = mande(`${import.meta.env.BASE_URL}api`)


export const getDuplicates = async (candidate: CandidateRequest) => {
    const a = {
        /*
        "firstName": "Scott",
        "lastName": "Sheppard",
        "birthDate": "8/31/1992",
        "email": "perezjanet@example.org",
        "phoneNumber": "421-429-7655x39421",
        "address": "597 Smith Point",
        "jobTitle": "Chief Tecology Officer",
        "skills": "python, sql, power bi, .NET, C#, azure",
        "gender": "Male",
        "educationLevel": "High School",
        "yearsOfExperience": "8",
        "supplierName": "Amasarte",
        "customerName": "EG Corp."
        */
        "firstName": "amirasadsdasd",
        "lastName": "Sheppard",
        "birthDate": "8/31/1992",
        "email": "perezjanet@example.org",
        "phoneNumber": "421-429-7655x39421",
        "address": "597 Smith Point",
        "jobTitle": "Chief Tecology Officer",
        "skills": "python, pandas",
        "gender": "",
        "educationLevel": "",
        "yearsOfExperience": "",
        "supplierName": "",
        "customerName": ""
        
    }


    const list = await api.post('/candidate/check', candidate).then((list: any) => {
        return <Array<CandidateResponse>>list
    })
        /*, {
        responseAs: 'response'
    }).then(async (response: Response) => {
        console.log(response.json);
        //return await response.json
        return response.json().then(response => ({ response }));
    })*/
        .catch((error: any) => {
            console.log(error);
            throw error;
        })
    console.log(list);
    return list;
}


export const submitCandidate = async (candidate: CandidateRequest) => {
    await api.post('/candidate/submit', candidate).then(() => {
        return true;
    })
        .catch((error: any) => {
            console.log(error);
            throw error;
        })
}


export const viewCandidates = async () => {
    const list = await api.get('/candidate/listview').then((list: any) => {
        return <Array<CandidateResponse>>list
    })
        .catch((error: any) => {
            console.log(error);
            throw error;
        })
    return list;
}