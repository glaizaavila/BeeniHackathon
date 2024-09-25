<template>
  <form @submit.prevent="submitCandidateData">
    <div>
      <h3>Personal Information</h3>
      <label>Firstname:</label>
      <input type="text" required v-model="firstname">
      <label>Lastname:</label>
      <input type="text" required v-model="lastname">
      <label>Email:</label>
      <input type="email" required v-model="email">
      <label>Phone Number:</label>
      <input type="text" class="no-spinner" v-model="phonenumber">
      <label>Birthdate:</label>
      <input type="date" v-model="birthdate">
      <label>Address:</label>
      <input type="text" v-model="address">
      <label>Gender:</label>
      <input type="radio" id="male" value="Male" v-model="gender" />
      <label for="male">Male</label>
      <input type="radio" id="female" value="Female" v-model="gender" />
      <label for="female">Female</label>
    </div>
    
    <h3>Other Details</h3>
    <label>Educational Level:</label>
    <input type="text" v-model="educationallevel">
    <label>Years of Experience:</label>
    <input type="text" v-model="yearsofexperience">
    <label>Job Title:</label>
    <input type="text" v-model="jobtitle">
    <label>Skills:</label>
    <textarea v-model="skills" placeholder="Add skills in comma-separated format"></textarea>
    <label>Supplier Name:</label>
    <input type="text" v-model="suppliername">
    <label>Customer Name:</label>
    <input type="text" v-model="customername">
    <div class="submit">
      <button>Submit Candidate</button>
    </div>
    <!-- <CandidateDataTable></CandidateDataTable> -->
  </form>


  <div class="table" v-if="responseDuplicates">
    <h3>Possible Duplicate Candidates</h3>
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Score</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(duplicate, index) in responseDuplicates" :key="index">
          <td>{{ duplicate.firstName }}</td>
          <td>{{ duplicate.averageScore }}</td>
        </tr>
        <!-- <tr>
          <td>Glaiza Avila<x/td>
          <td>50%</td>
        </tr> -->
      </tbody>
    </table>

    <!-- <EasyDataTable
      :headers="headers"
      :responseDuplicates="responseDuplicates"
    /> -->
  </div>

  
  
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { getDuplicates, viewCandidates } from '../api/candidateChecker'
import CandidateDataTable from "../components/CandidateDataTable.vue"
import type { CandidateRequest, CandidateResponse } from "@/interfaces/candidate.ts";
import type { Header, Item } from "vue3-easy-data-table";

export default defineComponent({
setup() {
  // Declare reactive variables with types
  const firstname = ref<string>('');
  const lastname = ref<string>('');
  const email = ref<string>('');
  const phonenumber = ref<string>('');
  const birthdate = ref<string>('');
  const gender = ref<string>('');
  const address = ref<string>('');
  const jobtitle = ref<string>('');
  const educationallevel = ref<string>('');
  const yearsofexperience = ref<string>('');
  const skills = ref<string>('');
  const suppliername = ref<string>('');
  const customername = ref<string>('');
  const headers: Header[] = [
    { text: "Name", value: "name" },
    { text: "Duplicate Percentage", value: "averageScore", sortable: true }
  ];

  const items: Item[] = []
  //[{ "name": "Stanley Lewis", "score": 90 },
  //{ "name": "Scott Sheppard", "score": 70 }];
  const addRow = () => {
      items.push({ name: '', height: 0, weight: 0, age: 0 });
    };
  return {
    firstname,
    lastname,
    email,
    phonenumber,
    birthdate,
    jobtitle,
    address,
    gender,
    educationallevel,
    yearsofexperience,
    skills,
    suppliername,
    customername,
    newCandidate: {} as CandidateRequest,
    // responseDuplicates: [{
    //   "firstName": "Scott",
    //   "lastName": "Sheppard",
    //   "email": "a@gmail.com",
    //   "phoneNumber": "09345",
    //   "birthDate": "8/31/1992",
    //   "gender": "Male",
    //   "address": "597 Smith PointHollandfort57588Micronesia",
    //   "educationalLevel": "High School",
    //   "yearsOfExperience": "4",
    //   "jobTitle": "Test Engineer",
    //   "skills": "python, css, java",
    //   "supplierName": "Beeline",
    //   "customerName": "Accenture"
    // }]
    responseDuplicates: {} as CandidateResponse,
    headers,
    items
  };
},
async mounted() {
  await this.submitCandidateData();
},
methods: {
  async submitCandidateData(): Promise<void> {
    try {
      // console("Went in submitCandidateData")
      this.newCandidate = {
        "applicationDate": "9/26/2024",
        firstName: this.firstname,
        lastName: this.lastname,
        gender: this.gender,
        birthDate: this.formatDateToMMDDYYYY(this.birthdate),
        phoneNumber: this.phonenumber,
        email: this.email,
        address: this.address,
        educationLevel: this.educationallevel,
        yearsOfExperience: this.yearsofexperience,
        "status": "",
        jobTitle: this.jobtitle,
        supplierName: this.suppliername,
        customerName: this.customername,
        skills: this.skills
      };
      this.responseDuplicates = await getDuplicates(this.newCandidate);
      //this.responseDuplicates = await viewCandidates();
      this.setItems();
      //this.responseDuplicates = response;
      console.log('Response from API:', this.responseDuplicates);
    } catch (error: unknown) { // Specify the type of error
      console.error('Error in submitCandidateData:', error);
    }
  },
  setItems(): void {
    for (const item of this.responseDuplicates) {
      console.log(`ID: ${item.firstName}, Name: ${item.lastName}`)
      const fullName = `${item.firstName} ${item.lastName}`
      const newItem = { "name": fullName, "score": item.averageScore };
      this.items.push(newItem)
      console.log('Fullname ' + newItem.name + ', Score: ' + newItem.score)
    }
    for (const item of this.items) {
      console.log('Fullname ' + item.name + ', Score: ' + item.score)
    }
  },

  formatDateToMMDDYYYY(date: string): string {
    const [year, month, day] = date.split('-');
    return `${month}/${day}/${year}`;
  }
},
});
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

input, select, textarea {
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
  --easy-table-scrollbar-thumb-color: #4c5d7a;;
  --easy-table-scrollbar-corner-color: #2d3a4f;

  --easy-table-loading-mask-background-color: #2d3a4f;
  
  border-radius: 15px;
}

EasyDataTable {
  margin-left: auto;
  margin-right: auto;
}

.root{
  position:relative;
}

.modal{
  position: absolute;
  top: 0;
  left: 0;
  background-color: rgba(0,0,0,0.1);
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal > div {
  background-color: white;
  padding: 50px;
  border-radius: 10px;
}
</style>