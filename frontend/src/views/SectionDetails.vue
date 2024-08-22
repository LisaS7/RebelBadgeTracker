<script setup>
import { useRoute } from "vue-router";
import BaseHeading from "@/components/Base/BaseHeading.vue";
import BadgeTable from "@/components/BadgeTable.vue";

const route = useRoute();
const section = route.params.name;

const props = defineProps(["badges"]);
const sectionBadges = props.badges.filter((badge) => badge.section === section);
</script>
<template>
  <BaseHeading :text="section" />
  <BadgeTable :badges="sectionBadges" />
</template>

<style scoped>
.v-table {
  margin-top: 15rem;
}
</style>
