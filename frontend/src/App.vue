<script setup>
import { ref, onMounted } from "vue";
import { RouterView } from "vue-router";
import Navbar from "./components/Navbar.vue";

const badges = ref([]);
const sections = ref([]);
const loaded = ref(false);

async function fetchBadges() {
  const response = await fetch("http://127.0.0.1:5000/badges");
  const data = await response.json();
  badges.value = data;
  loaded.value = true;
}

onMounted(() => {
  fetchBadges().then(() => {
    const section_data = badges.value.map((badge) => badge.section);
    sections.value = [...new Set(section_data)];
  });
});
</script>

<template>
  <Navbar v-if="loaded" />
  <RouterView v-if="loaded" :badges="badges" />
</template>

<style scoped></style>
