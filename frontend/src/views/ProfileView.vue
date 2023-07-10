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

<script setup>

import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue';
import Trends from '../components/Trends.vue';
import FeedItem from '../components/FeedItem.vue';
import axios from 'axios';
import { useUserStore } from '@/stores/user'
import { useToastStore } from '@/stores/toast'
import { onMounted, reactive, ref, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';

    const route = useRoute();
    const router = useRouter();
    const userStore = useUserStore();
    const toastStore = useToastStore();

    let posts = ref([]);
    let user = reactive ({
        id: null
    });
    let body = ref('');

    const getFeeds = () => {
        axios
            .get(`/api/posts/profile/${route.params.id}/`)
            .then(response => {
                posts.value = response.data.posts
                user = response.data.user
            })
            .catch(error => {
                console.log('error :', error)
            })
    };

    const submitForm = () => {
        console.log("submitForm ", body.value)
        axios
            .post('/api/posts/create/', {
                'body': body.value
            })
            .then(response => {
                // console.log('data', response.data)
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

    watch(
    () => route.params.id,
    () => {
        getFeeds();
    },
    { deep: true }
    );

        
    function sendFriendshipRequest(){
        axios
            .post(`/api/friends/${route.params.id}/request/`)
            .then(response => {
                console.log('data: ', response.data)
                if (response.data.message == 'friendship request already sent'){
                    toastStore.showToast('The request has already been sent!')
                }else{
                    toastStore.showToast('The request was sent!')
                }
            })
            .catch(error => {
                console.log('error', error)
            })
    };

    function logout(){
        console.log('logout')

        userStore.removeToken()
        router.push('/login')
    };

</script>