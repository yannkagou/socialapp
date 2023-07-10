import { defineStore } from 'pinia'

export const useToastStore = defineStore({
    id: 'toast',
    state: () => ({
        type: '',
        message:'',
        isVisible: false
    }),

    actions: {
        showToast(message, type = 'success'){
            this.message = message
            this.type = type
            this.isVisible = true

            setTimeout(() => {
                useToastStore.isVisible = false
            }, 2000)
        }
    }
})




// import { reactive } from 'vue'

// export const toastState = reactive({
//   isVisible: false,
//   message: '',
//   type: ''
// })

// export function showToast(message, type = 'success') {
//   toastState.isVisible = true
//   toastState.message = message
//   toastState.type = type
  
//   setTimeout(() => {
//     toastState.isVisible = false
//   }, 5000)
// }

