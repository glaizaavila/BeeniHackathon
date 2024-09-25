import { mande } from "mande";
import type { CandidateRequest, CandidateResponse } from "@/interfaces/candidate.ts";

const api = mande(`${import.meta.env.BASE_URL}api`)


export const getDuplicates = async (candidate: CandidateRequest) => {
    await api.post('/candidate/check', candidate).then((list: any) => {
        return list;
    })
        .catch((error: any) => {
            console.log(error);
            throw error;
        })
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
    await api.get('/candidate/view').then((list: any) => {
        return list;
    })
        .catch((error: any) => {
            console.log(error);
            throw error;
        })
}
