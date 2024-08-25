<script setup>
import { useBadgeStore } from "@/stores/BadgeStore";
import { RouterView } from "vue-router";
import Navbar from "./components/UI/TheNavbar.vue";

const badgeStore = useBadgeStore();
badgeStore.getBadges();
</script>

<template>
  <Navbar :sections="badgeStore.sectionNames" />
  <RouterView v-if="badgeStore.loading === false" />
</template>

<style scoped></style>
