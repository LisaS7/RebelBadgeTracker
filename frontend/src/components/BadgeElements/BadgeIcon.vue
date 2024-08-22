<script setup>
import { SECTION_COLOURS, ICON_SIZES } from "@/utils/constants";

const { section, image, size } = defineProps(["section", "image", "size"]);
const colour = SECTION_COLOURS[section];
let iconSize = ICON_SIZES[size] || "50px";
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
