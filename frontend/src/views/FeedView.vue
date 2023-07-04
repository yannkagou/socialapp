<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">

        <div class="main-center col-span-3 space-y-4" v-if="posts.length">
            <div class="p-4 bg-white border border-gray-200 rounded-lg" v-for="post in posts" :key="post.id">
                <FeedItem :post="post"/>
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

    export default {
        name: "FeedView",

        components:{
            PeopleYouMayKnow,
            Trends,
            FeedItem,
        },
        data(){
            return{
                posts: [],
                body: '',
            }
        },
        mounted(){
            this.getFeeds()
        },
        methods:{
            getFeeds(){
                axios
                    .get('/api/posts/')
                    .then(response => {
                        console.log('data: ', response.data)
                        this.posts = response.data
                    })
                    .catch(error => {
                        console.log('error :', error)
                    })
            },
            submitForm(){
                console.log("submitForm ", this.body)
                axios
                    .post('/api/posts/create/', {
                        'body': this.body
                    })
                    .then(response => {
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