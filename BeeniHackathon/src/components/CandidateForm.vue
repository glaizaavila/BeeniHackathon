<template>
    <form @submit.prevent="saveCandidate">
      <div>
        <div>
          <h3>Personal Information</h3>
          <label>Firstname:</label>
          <input type="text" require v-model="firstname">
          <span v-if="reqFieldEmptyError" class="error"> {{ reqFieldEmptyError }}</span>
          <label>Lastname:</label>
          <input type="text" required v-model="lastname">
          <label>Email:</label>
          <input type="email" required v-model="email">
          <label>Phone Number:</label>
          <input type="number" required v-model.number="phonenumber">
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
          <input type="number" required v-model.number="zipcode">
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
        <textarea v-model="skills" placeholder="Add skills in comma-separated format" @keyup.alt="addSkill"></textarea>
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

<script>
  export default {
    data() {
      return {
        firstname: '',
        lastname: '',
        email: '',
        jobtitle: '',
        phonenumber: '',
        tempSkills: '',
        skills: []
      }
    },
    methods: {
      addSkill(skill) {
        if (skill.key === ',' && this.tempSkills) {
          this.skills.push(this.tempSkills)
        }
      },
      saveCandidate(){
        this.reqFieldEmptyError = this.firstname === '' ? 'This is a required field' : '';
        // if (this.firstname === '') {
        //   this.reqFieldEmptyError = 'This is a required field';
        //   console.log("no firstnmame")
        // }
        console.log(this.firstname)
        console.log(this.lastname)
        console.log(this.email)
        console.log(this.phonenumber)
      }
    }

  }
</script>

<style>
</style>
<!-- <script setup>
  import {reactive} from 'vue'
  import QuickvForm from '@/components/Form.vue'
  import QuickvInput from '@/components/Input.vue'

  const formData = reactive({
    firstName:'',
    lastName:'',
    email:'',
    phoneNumber:'',
    age:'',
    password:''
  })
  


</script>
<template>
  <div>
    <quickv-form formId="authForm" name="myAuthForm">
      <div class="grid grid-cols-2 gap-4 container mx-auto my-4">
        <QuickvInput
          inputId="firstName"
          inputName="myInputFirstName"
          fieldPlaceholder="firstName" 
          label="firstName"
          qvRules='required|minlength:3|maxlength:20'
          qvMessages='The firstname is required | The name should be at least 3 characters | The field size should not exceed 20 characters'
          qvInvalidClass='border border-red-500'
          qvValidClass='border border-green-500'
          v-model="formData.firstName"
        />
        <QuickvInput
          inputId="lastName"
          inputName="myInputLastName"
          fieldPlaceholder="lastName" 
          label="lastName"
          qvRules='required|minlength:3|maxlength:20'
          qvMessages='The lastname is required | The name should be at least 3 characters | The field size should not exceed 20 characters'
          qvInvalidClass='border border-red-500'
          qvValidClass='border border-green-500'
          v-model="formData.lastName"
        />
        <QuickvInput
          inputId="email"
          inputName="myInputEmail"
          type="email"
          fieldPlaceholder="Email" 
          label="email"
          qvRules='required|email'
          qvMessages='The email is required | invalid email'
          qvInvalidClass='border border-red-500'
          qvValidClass='border border-green-500'
          v-model="formData.email"
        />
        <QuickvInput
          inputId="phoneNumber"
          inputName="myInputPhone"
          type="number"
          fieldPlaceholder="PhoneNumber" 
          label="phoneNumber"
          qvRules='required|number'
          qvMessages='The phoneNumber is required | invalid number'
          qvInvalidClass='border border-red-500'
          qvValidClass='border border-green-500'
          v-model="formData.phoneNumber"
        />
        <QuickvInput
          inputId="age"
          inputName="myInputAge"
          type="number"
          fieldPlaceholder="Age" 
          label="Age"
          qvRules='required|number|between:18,35'
          qvMessages='age is required | invalid number| number between 18 and 35'
          qvInvalidClass='border border-red-500'
          qvValidClass='border border-green-500'
          v-model="formData.age"
        />
        <QuickvInput
          inputId="password"
          inputName="myInputPassword"
          type="password"
          fieldPlaceholder="Password" 
          label="password"
          qvRules='required|password'
          qvMessages='password is required |invalide password ,password contain  !@#$%^&*(),.?":{}|<>'
          qvInvalidClass='border border-red-500'
          qvValidClass='border border-green-500'
          v-model="formData.password"
        />
      </div>


    </quickv-form>

  </div>
</template>

<style  scoped>

</style> -->