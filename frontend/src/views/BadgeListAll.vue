<script setup>
import { useBadgeStore } from "@/stores/BadgeStore";
import BadgeTable from "@/components/BadgeTable.vue";

const badgeStore = useBadgeStore();
</script>

<template>
  <badge-table :badges="badgeStore.badges" />
</template>
