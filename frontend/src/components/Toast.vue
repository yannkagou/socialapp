  <!-- <template>
  <div v-if="toastState.isVisible" :class="['toast', toastState.type]">
    {{ toastState.message }}
  </div>
</template>

<script>
import { computed } from 'vue'
import { toastState } from '@/stores/toast'

export default {
  setup() {
    const toastClasses = computed(() => {
      return {
        'toast': true,
        'success': toastState.type === 'success',
        'error': toastState.type === 'error'
      }
    })

    return {
      toastState,
      toastClasses
    }
  }
}
</script>

<style>
.toast {
  position: fixed;
  bottom: 20px;
  right: 20px;
  padding: 10px;
  border-radius: 5px;
  color: #fff;
  font-weight: bold;
}

.success {
  background-color: #4BB543;
}

.error {
  background-color: #FF4136;
}
</style> -->

<template>
  <div
      v-if="store.isVisible"
      class="bg-green-200"
  >
      {{ store.message }}
  </div>
</template>

<script setup>
  import { useToastStore } from '@/stores/toast'

  const store = useToastStore()
</script>

