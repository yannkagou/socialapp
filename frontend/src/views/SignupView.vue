<!-- <template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
        <div class="main-left">
            <div class="p-12 bg-white border border-gray-2oo rounded-lg">
                <h1 class="mb-6 text-2xl">Sign Up</h1>
                <p class="mb-6 text-gray-500">
                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Repudiandae unde illum minus, nesciunt nihil enim tempora cum? Doloremque maiores vel molestias totam voluptatem dolores quam.
                </p>
                <p class="font-bold">
                    Already have an account? <RouterLink to="/login" class="underline">Click here</RouterLink> to log in!!
                </p>
            </div>
        </div>
        <div class="main-right">
            <div class="p-12 bg-white border border-gray-2oo rounded-lg">
                <form @submit.prevent="submitForm" class="space-y-6" >
                    <div>
                        <label>Name</label><br>
                        <input v-model="form.name" type="text" placeholder="Your full name" class="w-full mt-2 px-6 border border-gray-200 rounded-lg">
                    </div>
                    <div>
                        <label>E-mail</label><br>
                        <input v-model="form.email" type="email" placeholder="Your e-mail address" class="w-full mt-2 px-6 border border-gray-200 rounded-lg">
                    </div>
                    <div>
                        <label>Password</label><br>
                        <input v-model="form.password" type="password" placeholder="Your password" class="w-full mt-2 px-6 border border-gray-200 rounded-lg">
                    </div>
                    <div>
                        <label>Confirm password</label><br>
                        <input v-model="password2" type="password" placeholder="Repeat your password" class="w-full mt-2 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <template v-if="formErrors.length > 0">
                        <div class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in formErrors" :key="error">{{ error }}</p>
                        </div>
                    </template>

                    <div>
                        <button class="py-4 px-6 bg-purple-600 text-white rounded-lg" type="submit">Sign up</button>
                    </div>
                    <div v-if="isLoading">
                        <Yann />
                    </div>
                </form>
            </div>

        </div>
        <Toast/>
     </div>
  </template> 


<script setup>
import axios from 'axios';
import { useToastStore } from '@/stores/toast'
import { useUserStore } from '@/stores/user'
import Yann from '../components/Yann.vue';
import Toast from '@/components/Toast.vue'
import { reactive, ref } from 'vue';
import { useRouter } from 'vue-router';


    const toastStore = useToastStore();
    const userStore = useUserStore();
    const router = useRouter();

    let form = reactive ({
        email: '',
        name: '',
        password: '',
    });
    let password2 = ref('');
    let formErrors = ref([]);
    let isLoading = ref(false);
    let logform = reactive ({
        email: '',
        password: '',
    });



    const submitForm = async () => {
        formErrors.value = []

        if (form.email === '') {
            formErrors.value.push('Your e-mail is missing')
        }

        if (form.name === '') {
            formErrors.value.push('Your name is missing')
        }

        if (form.password === '') {
            formErrors.value.push('Your password is missing')
        }

        if (form.password !== password2.value) {
            formErrors.value.push('The password does not match')
        }

        if (formErrors.value.length === 0) {
            await axios
                .post('/api/signup/', form)
                .then(response => {
                    console.log(response.data)
                        toastStore.showToast('The user is registered. Please activate your account by clicking your email link.')
                        isLoading = true;

                        form.name = ''
                        password2.value = ''

                        logform.email = form.email
                        logform.password = form.password
                    })
                .catch(error => {
                    console.log('error', error)
                })
        }

        if (formErrors.value.length === 0) {

            await axios
                .post('/api/login/', logform)
                .then(response => {
                userStore.setToken(response.data)

                axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access;
                })
                .catch((error) => {
                console.log(error)
                })
        }
        if (formErrors.value.length === 0){
            await axios
                .get('/api/meinfo/')
                .then(response => {
                    console.log('api/me', response.data)
                    userStore.setUserInfo(response.data)
                    form.email = '',
                    form.password = '',
                    router.push('/feed')
                })
                .catch(error => {
                    console.log('error', error)
                })
        }
    }


</script> -->

<template>
    <div class="signup-form">
      <h2>Signup</h2>
      <form @submit.prevent="signup">
        <div>
          <label>Name</label>
          <input type="text" v-model="name" />
        </div>
        <div>
          <label>Password</label>
          <input type="password" v-model="password" />
        </div>
        <div>
          <label>Email</label>
          <input type="email" v-model="email" />
        </div>
        <input type="submit" value="Signup" />
      </form>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  import { ref } from "vue";
  
  export default {
    setup() {
      const name = ref("");
      const password = ref("");
      const email = ref("");
  
      const signup = async () => {
        await axios
            .post("/api/signup/", {
                'name': name.value,
                'password': password.value,
                'email': email.value,
            })
            .then (response => {
                console.log('data', response.data);
            })
            .catch (error => {
                console.log(error);
            })
        };
  
      return {
        name,
        password,
        email,
        signup,
      };
    },
  };
  </script>
  
  <style>
  .signup-form {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  .signup-form h2 {
    margin-bottom: 20px;
  }
  
  .signup-form label {
    display: block;
    margin-bottom: 5px;
  }
  
  .signup-form input[type="text"],
  .signup-form input[type="password"],
  .signup-form input[type="email"] {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border-radius: 5px;
    border: 1px solid #ccc;
  }
  .signup-form input[type="submit"] {
    background-color: #4caf50;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  .signup-form input[type="submit"]:hover {
    background-color: #3e8e41;
  }
  </style>