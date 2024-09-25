<template>
    <form @submit.prevent="saveCandidate">
      <div>
        <div>
          <h3>Personal Information</h3>
          <label>Firstname:</label>
          <input type="text" required v-model="firstname">
          <label>Lastname:</label>
          <input type="text" required v-model="lastname">
          <label>Email:</label>
          <input type="email" required v-model="email">
          <label>Phone Number:</label>
          <input type="number" required class="no-spinner" v-model.number="phonenumber">
          <label>Gender:</label>
          <input type="radio" id="male" value="Male" v-model="gender" />
          <label for="male">Male</label>
          <input type="radio" id="female" value="Female" v-model="gender" />
          <label for="female">Female</label>
        </div>
        
        <div>
          <h3>Address</h3>
          <label>City:</label>
          <input type="text" require v-model="city">
          <label>Country:</label>
          <input type="text" required v-model="country">
          <label>State:</label>
          <input type="text" required v-model="state">
          <label>Zip Code:</label>
          <input type="number" required class="no-spinner" v-model.number="zipcode">
        </div>
        
        <h3>Other Details</h3>
        <label>Educational Level:</label>
        <select v-model="educationallevel">
          <option value="Associate Degree">ssociate Degree</option>
          <option value="Bachelor’s degree">Bachelor’s degree</option>
          <option value="Master’s Degree">Master’s Degree</option>
          <option value="Doctorate Degree">Doctorate Degree</option>
        </select>
        <label>Years of Experience:</label>
        <input type="text" required v-model="yearsofexp">
        <label>Job Title:</label>
        <select v-model="jobtitle">
          <option value="Business Intelligence Engineer">Business Intelligence Engineer</option>
          <option value="Software Engineer">Software Engineer</option>
        </select>
        <label>Skills:</label>
        <textarea v-model="skills" placeholder="Add skills in comma-separated format"></textarea>
        <label>Supplier Name:</label>
        <input type="text" required v-model="suppliername">
        <label>Customer Name:</label>
        <input type="text" required v-model="customername">
        <div class="submit">
          <button>Save Candidate</button>
        </div>
       
        
      </div>
    </form>
</template>

<script setup lang="ts">
  
</script>
