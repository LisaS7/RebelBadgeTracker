<script setup>
import { colorShade } from "@/utils/functions";

const props = defineProps(["patchData"]);

function section_colours(data) {
  let patches = {};
  for (const patch in data) {
    patches[patch] = data[patch].map((colour) => {
      if (colour.substring(0, 4) === "dark") {
        const colour_hex = colour.substring(5);
        const darker = colorShade(colour_hex, -150);
        return darker;
      } else {
        return colour;
      }
    });
  }
  return patches;
}

const patches = section_colours(props.patchData);
</script>

<template>
  <h3 class="home-header">Section Patch Progress</h3>
  <div v-for="(colours, section) in patches" class="row d-flex flex-row">
    <p class="w-25">{{ section }}</p>
    <div
      v-for="colour in colours"
      class="section-square"
      :style="
        colour
          ? `background: ${colour};`
          : `background: ${colorShade(colour, -100)};`
      "
    ></div>
  </div>
</template>

<style scoped>
.section-square {
  height: 20px;
  width: 20px;
  margin: 10px;
}
</style>
