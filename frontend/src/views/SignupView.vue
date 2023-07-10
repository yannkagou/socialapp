<template>
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
     </div>
  </template> 


<script setup>
import axios from 'axios';
import { useToastStore } from '@/stores/toast'
import { useUserStore } from '@/stores/user'
import Yann from '../components/Yann.vue';
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


</script>

// setup(){
    //     const toastStore = useToastStore()

        // let form = {
        //         email: '',
        //         name: '',
        //         password1: '',
        //         password2: '',
        //     }
        
        // let errors = []

        // function showToast() {
        //     toastStore.showToast('This is a success message', 'success');
        //     console.log('Click')
        // }

        // function submitForm() {
        //     errors = []

        //     if (form.email === '') {
        //         errors.push('Your email is missing')
        //     }

        //     if (form.name === '') {
        //         errors.push('Your name is missing')
        //     }

        //     if (form.password1 === '') {
        //         errors.push('Your password is missing')
        //     }

        //     if (form.password1 !== form.password2) {
        //         errors.push('The password does not match')
        //     }

        //     if (errors.length === 0) {
        //         axios
        //         .post('/api/signup/', form)
        //         .then(response => {
        //             console.log(response.data)
        //             if (response.data.message === 'success') {
        //                 toastStore.showToast('The user is registered. Please log in', 'bg-emerald-green')

        //                 form = {
        //                     email: '',
        //                     name: '',
        //                     password1: '',
        //                     password2: ''
        //                 }
        //             } else {
        //                 toastStore.showToast('Something went wrong. Please try again', 'bg-red-300')
        //             }
        //         })
        //         .catch(error => {
        //             console.log('error', error)
        //         })
        //     }
        // }

        // return{
        //     toastStore,
        //     // form,
        //     // errors,
        //     // submitForm,
        //     showToast,
        // }
    // },
