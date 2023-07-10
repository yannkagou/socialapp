<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">

        <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
                <div class="flex items-center justify-center">
                    <img src="https://i.pravatar.cc/40?img=70" alt="profil" class="rounded-full w-4/5">
                </div>
                <p><strong>{{ user.name }}</strong></p>
                <div class="mt-6 flex space-x-8 justify-around">
                        <p class="text-xs text-gray-500">{{ user.friend_count }} friends</p>
                    <p class="text-xs text-gray-500">18 posts</p>
                </div>
            </div>

        <div  class="main-center col-span-2 space-y-4">
            <div v-if="friendshipRequests.length">
                <h2 class="text-xl mb-6">Friendship Requests</h2>
                <div class="p-4 bg-white border border-gray-200 rounded-lg" v-for="friendshipRequest in friendshipRequests" :key="friendshipRequest.id">
                    <div>
                        <p><strong>
                        <RouterLink :to="{name: 'profile', params: {'id': friendshipRequest.created_by.id}}">  {{ friendshipRequest.created_by.name }}</RouterLink>
                        </strong></p>
                        <p>{{ friendshipRequest.created_by.friend_count }}</p>
                    </div>
                    <div class="mt-6 space-x-4">
                        <button class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg" @click="handleRequest('accepted', friendshipRequest.created_by.id)">Accept</button>
                        <button class="inline-block py-4 px-6 bg-red-600 text-white rounded-lg" @click="handleRequest('rejected', friendshipRequest.created_by.id)">Reject</button>
                    </div>
                </div> 
                <hr>
            </div>

            <div v-if="friends.length">
                <h2 class="text-xl mb-6">Friends</h2>
                <div class="p-4 bg-white border border-gray-200 rounded-lg" v-for="friend in friends" :key="friend.id">
                    <p><strong>
                    <RouterLink :to="{name: 'profile', params: {'id': friend.id}}">  {{ friend.name }} </RouterLink>
                    </strong></p>
                    <p>{{ friend.name }}</p>
                </div> 
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
import axios from 'axios';
import { useUserStore } from '@/stores/user'
import { onMounted, reactive, ref } from 'vue';
import { useRoute } from 'vue-router';


    const userStore = useUserStore()
    const route = useRoute()

    let user = reactive({});
    let friendshipRequests = ref([]);
    let friends = ref([]);

    onMounted(() => {
        getFriends();
    });

       
    function getFriends() {
        axios
            .get(`/api/friends/${route.params.id}/`)
            .then(response => {
                console.log('data: ', response.data)
                friendshipRequests.value = response.data.requests
                friends.value = response.data.friends
                user = response.data.user
            })
            .catch(error => {
                console.log('error :', error)
            })
    };

    function handleRequest(status, pk) {
        console.log('status: ', status)
        axios
            .post(`/api/friends/${pk}/${status}/`)
            .then(response => {
                console.log('data: ', response.data)
            })
            .catch(error => {
                console.log('error', error)
            })
    }

</script>