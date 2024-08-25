<script setup>
import { useBadgeStore } from "@/stores/BadgeStore";
import { useRoute } from "vue-router";
import BadgeTable from "@/components/BadgeTable.vue";

const badgeStore = useBadgeStore();
const route = useRoute();
const section = route.params.name;

const sectionBadges = badgeStore.badges.filter(
  (badge) => badge.section === section
);
</script>
<template>
  <BadgeTable :badges="sectionBadges" />
</template>
