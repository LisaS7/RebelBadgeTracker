<script setup>
import { ref } from "vue";
const ratings = ref(["None", "✖️", "🟢", "🟡", "🟠", "🔴"]);
const props = defineProps(["current", "id"]);
const current = ref(props.current);
const selected = ref(current);

function changeRating(id, selected) {
  fetch(`http://127.0.0.1:5000/badge/${id}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      id: id,
      rating: selected,
    }),
  });
}
</script>

<template>
  <select
    label="Select"
    @change="changeRating(props.id, selected)"
    v-model="selected"
  >
    <option v-for="rating in ratings" :value="rating">{{ rating }}</option>
  </select>
</template>
