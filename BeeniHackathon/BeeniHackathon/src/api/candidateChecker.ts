import { mande } from "mande";

const api = mande(`${import.meta.env.BASE_URL}api`)

console.log("E1 " + import.meta.env.BASE_URL);

export const testGet = async () =>
{
    const a = {
        "firstname": "amirasadsdasd",
        "lastname": "Sheppard",
        "birthdate": "8/31/1992",
        "email": "perezjanet@example.org",
        "phonenumber": "421-429-7655x39421",
        "address": "597 Smith Point",
        "jobtitle": "Chief Tecology Officer",
        "skillset": "python, pandas"
    };

    await api.post('/check/singlecandidate', a).then((response: any) => {
        console.log('RETURN!')
        console.log(response)
        return response;
    })
    .catch((error: any) => {
        console.log(error);
        throw error;
    })
}

