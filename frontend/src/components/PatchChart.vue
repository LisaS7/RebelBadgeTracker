<script setup>
import { ref, onMounted } from "vue";
import { useBadgeStore } from "@/stores/BadgeStore";
import { colorShade } from "@/utils/functions";
import { SECTION_COLOURS } from "@/utils/constants";

const badgeStore = useBadgeStore();

let patches = ref({});
let patchData = ref([]);
let loaded = ref(false);

function section_colours(data) {
  let patches = {};
  for (const patch in data) {
    patches[patch] = data[patch].map((item) => {
      if (item.substring(0, 4) === "dark") {
        const section = item.substring(5);
        const colour_hex = SECTION_COLOURS[section];
        const darker = colorShade(colour_hex, -150);
        return darker;
      } else {
        return SECTION_COLOURS[item];
      }
    });
  }
  return patches;
}

badgeStore.getPatchData();
patchData.value = badgeStore.patchData;
patches.value = section_colours(patchData.value);
loaded.value = true;
onMounted(async () => {});
</script>

<template v-if="loaded">
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
