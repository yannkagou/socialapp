<template>
    <div>
        <div class="mb-6 flex items-center justify-between">
            <div class="flex items-center space-x-6">
                <img src="https://i.pravatar.cc/40?img=70" alt="profil" class="rounded-full">
                <p>
                    <strong>
                        <RouterLink :to="{name: 'profile', params:{id: post.created_by.id}}">{{ post.created_by.name }}</RouterLink>
                    </strong>
                </p>
            </div>
            <p class="text-gray-600">{{ post.created_at_formatted }} ago</p>
        </div>

        <p>{{ post.body }}</p>

        <div class="my-6 flex justify-between">
            <div class="flex space-x-6 items-center">
                <div class="flex items-center space-x-2" @click="likepost(post.id)">
                    <i class="fa-regular fa-heart"></i>
                    <span class="text-gray-500 text-xs">{{ post.likes_count }} likes</span>
                </div>
                
                <div class="flex items-center space-x-2">
                    <RouterLink :to="{name: 'postview', params: {id:post.id}}">
                        <i class="fa-regular fa-comment"></i>
                    </RouterLink>
                    <div class="text-gray-500 text-xs">
                        {{ post.comments_count }}
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>

    import axios from 'axios';

    export default {
        props: {
            post: Object
        },
        methods: {
            likepost(id){
                console.log('Likepost', id)
                axios
                    .post(`/api/posts/${id}/like/`)
                    .then(response => {
                        console.log(response.data)
                        if (response.data.message == 'Like created'){
                            this.post.likes_count += 1
                        } 
                    })
                    .catch(error => {
                        console.log('error', error)
                    })
            }
        }
    }

</script>