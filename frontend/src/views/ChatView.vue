<template>
    <div>
        <div class="p-4 bg-white border border-gray-200 rounded-lg" v-if="conversations.length">
            <div class="space-y-4">
                <div class="flex items-center justify-between" v-for="conversation in conversations" :key="conversation.id">
                    <div v-for="user in conversation.users" :key="user.id">
                        <div v-if="user.id !== userStore.user.id" >
                            <img src="https://i.pravatar.cc/40?img=70" alt="profil" class="rounded-full"/>
                            <p class="text-xs font.bold text-black" >{{ user.name }}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template> 

<script>
    import axios from 'axios';
    import { useUserStore } from '@/stores/user'

    export default {
        name: 'chat',

        setup(){
            const userStore = useUserStore()

            return{
                userStore,
            }
        },

        data(){
            return{
                conversations: [],
            }
        },

        mounted(){
            this.getConversations()
        },
        methods: {
            getConversations(){

                axios
                    .get('/api/chat/')
                    .then(response => {
                        console.log('get conversation', response.data)
                        this.conversations = response.data
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
            }
        }
    }

</script>