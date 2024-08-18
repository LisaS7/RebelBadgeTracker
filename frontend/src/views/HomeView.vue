<script setup>
import { ref, onMounted } from "vue";
import BadgeChart from "@/components/BadgeChart.vue";
import PatchChart from "@/components/PatchChart.vue";

const badges = ref([]);
const patchData = ref({});
const loaded = ref(false);
const in_progress = ref([]);
const up_next = ref([]);
const shopping_list = ref([]);

async function fetchData() {
  const response = await fetch("http://127.0.0.1:5000/");
  const data_json = await response.json();
  patchData.value = data_json["patches"];
  badges.value = data_json["badges"];
  loaded.value = true;

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
      <PatchChart v-if="loaded" :patchData="patchData" />
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
.list-group {
  padding: 2rem;
}
</style>
