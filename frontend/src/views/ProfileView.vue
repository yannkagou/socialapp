<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">

        <div class="main-left col-span-1">
            <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
                <div class="flex items-center justify-center">
                    <img src="https://i.pravatar.cc/40?img=70" alt="profil" class="rounded-full w-4/5">
                </div>
                <p><strong>{{ user.name }}</strong></p>
                <div class="mt-6 flex space-x-8 justify-around">
                    <RouterLink :to="{name: 'friends', params: {id: user.id}}">
                        <p class="text-xs text-gray-500">{{ user.friend_count }} friends</p>
                    </RouterLink>
                    <p class="text-xs text-gray-500">18 posts</p>
                </div>
                <div class="mt-6">
                    <button v-if="userStore.user.id !== user.id" class="inline-block py-4 px-3 bg-purple-600 text-xs text-white rounded-lg" @click="sendFriendshipRequest">
                        Send Friendship Request
                    </button>
                    <button v-if="userStore.user.id === user.id" class="inline-block py-4 px-3 bg-purple-600 text-xs text-white rounded-lg" @click="logout">
                        Logout
                    </button>
                </div>
            </div>
        </div>

        <div class="main-center col-span-2 space-y-4">
            <div class="bg-white border border-gray-200 rounded-lg">
                <div class="p-4" v-if="userStore.user.id === user.id">
                    <form @submit.prevent="submitForm" method="post">
                        <input type="textarea" v-model="body" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="What are you thinking about?">
                        <div class="p-4 border-t border-gray-100 flex justify-between">
                            <button class="inline-block py-4 px-6 bg-gray-600 text-white rounded-lg">Attach image</button>
                            <button type="submit" class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg">Post</button>
                        </div> 
                    </form>
                </div>
            </div>
            <div class="my-6 flex items-center justify-between" v-for="post in posts" :key="post.id">
                <FeedItem :post="post"></FeedItem>
            </div>
        </div>

        <div class="main-right col-span-1 space-y-4">
            <PeopleYouMayKnow/>
            <Trends/>
        </div>
    </div>
</template>

<script>

    import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue';
    import Trends from '../components/Trends.vue';
    import FeedItem from '../components/FeedItem.vue';
    import axios from 'axios';
    import { useUserStore } from '@/stores/user'
    import { useToastStore } from '@/stores/toast'


    export default {
        name: "ProfileView",

        setup() {
            const userStore = useUserStore();
            const toastStore = useToastStore()
            return {
                userStore,
                toastStore
            };
        },

        components:{
            PeopleYouMayKnow,
            Trends,
            FeedItem,
        },

        data(){
            return{
                posts: [],
                user: {
                    id: null
                },
                body: '',
            }
        },

        mounted(){
            this.getFeeds()
        },

        watch: { 
            '$route.params.id': {
                handler: function() {
                    this.getFeeds()
                },
                deep: true,
                immediate: true
            }
        },

        methods:{
            getFeeds(){
                axios
                    .get(`/api/posts/profile/${this.$route.params.id}/`)
                    .then(response => {
                        this.posts = response.data.posts
                        this.user = response.data.user
                    })
                    .catch(error => {
                        console.log('error :', error)
                    })
            },
            sendFriendshipRequest(){
                axios
                    .post(`/api/friends/${this.$route.params.id}/request/`)
                    .then(response => {
                        console.log('data: ', response.data)
                        if (response.data.message == 'friendship request already sent'){
                            this.toastStore.showToast(5000, 'The request has already been sent!', 'bg-red-300')
                        }else{
                            this.toastStore.showToast(5000, 'The request was sent!', 'bg-emerald-300')
                        }
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
            },
            logout(){
                console.log('logout')

                this.userStore.removeToken()
                this.$router.push('/login')
            },
            submitForm(){
                console.log("submitForm ", this.body)
                axios
                    .post('/api/posts/create/', {
                        'body': this.body
                    })
                    .then(response => {
                        // console.log('data', response.data)
                        this.posts.unshift(response.data)
                        this.body = ''
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
            },
        }
    }
</script>