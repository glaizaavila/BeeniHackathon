
export interface CandidateRequest {
    applicationDate: string,
    firstName: string,
    lastName: string, 
    gender: string,
    birthDate: string,
    phoneNumber: string,
    email: string,
    address: string,
    educationLevel: string,
    yearsOfExperience: string,
    jobTitle: string,
    status: string,
    supplierName: string,
    customerName: string,
    skills: string
}

export interface CandidateResponse {
    applicantId: string,
    applicationDate: Date,
    firstName: string,
    lastName: string,
    gender: string,
    birthDate: Date,
    phoneNumber: string,
    email: string,
    address: string,
    educationLevel: string,
    yearsOfExperience: string,
    jobTitle: string,
    status: string,
    supplierName: string,
    customerName: string,
    skills: string,
    averageScore: number
}
