<template>

  <div>

    <nav class="py-10 px-8 border-b border-gray-200">
      
      <div class="max-w-7xl mx-auto">

        <div class="flex item-center justify-between">

          <div class="menu-left">
            <i class="fas fa-thumbs-up"></i>
          </div>

          <div class="menu-center flex space-x-12" v-if="userStore.user.isAuthenticated">

            <div>
              <RouterLink to="/feed">
                <i class="fa-solid fa-house fa-beat"></i>
              </RouterLink>
            </div>
            <div>
              <RouterLink to="/chat">
                <i class="fas fa-message fa-beat"></i>
              </RouterLink>
            </div>
            <div>
              <!-- <RouterLink> -->
                <i class="fas fa-bell fa-beat"></i>
              <!-- </RouterLink> -->
            </div>
            <div>
              <RouterLink to="/search">
                <i class="fas fa-search fa-beat"></i>
              </RouterLink>
            </div>

          </div>

          <div class="menu-right flex space-x-2">

            <template v-if="userStore.user.isAuthenticated">

              <RouterLink :to="{name: 'profile', params: {id: userStore.user.id}}">
                <img src="https://i.pravatar.cc/40?img=70" alt="profil" class="rounded-full">
              </RouterLink>
              
            </template>

            <template v-else>

              <RouterLink to="/login" class="mr-4 py-4 px-6 bg-gray-600 text-white rounded-lg">Login</RouterLink>
              <RouterLink to="/signup" class="py-4 px-6 bg-purple-600 text-white rounded-lg">Sign Up</RouterLink>

            </template>
          </div>

        </div>
        
      </div>

    </nav>

    <main class="px-8 py-6 bg-gray-100">

      <RouterView />
      
    </main>

  </div>
</template>

<script setup>
import axios from 'axios'
import { useUserStore } from '@/stores/user'

  const userStore = useUserStore();

  userStore.initStore();
  const token = userStore.user.access;

  if (token) {
      axios.defaults.headers.common["Authorization"] = "Bearer " + token;
  }
  else {
      axios.defaults.headers.common["Authorization"] = "";
  }

</script>

<style scoped>
 
</style>


