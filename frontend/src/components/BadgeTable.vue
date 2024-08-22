<script setup>
import BadgeIcon from "@/components/BadgeElements/BadgeIcon.vue";
import BadgeProgress from "@/components/BadgeElements/BadgeProgress.vue";
import BadgeRating from "@/components/BadgeElements/BadgeRating.vue";

const props = defineProps(["badges"]);
const headers = [
  { title: "icon", value: "image" },
  { title: "Name", value: "name", sortable: true },
  { title: "Progress", value: "progress", sortable: true },
  { title: "Rating", value: "rating", sortable: true },
  { title: "Notes", value: "notes" },
  { title: "Tags" },
];
</script>

<template>
  <v-data-table :headers="headers" :items="props.badges">
    <template v-slot:item.image="{ item }">
      <badge-icon :colour="item.colour" :image="item.image" />
    </template>
    <template v-slot:item.progress="{ item }">
      <badge-progress :progress="item.progress" />
    </template>
    <template v-slot:item.rating="{ item }">
      <badge-rating :current="item.rating" :id="item.id" />
    </template>
    <template v-slot:item.tags="{ item }">
      <span v-if="item.is_next" class="badge rounded-pill bg-light text-dark"
        >Next</span
      >
      <span v-if="item.complete" class="badge rounded-pill bg-light text-dark"
        >Complete</span
      >
    </template>
  </v-data-table>
</template>

<style scoped>
.table-container {
  margin: 5rem;
}
</style>
