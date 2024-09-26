<template>

  <h3>Candidate List</h3>

  <EasyDataTable :headers="headers" :items="responseDuplicates" theme-color="#1d90ff" table-class-name="customize-table"
    header-text-direction="center" body-text-direction="center" @click-row="openProfile" />

</template>

<script setup lang="ts">
import type CandidateResponse from '@/interfaces/candidate.ts'
import { viewCandidates } from '@/api/candidateChecker'
import { onMounted, ref, watch } from "vue"

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
  { text: "Application Date", value: "applicationDate" }
];
const items: Item[] = []
const addRow = () => {
  items.push({ name: '', height: 0, weight: 0, age: 0 });
};

let responseDuplicates = ref([] as Array<CandidateResponse>)

onMounted(() => {
  loadData()
});

const loadData = async () => {
  responseDuplicates.value = await viewCandidates();
}

</script>
