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

                    <template v-if="errors.length > 0">
                        <div class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in errors" :key="error">{{ error }}</p>
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


<script>
import axios from 'axios';
import { useToastStore } from '@/stores/toast'
import { useUserStore } from '@/stores/user'
import Yann from '../components/Yann.vue';

export default{

    components:{
            Yann,
        },

    setup(){
        const toastStore = useToastStore()
        const userStore = useUserStore()

        return {
            toastStore,
            userStore,
        }
    },

    data(){
        return {
            form: {
                email: '',
                name: '',
                password: '',
            },
            password2: '',
            errors: [],
            isLoading: false,
            logform: {
                email: '',
                password: '',
            },
        }
    },

    methods: {
        async submitForm() {
            this.errors = []

            if (this.form.email === '') {
                this.errors.push('Your e-mail is missing')
            }

            if (this.form.name === '') {
                this.errors.push('Your name is missing')
            }

            if (this.form.password === '') {
                this.errors.push('Your password is missing')
            }

            if (this.form.password !== this.password2) {
                this.errors.push('The password does not match')
            }

            if (this.errors.length === 0) {
                await axios
                    .post('/api/signup/', this.form)
                    .then(response => {
                        console.log(response.data)
                            this.toastStore.showToast(5000, 'The user is registered. Please activate your account by clicking your email link.', 'bg-emerald-300')
                            this.isLoading = true;

                            this.form.name = ''
                            this.password2 = ''

                            this.logform.email = this.form.email
                            this.logform.password = this.form.password
                        })
                    .catch(error => {
                        console.log('error', error)
                    })
            }

            if (this.errors.length === 0) {

                await axios
                    .post('/api/login/', this.logform)
                    .then(response => {
                    this.userStore.setToken(response.data)

                    axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access;
                    })
                    .catch((error) => {
                    console.log(error)
                    })
            }
            if (this.errors.length === 0){
                await axios
                    .get('/api/meinfo/')
                    .then(response => {
                        console.log('api/me', response.data)
                        this.userStore.setUserInfo(response.data)
                        this.form.email = '',
                        this.form.password = '',
                        this.$router.push('/feed')
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
            }
        }
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
