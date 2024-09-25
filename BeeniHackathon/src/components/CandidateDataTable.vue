<template>
  
    
  <EasyDataTable
    :headers="headers"
    :items="items"
    theme-color="#1d90ff"
    table-class-name="customize-table"
    header-text-direction="center"
    body-text-direction="center"
    @click-row="openProfile"
  />
  
  <ProfileModal v-if="isOpen" @close="closeProfile" ></ProfileModal>
</template>

<script lang="ts">
import type { Header, Item, ClickRowArgument } from "vue3-easy-data-table"
import ProfileModal from "./ProfileModal.vue";

export default{
  data() {
    return {
      isOpen: false
   }
  },
  methods:{
    showRow(any: row){
      console.log(row)
    },
    openProfile(){
      this.isOpen = true
    },
    closeProfile(){
      this.isOpen = false
    },
    readCSV(){
    }
  },
  setup() {
    const headers: Header[] = [
      { text: "Name", value: "name" ,sortable: true},
      { text: "Score", value: "score", sortable: true }
    ];

    const items: Item[] = [
      { "name": "Glaiza Avila", "score": 70 },
      { "name": "Eileen Garcia", "score": 30 },
      { "name": "Jazmin Ruma", "score": 12}
    ];

    return {
      headers,
      items
    };
  },
  components:{
    ProfileModal
  }
};
</script>

<style>

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