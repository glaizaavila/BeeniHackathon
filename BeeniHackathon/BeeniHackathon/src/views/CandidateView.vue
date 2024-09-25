<template>

<CandidateDataTable></CandidateDataTable>

</template>

<script setup lang="ts">
import CandidateDataTable from '@/components/CandidateDataTable2.vue'
import type CandidateResponse from '@/interfaces/candidate.ts'
import { viewCandidates, getDuplicates } from '@/api/candidateChecker'
import { onMounted, ref, watch } from "vue"

onMounted(() => {
  loadData()
});

const loadData = async () => {
  await getDuplicates();
  const list: Array<CandidateResponse> = await viewCandidates();

}



</script>
