<script setup>
import { ref } from "vue";
import BadgeIcon from "@/components/BadgeElements/BadgeIcon.vue";
import BadgeNameButton from "./BadgeElements/BadgeNameButton.vue";
import BadgeProgress from "@/components/BadgeElements/BadgeProgress.vue";
import BadgeRating from "@/components/BadgeElements/BadgeRating.vue";

const search = ref("");
const ratingFilter = ref([]);
const tagFilter = ref([]);
const props = defineProps(["badges"]);
const badges = ref(props.badges);
const headers = [
  { title: "", value: "image" },
  { title: "Name", value: "name", sortable: true },
  { title: "Progress", value: "progress", sortable: true },
  { title: "Rating", value: "rating", sortable: true },
  { title: "Notes", value: "notes" },
  { title: "Tags", value: "tags" },
];

function toggleRating() {
  const ratingFiltersCount = ratingFilter.value.length;
  if (ratingFiltersCount === 0) {
    badges.value = props.badges;
  } else {
    badges.value = props.badges.filter((item) =>
      ratingFilter.value.includes(item.rating)
    );
  }
}

function toggleTags(ev) {
  console.log(ev);
  ratingFilter.value = [];
  if (tagFilter.value.length === 0) {
    badges.value = props.badges;
  }
  if (tagFilter.value.includes("started")) {
    badges.value = props.badges.filter((item) => item.is_started);
    tagFilter.value = [];
  }
  if (tagFilter.value.includes("next")) {
    badges.value = props.badges.filter((item) => item.is_next);
    tagFilter.value = [];
  }
  if (tagFilter.value.includes("purchased")) {
    badges.value = props.badges.filter((item) => item.is_purchased);
    tagFilter.value = [];
  }
}
</script>

<template>
  <v-card class="d-flex flex-row justify-content-evenly">
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
  </v-card>
  <v-row class="justify-end filter-container">
    <v-col class="v-col-3"
      ><p>Filter rating</p>
      <v-btn-toggle
        v-model="ratingFilter"
        background-color="primary"
        dark
        multiple
        @update:modelValue="toggleRating"
      >
        <v-btn value="✖️"> ✖️ </v-btn>
        <v-btn value="🟢"> 🟢 </v-btn>
        <v-btn value="🟡"> 🟡 </v-btn>
        <v-btn value="🟠"> 🟠 </v-btn>
        <v-btn value="🔴"> 🔴 </v-btn>
      </v-btn-toggle></v-col
    >
    <v-col class="v-col-3"
      ><p>Filter Tags</p>
      <v-btn-toggle
        v-model="tagFilter"
        background-color="primary"
        dark
        multiple
        @update:modelValue="toggleTags"
      >
        <v-btn value="started"> Started </v-btn>
        <v-btn value="next"> Next </v-btn>
        <v-btn value="purchased"> Purchased </v-btn>
      </v-btn-toggle></v-col
    >
  </v-row>
  <v-data-table
    :headers="headers"
    :items="badges"
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
</template>

<style scoped>
.table-container {
  margin: 5rem;
}

.v-text-field {
  width: 25%;
}

.filter-container {
  background: #212121;
}
</style>
