<script setup>
const props = defineProps(["colour", "image"]);
</script>
<template>
  <div
    class="badge-icon"
    :style="`background:${props.colour}`"
    v-html="`${props.image}`"
  ></div>
</template>

<style scoped>
.badge-icon {
  width: 40px;
  height: 40px;
  padding: 8px;
  border-radius: 50%;
}
</style>
