<script setup>
import { useRoute } from "vue-router";
import { ref, onMounted } from "vue";
import BaseHeading from "@/components/Base/BaseHeading.vue";
import BadgeIcon from "@/components/BadgeElements/BadgeIcon.vue";
import BadgeProgress from "@/components/BadgeElements/BadgeProgress.vue";
import BadgeCard from "@/components/BadgeElements/BadgeCard.vue";
import ClauseCard from "@/components/BadgeElements/ClauseCard.vue";

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
  <div class="progress-container">
    <BadgeProgress :progress="badge.progress" />
  </div>
  <div class="row">
    <BadgeCard :badge="badge"></BadgeCard>
    <ClauseCard></ClauseCard>
  </div>
</template>

<style scoped>
.progress-container {
  margin-top: 15rem;
  margin-left: 3rem;
  width: 25%;
}
</style>
