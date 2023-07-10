<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">

        <div class="main-center col-span-3 space-y-4" v-if="posts.length">
            <div class="p-4 bg-white border border-gray-200 rounded-lg" v-for="post in posts" :key="post.id">
                <FeedItem :post="post"/>
            </div>
        </div>
        <div v-else  class="main-center col-span-3 space-y-4">
            <h1 class="text-center">NO POSTS FOR THE MOMENT</h1>
        </div>

        <div class="main-right col-span-1 space-y-4">
            <PeopleYouMayKnow/>
            <Trends/>
        </div>
        
    </div>
</template>

<script setup>

import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue';
import Trends from '../components/Trends.vue';
import FeedItem from '../components/FeedItem.vue';
import axios from 'axios';
import { ref, onMounted } from 'vue';


    let posts = ref([]);
    let body = ref('');

    function getFeeds() {
        axios
            .get('/api/posts/')
            .then(response => {
                console.log('data: ', response.data)
                posts.value = response.data
            })
            .catch(error => {
                console.log('error :', error)
            })
    };

    function submitForm() {
        console.log("submitForm ", body.value)
        axios
            .post('/api/posts/create/', {
                'body': body.value
            })
            .then(response => {
                posts.unshift(response.data)
                body.value = ''
            })
            .catch(error => {
                console.log('error', error)
            })
    };

    onMounted(() => {
        getFeeds();
    });

</script>