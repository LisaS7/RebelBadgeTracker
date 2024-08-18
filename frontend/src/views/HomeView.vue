<script setup>
import { ref, onMounted } from "vue";
import BadgeChart from "@/components/Chart.vue";
import { colorShade } from "@/utils/functions";

const badges = ref([]);
const loaded = ref(false);
const patches = ref({});
const in_progress = ref([]);
const up_next = ref([]);
const shopping_list = ref([]);

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

async function fetchData() {
  const response = await fetch("http://127.0.0.1:5000/");
  const data_json = await response.json();
  const patchData = data_json["patches"];
  badges.value = data_json["badges"];
  loaded.value = true;

  patches.value = section_colours(patchData);
  in_progress.value = badges.value.filter((badge) => badge.complete === false);
  up_next.value = badges.value.filter((badge) => badge.is_next === true);
  shopping_list.value = badges.value.filter(
    (badge) => badge.complete === true && badge.is_purchased === false
  );
}

onMounted(async () => {
  await fetchData();
});
</script>

<template>
  <div class="row my-5">
    <div class="col-5">
      <BadgeChart v-if="loaded" :badges="badges" />
    </div>
    <div class="col">
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
    </div>
  </div>
  <div class="row">
    <div class="col d-flex justify-content-evenly">
      <div class="card w-25">
        <div class="card-header">In Progress</div>
        <ul class="list-group">
          <li v-for="badge in in_progress">{{ badge.name }}</li>
        </ul>
      </div>
      <div class="card w-25">
        <div class="card-header">Up Next</div>
        <ul class="list-group">
          <li v-for="badge in up_next">{{ badge.name }}</li>
        </ul>
      </div>
      <div class="card w-25">
        <div class="card-header">Shopping List</div>
        <ul class="list-group">
          <p class="fs-6">Badges which are completed but not purchased</p>
          <li v-for="badge in shopping_list">{{ badge.name }}</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<style scoped>
.section-square {
  height: 20px;
  width: 20px;
  margin: 10px;
}

.list-group {
  padding: 2rem;
}
</style>
