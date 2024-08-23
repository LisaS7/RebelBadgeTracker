<script setup>
import { ref } from "vue";
const { value, id } = defineProps(["value", "id"]);
const textContent = ref(value);
import { handleChange } from "@/utils/functions";

function changeText() {}
</script>
<template>
  <div class="notes-container">
    <v-textarea
      label="Notes"
      variant="outlined"
      v-model="textContent"
      @blur="handleChange($event, 'notes', id)"
    />
  </div>
</template>

<style scoped>
.notes-container {
  padding: 2rem 0;
}
</style>
