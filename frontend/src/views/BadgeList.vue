<script setup>
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
      <div
        class="badge-icon"
        :style="`background:${item.colour}`"
        v-html="`${item.image}`"
      ></div>
    </template>
    <template v-slot:item.progress="{ item }">
      <v-progress-linear :model-value="`${item.progress}`" :height="20" rounded
        ><template v-slot:default="{ value }">
          <strong style="color: black">{{ Math.ceil(value) }}%</strong>
        </template>
      </v-progress-linear>
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

.badge-icon {
  width: 40px;
  height: 40px;
  padding: 8px;
  border-radius: 50%;
}
</style>
