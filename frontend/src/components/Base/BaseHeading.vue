<script setup>
import { SECTION_COLOURS } from "@/utils/constants";
import { colorShade } from "@/utils/functions";
const { text, section } = defineProps(["text", "section"]);
const colour = SECTION_COLOURS[section];
const adjusted_colour = colorShade(colour, 50);
</script>
<template>
  <h1
    class="heading-tab d-flex flex-row"
    :style="`background: ${colour}; box-shadow: ${adjusted_colour} 0px 0px 5px 10px;`"
  >
    <slot class="heading-icon"></slot>
    <span class="heading-text">{{ text }}</span>
  </h1>
</template>

<style scoped>
.heading-tab {
  color: var(--blue-dark2);
  font-size: 3rem;
  font-weight: 800;
  position: absolute;
  top: 10rem;
  left: 0;
  padding: 2rem 4rem 2rem 5rem;
  border-radius: 5px;
  gap: 2rem;
}

.heading-icon {
  margin-right: 3rem;
}

.heading-text {
  margin: auto 0;
}
</style>
