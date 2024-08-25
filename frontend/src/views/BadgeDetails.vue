<script setup>
import { useRoute } from "vue-router";
import { useBadgeStore } from "@/stores/BadgeStore";
import { ref } from "vue";
import BaseHeading from "@/components/Base/BaseHeading.vue";
import BadgeIcon from "@/components/BadgeElements/BadgeIcon.vue";
import BadgeProgress from "@/components/BadgeElements/BadgeProgress.vue";
import BadgeCard from "@/components/BadgeElements/BadgeCard.vue";
import ClauseCard from "@/components/BadgeElements/ClauseCard.vue";

const badgeStore = useBadgeStore();
const route = useRoute();
const id = parseInt(route.params.id);

const badge = badgeStore.badges.find((badge) => badge.id === id);
let clauses_complete = ref(
  badge.clauses.filter((clause) => clause.complete).length
);

function updateProgress(value, factor) {
  if (value === true) {
    clauses_complete.value + factor;
  } else {
    clauses_complete.value - factor;
  }

  badge.progress = (clauses_complete.value / badge.clauses_required) * 100;
}
</script>

<template>
  <BaseHeading :text="badge.name" :section="badge.section">
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
    <BadgeCard :badge="badge" />
    <ClauseCard :clauses="badge.clauses" @clauseComplete="updateProgress" />
  </div>
</template>

<style scoped>
.progress-container {
  margin-top: 15rem;
  margin-left: 3rem;
  width: 25%;
}
</style>
