<template>
    <div>
        <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">

            <div class="main-center col-span-3 space-y-4">

                <form @submit.prevent="submitForm" class="p-4 flex items-center space-x-4 w-4/5 m-auto">
                    <input v-model="query" type="text" placeholder="Search here..." class="px-3 py-2 w-4/5">
                    <button type="submit"><i class="fa-solid fa-magnifying-glass fa-rotate-90 fa-lg" style="color: #65538d;"></i></button>
                </form>

                <div v-if="users.length">
                    <div class="p-4 bg-white border border-gray-200 rounded-lg" v-for="user in users" :key="user.id">
                        <p><strong>
                            <RouterLink :to="{name: 'profile', params: {'id': user.id}}">  {{ user.name }} </RouterLink>
                        </strong></p>
                        <p>{{ user.friend_count }} friends</p>
                    </div>
                </div>

                <div v-if="posts.length" class="space-y-4">
                    <div v-for="post in posts" :key="post.id" class="p-4 bg-white border border-gray-200 rounded-lg">
                        <FeedItem :post="post"/>
                    </div>
                </div>
                
            </div>

            <div class="main-right col-span-1 space-y-4">
                <PeopleYouMayKnow/>
                <Trends/>
            </div>

            
            
        </div>
    </div>
</template>

<script>

    
    import Trends from "../components/Trends.vue";
    import PeopleYouMayKnow from "../components/PeopleYouMayKnow.vue";
    import FeedItem from  "../components/FeedItem.vue";
    import axios from 'axios';

    export default {
        name: 'SearchView',

        components:{
            PeopleYouMayKnow,
            Trends,
            FeedItem,
        },

        data(){
            return {
                query: "",
                users: [],
                posts: []
            }
        }, 
        methods: {
            submitForm(){
                console.log('submitForm', this.query)

                axios
                    .post('/api/search/', {
                        query: this.query
                    })
                    .then (response => {
                        console.log ('response: ', response.data)
                        this.users = response.data.users;
                        this.posts = response.data.posts;
                    })
                    .catch (error => {
                        console.log('error', error)
                    })
            }
        }
    }


</script>