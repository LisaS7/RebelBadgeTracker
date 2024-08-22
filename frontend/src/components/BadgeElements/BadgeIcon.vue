<script setup>
import { SECTION_COLOURS } from "@/utils/constants";

const { section, image, size } = defineProps(["section", "image", "size"]);
const colour = SECTION_COLOURS[section];

let iconSize = "70px";
if (size === "lg") {
  iconSize = "100px";
} else if (size === "sm") {
  iconSize = "40px";
}
</script>
<template>
  <div
    class="badge-icon"
    :style="`background:${colour}`"
    v-html="`${image}`"
  ></div>
</template>

<style scoped>
.badge-icon {
  width: v-bind(iconSize);
  height: v-bind(iconSize);
  padding: 8px;
  border-radius: 50%;
}
</style>
