<script setup>
import { ref, onMounted } from "vue";
import BadgeChart from "@/components/BadgeChart.vue";
import PatchChart from "@/components/PatchChart.vue";

const props = defineProps(["badges"]);

let in_progress = ref([]);
const up_next = ref([]);
const shopping_list = ref([]);

onMounted(async () => {
  in_progress.value = props.badges.filter((badge) => badge.complete === false);
  up_next.value = props.badges.filter((badge) => badge.is_next === true);
  shopping_list.value = props.badges.filter(
    (badge) => badge.complete === true && badge.is_purchased !== true
  );
});
</script>

<template>
  <div class="row chart-container">
    <div class="col-5">
      <BadgeChart :badges="badges" />
    </div>
    <div class="col">
      <PatchChart />
    </div>
  </div>
  <div v-if="badges" class="row">
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
.chart-container {
  margin: 5rem 0;
}

.list-group {
  padding: 2rem;
}
</style>
