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
                        <input v-model="form.password1" type="password" placeholder="Your password" class="w-full mt-2 px-6 border border-gray-200 rounded-lg">
                    </div>
                    <div>
                        <label>Repeat password</label><br>
                        <input v-model="form.password2" type="password" placeholder="Repeat your password" class="w-full mt-2 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <template v-if="errors.length > 0">
                        <div class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in errors" :key="error">{{ error }}</p>
                        </div>
                    </template>

                    <div>
                        <button class="py-4 px-6 bg-purple-600 text-white rounded-lg" type="submit">Sign up</button>
                    </div>
                </form>
            </div>

        </div>
     </div>
  </template> 


<script>
import axios from 'axios';
import { useToastStore } from '@/stores/toast'

export default{

    setup(){
        const toastStore = useToastStore()
        return {
            toastStore
        }
    },

    data(){
        return {
            form: {
                email: '',
                name: '',
                password1: '',
                password2: ''
            },
            errors: [],
        }
    },

    methods: {
        submitForm() {
            this.errors = []

            if (this.form.email === '') {
                this.errors.push('Your e-mail is missing')
            }

            if (this.form.name === '') {
                this.errors.push('Your name is missing')
            }

            if (this.form.password1 === '') {
                this.errors.push('Your password is missing')
            }

            if (this.form.password1 !== this.form.password2) {
                this.errors.push('The password does not match')
            }

            if (this.errors.length === 0) {
                axios
                    .post('/api/signup/', this.form)
                    .then(response => {
                        console.log(response.data)
                        if (response.data.message === 'success') {
                            this.toastStore.showToast(5000, 'The user is registered. Please activate your account by clicking your email link.', 'bg-emerald-300')

                            this.form.email = ''
                            this.form.name = ''
                            this.form.password1 = ''
                            this.form.password2 = ''
                        } else {
                            const data = JSON.parse(response.data.message)
                            for (const key in data){
                                this.errors.push(data[key][0].message)
                            }

                            this.toastStore.showToast(5000, 'Something went wrong. Please try again', 'bg-red-300')
                        }
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
            }
        }
  }

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

}

</script>
