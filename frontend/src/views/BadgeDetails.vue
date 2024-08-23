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
const progress = ref(0);
const clauses_complete = ref(0);

async function fetchBadge() {
  const response = await fetch("http://127.0.0.1:5000/badge/" + id);
  const data = await response.json();
  badge.value = data.badge;
  clauses.value = data.clauses;
  loaded.value = true;
}

function calcProgress() {
  progress.value =
    (clauses_complete.value / badge.value.clauses_required) * 100;
}

onMounted(() => {
  fetchBadge().then(() => {
    clauses_complete.value = clauses.value.filter(
      (clause) => clause.complete
    ).length;
    calcProgress();
  });
});

function updateProgress(value) {
  if (value === true) {
    clauses_complete.value++;
  } else {
    clauses_complete.value--;
  }

  calcProgress();
}
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
    <BadgeProgress :progress="progress" />
  </div>
  <div class="row">
    <BadgeCard v-if="loaded" :badge="badge"></BadgeCard>
    <ClauseCard
      v-if="loaded"
      :clauses="clauses"
      @clauseComplete="updateProgress"
    ></ClauseCard>
  </div>
</template>

<style scoped>
.progress-container {
  margin-top: 15rem;
  margin-left: 3rem;
  width: 25%;
}
</style>
