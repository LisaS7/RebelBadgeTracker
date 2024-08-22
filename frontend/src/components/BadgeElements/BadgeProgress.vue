<script setup>
const props = defineProps(["progress"]);
</script>
<template>
  <v-progress-linear :model-value="`${props.progress}`" :height="20" rounded
    ><template v-slot:default="{ value }">
      <strong>{{ Math.ceil(value) }}%</strong>
    </template>
  </v-progress-linear>
</template>

<style scoped>
strong {
  color: black;
}
</style>
