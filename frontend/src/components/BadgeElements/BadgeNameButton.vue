<script setup>
const props = defineProps(["id", "name"]);
</script>
<template>
  <RouterLink :to="`/badge/${id}`"
    ><v-btn variant="outlined" color="blue-lighten-5">{{
      name
    }}</v-btn></RouterLink
  >
</template>
