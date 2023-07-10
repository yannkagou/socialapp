<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">

        <div class="main-center col-span-3 space-y-4">
            
            <div class="my-6 flex items-center justify-between" v-if="post.id">
                <FeedItem :post="post"></FeedItem>
            </div>

            <div class="p-4 ml-8 bg-white border border-gray-200 rounded-lg" v-for="comment in post.comments" :key="comment.id">
                <CommentItem :comment="comment" />
            </div>

            <div class="bg-gray-100 border border-gray-200 rounded-lg">
                <form @submit.prevent="submitForm" method="post">

                    <input type="textarea" v-model="body" class="p-4 w-full bg-white rounded-lg" placeholder="What do you think?">
                    <div class="p-4 border-t border-gray-100 flex justify-between">
                        <button type="submit" class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg">Comment</button>
                    </div>
                </form>
            </div>
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
import CommentItem from '../components/CommentItem.vue';
import axios from 'axios';
import { onMounted, reactive, ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';

    const route = useRoute();
    let post = reactive ({
        id: null,
        comments: [],
    });

    let body = ref("");

    onMounted(() =>{
        getPost()
    });

    function getPost() {
        axios
            .get(`/api/posts/${route.params.id}`)
            .then(response => {
                console.log('data: ', response.data)
                post = response.data.post
            })
            .catch(error => {
                console.log('error :', error)
        })
    };

    function submitForm() {
        console.log("submitForm ", body.value)
        axios
            .post(`/api/posts/${route.params.id}/comment/`, {
                'body': body.value
            })
            .then(response => { 
                post.comments.push(response.data)
                post.comments_count += 1
                body.value = ''
            })
            .catch(error => {
                console.log('error', error)
        })
    };

</script>