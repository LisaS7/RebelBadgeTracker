<script setup>
import { useRoute } from "vue-router";
import { ref, onMounted } from "vue";
import BaseHeading from "@/components/Base/BaseHeading.vue";
import BadgeIcon from "@/components/BadgeElements/BadgeIcon.vue";

const route = useRoute();
const id = parseInt(route.params.id);
const badge = ref({});
const clauses = ref([]);
const loaded = ref(false);

async function fetchBadge() {
  const response = await fetch("http://127.0.0.1:5000/badge/" + id);
  const data = await response.json();
  badge.value = data.badge;
  clauses.value = data.clauses;
  loaded.value = true;
}

onMounted(() => {
  fetchBadge();
});
</script>

<template>
  <BaseHeading v-if="loaded" :text="badge.name" :section="badge.section">
    <BadgeIcon
      v-if="loaded"
      :section="badge.section"
      :image="badge.image"
      size="lg"
    />
  </BaseHeading>
</template>
