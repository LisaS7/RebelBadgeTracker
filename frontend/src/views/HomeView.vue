<script setup>
import { useBadgeStore } from "@/stores/BadgeStore";
import BadgeChart from "@/components/BadgeChart.vue";
import PatchChart from "@/components/PatchChart.vue";

const badgeStore = useBadgeStore();
</script>

<template>
  <div class="row chart-container">
    <div class="col-5">
      <BadgeChart :badges="badgeStore.badges" />
    </div>
    <div class="col">
      <PatchChart />
    </div>
  </div>
  <div class="row">
    <div class="col d-flex justify-content-evenly">
      <div class="card w-25">
        <div class="card-header">In Progress</div>
        <ul class="list-group">
          <li v-for="badge in badgeStore.inProgress">{{ badge.name }}</li>
        </ul>
      </div>
      <div class="card w-25">
        <div class="card-header">Up Next</div>
        <ul class="list-group">
          <li v-for="badge in badgeStore.upNext">{{ badge.name }}</li>
        </ul>
      </div>
      <div class="card w-25">
        <div class="card-header">Shopping List</div>
        <ul class="list-group">
          <p class="fs-6">Badges which are completed but not purchased</p>
          <li v-for="badge in badgeStore.shoppingList">{{ badge.name }}</li>
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
