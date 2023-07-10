<!-- <template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
      <div class="main-left">
          <div class="p-12 bg-white border border-gray-2oo rounded-lg">
              <h1 class="mb-6 text-2xl">Log in</h1>
              <p class="mb-6 text-gray-500">
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Repudiandae unde illum minus, nesciunt nihil enim tempora cum? Doloremque maiores vel molestias totam voluptatem dolores quam.
              </p>
              <p class="font-bold">
                  Don't have an account? <RouterLink to="/signup" class="underline">Click here</RouterLink> to create one!!
              </p>
          </div>
      </div>
      <div class="main-right">
          <div class="p-12 bg-white border border-gray-2oo rounded-lg">
              <form class="space-y-6" @submit.prevent="submitForm">
                  <div>
                      <label>E-mail</label><br>
                      <input v-model="form.email" type="email" placeholder="Your e-mail address" class="w-full mt-2 px-6 border border-gray-200 rounded-lg">
                  </div>
                  <div>
                      <label>Password</label><br>
                      <input v-model="form.password" type="password" placeholder="Your password" class="w-full mt-2 px-6 border border-gray-200 rounded-lg">
                  </div>

                  <template v-if="formErrors.length > 0">
                        <div class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in formErrors" :key="error">{{ error }}</p>
                        </div>
                    </template>

                  <div>
                      <button class="py-4 px-6 bg-purple-600 text-white rounded-lg">Log in</button>
                  </div>
              </form>
          </div>
      </div>
    </div>
</template>  -->

<!-- <script setup>
import axios from 'axios';
import { useUserStore } from '@/stores/user'
import { reactive, ref } from 'vue';
import { useRouter } from 'vue-router';

    const userStore = useUserStore();
    const router = useRouter();

    let form = reactive ({
        email: '',
        password: '',
    });

    let formErrors = ref([]);

    const submitForm = async () => {
        formErrors.value = []

        if (form.email === ''){
            formErrors.value.push('Your email is missing')
        }

        if (form.password === ''){
            formErrors.value.push('Your password is missing')
        }

        if (formErrors.value === 0){
            await axios
                .post('/api/login/', form)
                .then(response => {
                userStore.setToken(response.data)

                axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access;
                })
                .catch((error) => {
                console.log(error)
                })
        }
        if (formErrors.value === 0){
            await axios
                .get('/api/meinfo/')
                .then(response => {
                    console.log('api/me', response.data)
                    userStore.setUserInfo(response.data)
                    router.push('/feed')
                })
                .catch(error => {
                    console.log('error', error)
                })
        }
    }

</script> -->

<template>
    <div class="App">
      <form @submit.prevent="login">
        <div>
          <label>Name</label>
          <input type="text" v-model="form.email" />
        </div>
        <div>
          <label>Password</label>
          <input type="password" v-model="form.password" />
        </div>
        <input type="submit" value="Login" />
      </form>
    </div>
  </template>
  
  <script setup>
  import axios from "axios";
  import { reactive } from "vue";
  
    let form = reactive ({
        email: "",
        password: "",
    });

    const login = async () => {
        await axios
                .post("/api/login/", form)
                .then(response => {
                    console.log(response.data);
                })
                .catch(error => {
                    console.log('error', error)
                })
            // { withCredentials: true }
        };

  </script>
  
  <style>
  /* Add any necessary styles here */
  </style>