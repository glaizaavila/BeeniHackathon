<template>
  <form @submit.prevent="submitCandidateData">
    <div>
      <h3>Personal Information</h3>
      <label>Firstname:</label>
      <input type="text" required v-model="candidateRequest.firstName" v-bind="candidateRequest.firstName.value">
      <label>Lastname:</label>
      <input type="text" required v-model="candidateRequest.lastName" v-bind="candidateRequest.lastName.value">
      <label>Email:</label>
      <input type="email" required v-model="candidateRequest.email" v-bind="candidateRequest.email.value">
      <label>Phone Number:</label>
      <input type="text" class="no-spinner" v-model="candidateRequest.phoneNumber"
        v-bind="candidateRequest.phoneNumber.value">
      <label>Birthdate:</label>
      <input type="date" v-model="candidateRequest.birthDate" v-bind="candidateRequest.birthDate.value">
      <label>Address:</label>
      <input type="text" v-model="candidateRequest.address" v-bind="candidateRequest.address.value">
      <label>Gender:</label>
      <input type="radio" id="male" value="Male" v-model="candidateRequest.gender"
        v-bind="candidateRequest.gender.value" />
      <label for="male">Male</label>
      <input type="radio" id="female" value="Female" v-model="candidateRequest.gender"
        v-bind="candidateRequest.gender.value" />
      <label for="female">Female</label>
    </div>

    <h3>Other Details</h3>
    <label>Educational Level:</label>
    <input type="text" v-model="candidateRequest.educationLevel" v-bind="candidateRequest.educationLevel.value">
    <label>Years of Experience:</label>
    <input type="text" v-model="candidateRequest.yearsOfExperience" v-bind="candidateRequest.yearsOfExperience.value">
    <label>Job Title:</label>
    <input type="text" v-model="candidateRequest.jobTitle" v-bind="candidateRequest.jobTitle.value">
    <label>Skills:</label>
    <textarea v-model="candidateRequest.skills" v-bind="candidateRequest.skills.value"
      placeholder="Add skills in comma-separated format"></textarea>
    <label>Supplier Name:</label>
    <input type="text" v-model="candidateRequest.supplierName" v-bind="candidateRequest.supplierName.value">
    <label>Customer Name:</label>
    <input type="text" v-model="candidateRequest.customerName" v-bind="candidateRequest.customerName.value">
    <div class="submit">
      <button>Submit Candidate</button>
    </div>
    <!-- <CandidateDataTable></CandidateDataTable> -->
  </form>


  <div class="table" v-if="responseDuplicates">
    <h3>Possible Duplicate Candidates</h3>

    <EasyDataTable :headers="headers" :items="responseDuplicates" theme-color="#1d90ff"
      table-class-name="customize-table" header-text-direction="center" body-text-direction="center"
      @click-row="openProfile" />

  </div>



</template>

<script setup lang="ts">
import { defineComponent, ref } from 'vue';
import { getDuplicates, viewCandidates } from '../api/candidateChecker'
import CandidateDataTable from "../components/CandidateDataTable.vue"
import type { CandidateRequest, CandidateResponse } from "@/interfaces/candidate.ts";
import type { Header, Item } from "vue3-easy-data-table";

const candidateRequest: CandidateRequest = ref(
  {
    applicationDate: "09/26/2024",
    firstName: "",
    lastName: "",
    gender: "",
    birthDate: "",
    phoneNumber: "",
    email: "",
    address: "",
    educationLevel: "",
    yearsOfExperience: "",
    jobTitle: "",
    status: "",
    supplierName: "",
    customerName: "",
    skills: ""
  }
)

const headers: Header[] = [
  { text: "Firstname", value: "firstName" },
  { text: "Lastname", value: "lastName" },
  { text: "Gender", value: "gender" },
  { text: "Birth Date", value: "birthDate" },
  { text: "Contact #", value: "phoneNumber" },
  { text: "Email", value: "email" },
  { text: "Address", value: "address" },
  { text: "Educational Level", value: "educationLevel" },
  { text: "Yrs. of Exp", value: "yearsOfExperience" },
  { text: "Job Title", value: "jobTitle" },
  { text: "Status", value: "status" },
  { text: "Supplier Name", value: "supplierName" },
  { text: "Customer Name", value: "customerName" },
  { text: "Application Date", value: "applicationDate" },
  { text: "Duplicate Percentage", value: "averageScore", sortable: true }
];
const items: Item[] = []
const addRow = () => {
  items.push({ name: '', height: 0, weight: 0, age: 0 });
};

let responseDuplicates = ref([] as Array<CandidateResponse>)

const submitCandidateData = async () => {
  try {
    const resp = await getDuplicates(candidateRequest.value);
    console.log(resp);
    if (JSON.stringify(resp) === '{}') {
      candidateRequest.value =
      {
        applicationDate: "09/26/2024",
        firstName: "",
        lastName: "",
        gender: "",
        birthDate: "",
        phoneNumber: "",
        email: "",
        address: "",
        educationLevel: "",
        yearsOfExperience: "",
        jobTitle: "",
        status: "",
        supplierName: "",
        customerName: "",
        skills: ""
      }
      alert("No duplicate. Candidate profile successfully saved!");
      //responseDuplicates.value = [];
    }
    else
    {
      responseDuplicates.value = resp;
    }
  } catch (error: unknown) { // Specify the type of error
    console.error('Error in submitCandidateData:', error);
  }
}

const formatDateToMMDDYYYY = (date: string) => {
  const [year, month, day] = date.split('-');
  return `${month}/${day}/${year}`;
}

</script>

<style>
form {
  width: 186%;
  display: block;
  margin: 20px auto;
  background: white;
  text-align: left;
  padding: 20px 30px;
  border-radius: 10px;
}

label {
  color: #414141;
  display: inline-block;
  margin: 25px 0 15px;
  font-size: 0.6em;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-weight: bold;
}

input,
select,
textarea {
  display: block;
  padding: 10px 6px;
  width: 100%;
  box-sizing: border-box;
  border: none;
  border-bottom: 1px solid #ddd;
  color: #555;
}

input[type="radio"] {
  display: inline-block;
  width: 16px;
  margin: 0 10px 0 0;
  position: relative;
  top: 2px;
}

button {
  background: #588548;
  border: 0;
  padding: 10px 20px;
  margin-top: 20px;
  margin-left: auto;
  margin-right: auto;
  color: white;
  border-radius: 20px;
  cursor: pointer;
}

#table {
  margin-bottom: 30px;
}

/* Change style on hover */
button:hover {
  background-color: #4f7741;
}

/* button:active {
  background-color: #588548;
} */

#cform {
  max-width: 600px;
  margin: 10px auto;
  background: rgb(146, 185, 130);
  text-align: left;
  padding: 30px;
  border-radius: 10px;
}

h3 {
  padding-top: 10px;
}

/* Hide the spinner buttons in Chrome, Safari, Edge, and Opera */
.no-spinner::-webkit-outer-spin-button,
.no-spinner::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

.customize-table {
  --easy-table-border: 5px solid #448500;
  --easy-table-row-border: 3px solid #448500;

  --easy-table-header-font-size: 18px;
  --easy-table-header-height: 25px;
  --easy-table-header-font-color: #ffffff;
  --easy-table-header-background-color: #448500;

  --easy-table-header-item-padding: 10px 15px;

  --easy-table-body-even-row-font-color: #242424;
  --easy-table-body-even-row-background-color: #4c5d7a;

  --easy-table-body-row-font-color: #16171a;
  --easy-table-body-row-background-color: #ffffff;
  --easy-table-body-row-height: 30px;
  --easy-table-body-row-font-size: 16px;

  --easy-table-body-row-hover-font-color: #ffffff;
  --easy-table-body-row-hover-background-color: #063f1e;

  --easy-table-body-item-padding: 10px 15px;

  --easy-table-footer-background-color: #448500;
  --easy-table-footer-font-color: #ffffff;
  --easy-table-footer-font-size: 14px;
  --easy-table-footer-padding: 0px 10px;
  --easy-table-footer-height: 30px;

  --easy-table-rows-per-page-selector-width: 350px;
  --easy-table-rows-per-page-selector-option-padding: 10px;
  --easy-table-rows-per-page-selector-z-index: 1;


  --easy-table-scrollbar-track-color: #2d3a4f;
  --easy-table-scrollbar-color: #2d3a4f;
  --easy-table-scrollbar-thumb-color: #4c5d7a;
  ;
  --easy-table-scrollbar-corner-color: #2d3a4f;

  --easy-table-loading-mask-background-color: #2d3a4f;

  border-radius: 15px;
}

EasyDataTable {
  margin-left: auto;
  margin-right: auto;
}

.root {
  position: relative;
}

.modal {
  position: absolute;
  top: 0;
  left: 0;
  background-color: rgba(0, 0, 0, 0.1);
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal>div {
  background-color: white;
  padding: 50px;
  border-radius: 10px;
}
</style>