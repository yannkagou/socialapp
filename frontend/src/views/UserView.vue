<template>
    <div>
      <h1>Informations utilisateur</h1>
      <p v-if="loading">Chargement...</p>
      <div v-if="!loading">
        <!-- <p><strong>ID:</strong> {{ user.id }}</p> -->
        <p><strong>name:</strong> {{ user.name }}</p>
        <p><strong>Email:</strong> {{ user.email }}</p>
      </div>
    </div>
  </template>
  
  <script setup>
  import axios from 'axios';
  import { useCookies } from "vue3-cookies";
  import { onMounted, reactive, ref } from 'vue';

    let user = reactive({
        id: null
    });
    let loading = ref(true);
    const { cookies } = useCookies();

    onMounted(() => {
        // const accessToken = cookies.get("access_token");
        axios.get('/api/user/', {
            headers: {
            'Authorization': `Bearer ${cookies.get("access_token")}` 
            // 'Bearer ' + cookies.get("access_token"),
            },  
            withCredentials: true,
        })
        .then(response => {
            user = response.data;
            loading.value = false;
            console.log(user)
            console.log(loading.value)
            console.log(accessToken)
        })
        .catch(error => {
            console.log('error', error);
            loading.value = false;
        });
    });
 
  </script>