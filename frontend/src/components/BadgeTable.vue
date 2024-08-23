<script setup>
import { ref } from "vue";
import BadgeIcon from "@/components/BadgeElements/BadgeIcon.vue";
import BadgeNameButton from "./BadgeElements/BadgeNameButton.vue";
import BadgeProgress from "@/components/BadgeElements/BadgeProgress.vue";
import BadgeRating from "@/components/BadgeElements/BadgeRating.vue";

const search = ref("");
const props = defineProps(["badges"]);
const headers = [
  { title: "", value: "image" },
  { title: "Name", value: "name", sortable: true },
  { title: "Progress", value: "progress", sortable: true },
  { title: "Rating", value: "rating", sortable: true },
  { title: "Notes", value: "notes" },
  { title: "Tags", value: "tags" },
];
</script>

<template>
  <v-card>
    <template v-slot:text>
      <v-text-field
        v-model="search"
        label="Search"
        prepend-inner-icon="mdi-magnify"
        variant="outlined"
        hide-details
        single-line
      ></v-text-field>
    </template>

    <v-data-table
      :headers="headers"
      :items="props.badges"
      :items-per-page="25"
      :search="search"
    >
      <template v-slot:item.image="{ item }">
        <badge-icon :section="item.section" :image="item.image" size="sm" />
      </template>
      <template v-slot:item.name="{ item }">
        <BadgeNameButton :id="item.id" :name="item.name" />
      </template>
      <template v-slot:item.progress="{ item }">
        <badge-progress :progress="item.progress" />
      </template>
      <template v-slot:item.rating="{ item }">
        <badge-rating :current="item.rating" :id="item.id" />
      </template>
      <template v-slot:item.tags="{ item }">
        <v-chip v-if="item.is_started">Started</v-chip>
        <v-chip v-if="item.is_next">Next</v-chip>
        <v-chip v-if="item.is_purchased">Purchased</v-chip>
      </template>
    </v-data-table>
  </v-card>
</template>

<style scoped>
.table-container {
  margin: 5rem;
}

.v-text-field {
  width: 25%;
}
</style>
