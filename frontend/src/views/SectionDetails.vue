<script setup>
import { useRoute } from "vue-router";
import BaseHeading from "@/components/Base/BaseHeading.vue";

const route = useRoute();
const section = route.params.name;
</script>
<template>
  <BaseHeading :text="section" />
</template>
