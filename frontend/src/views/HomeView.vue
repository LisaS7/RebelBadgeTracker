<script setup>
import { ref, onMounted } from "vue";
import BadgeChart from "@/components/Chart.vue";

const badges = ref([]);
const loaded = ref(false);

async function fetchData() {
  const response = await fetch("http://127.0.0.1:5000/badges");
  const data_json = await response.json();
  badges.value = await data_json;
  loaded.value = true;
  console.log("loaded");
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
    </div>
  </div>
  <div class="row">
    <div class="col d-flex justify-content-evenly">
      <div class="card">
        <div class="card-header">In Progress</div>
        <ul class="list-group"></ul>
      </div>
      <div class="card">
        <div class="card-header">Up Next</div>
        <ul class="list-group"></ul>
      </div>
      <div class="card">
        <div class="card-header">Shopping List</div>
        <ul class="list-group">
          <p class="fs-6">Badges which are completed but not purchased</p>
        </ul>
      </div>
    </div>
  </div>
</template>
