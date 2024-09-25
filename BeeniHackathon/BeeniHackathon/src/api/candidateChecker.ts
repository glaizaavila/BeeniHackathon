import { mande } from "mande";
import type { CandidateRequest, CandidateResponse } from "@/interfaces/candidate.ts";

const api = mande(`${import.meta.env.BASE_URL}api`)


export const getDuplicates = async (candidate: CandidateRequest) => {
    const list = await api.post('/candidate/check', candidate).then((list: any) => {
        return <Array<CandidateResponse>>list
    })
    .catch((error: any) => {
        console.log(error);
        throw error;
    })
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