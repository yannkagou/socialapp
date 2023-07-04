<template>
    <div>
        <div class="mb-6 flex items-center justify-between">
            <div class="flex items-center space-x-6">
                <div class="flex items-center justify-center">
                    <img src="https://i.pravatar.cc/40?img=70" alt="profil" class="rounded-full w-4/5">
                </div>
                
                <p>
                    <strong>
                        <RouterLink :to="{name: 'profile', params:{id: comment.created_by.id}}">{{ comment.created_by.name }}</RouterLink>
                    </strong>
                </p>
            </div>

            <p class="text-gray-600">{{ comment.created_at_formatted }} ago</p>
        </div>

        <p>{{ comment.body }}</p>

    </div>
</template>

<script>

    export default {
        props: {
            comment: Object
        },
    }

</script>