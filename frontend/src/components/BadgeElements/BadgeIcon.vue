<script setup>
import { SECTION_COLOURS } from "@/utils/constants";

const props = defineProps(["section", "image"]);
const colour = SECTION_COLOURS[props.section];
</script>
<template>
  <div
    class="badge-icon"
    :style="`background:${colour}`"
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
