<template>
    <div class="p-4 bg-white border border-gray-200 rounded-lg">
        <h3 class="mb-6 text-xl">People you may know</h3>

        <div class="space-y-4">
            <div 
                class="flex items-center justify-between"
                v-for="user in users"
                v-bind:key="user.id"
            >
                <div class="flex items-center space-x-2" v-if="userStore.user.id !== user.id">
                    <img src="https://i.pravatar.cc/40?img=70" alt="profil" class="rounded-full">
                    <p class="text-xs"><strong>{{ user.name }}</strong></p>
                    <RouterLink :to="{name: 'profile', params: {id: user.id}}" class="py-2 px-3 bg-purple-600 text-white text-xs rounded-lg">Show</RouterLink>
                </div>
            </div>
        </div>
    </div>
 </template>
    
<script>

    import axios from 'axios'
    import { useUserStore } from '@/stores/user'

    export default {

        setup() {
            const userStore = useUserStore();
            return {
                userStore,
            };
        },

        data(){
            return{
                users: [],
            }
        },
        mounted(){
            this.getUsers()
        },
        methods:{
            getUsers(){
                axios
                    .get('/api/users/')
                    .then(response => {
                        console.log('data: ', response.data)
                        this.users = response.data
                    })
                    .catch(error => {
                        console.log('error :', error)
                    })
            },
        }
    }
</script>