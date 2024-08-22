<script setup>
import { SECTION_COLOURS } from "@/utils/constants";
import { colorShade } from "@/utils/functions";
const { text } = defineProps(["text"]);
const colour = SECTION_COLOURS[text];
const adjusted_colour = colorShade(colour, 50);
</script>
<template>
  <h1
    class="heading-tab"
    :style="`background: ${colour}; box-shadow: ${adjusted_colour} 0px 0px 5px 10px;`"
  >
    {{ text }}
  </h1>
</template>

<style scoped>
.heading-tab {
  color: var(--blue-dark2);
  font-size: 4rem;
  font-weight: 800;
  position: absolute;
  top: 10rem;
  left: 0;
  padding: 2rem 4rem 2rem 5rem;
  border-radius: 5px;
}
</style>
