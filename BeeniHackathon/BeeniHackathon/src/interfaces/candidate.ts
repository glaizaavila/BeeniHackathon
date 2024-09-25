
export interface CandidateRequest {
    firstName: string,
    lastName: string, 
    email: string,
    phoneNumber: string,
    birthDate: string,
    gender: string,
    address: string,
    educationalLevel: string,
    yearsOfExperience: string,
    jobTitle: string,
    skills: string,
    supplierName: string,
    customerName: string
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
