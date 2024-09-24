<script setup lang="ts">
import TheWelcome from '../components/TheWelcome.vue'
import { testGet } from '../api/candidateChecker.ts'

function callme()
{
  testGet();
}


</script>

<template>
  <main>
    <TheWelcome />
    <button @click="callme">Click Me!</button>
  </main>
</template>
