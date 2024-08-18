<script setup>
const props = defineProps(["badges"]);
const headers = [
  { title: "icon", value: "image" },
  { title: "Name", value: "name", sortable: true },
  { title: "Progress", value: "progress", sortable: true },
  { title: "Rating", value: "rating", sortable: true },
  { title: "Notes", value: "notes" },
];
</script>

<template>
  <v-data-table :headers="headers" :items="props.badges">
    <template v-slot:item.image="{ item }">
      <div
        class="badge-icon"
        :style="`fill:${item.colour}`"
        v-html="`${item.image}`"
      ></div>
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
}
</style>
