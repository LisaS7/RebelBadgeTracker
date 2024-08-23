<script setup>
import { ref } from "vue";
const { badge } = defineProps(["badge"]);

const status = ref({
  is_started: badge.is_started,
  is_next: badge.is_next,
  is_purchased: badge.is_purchased,
});

function toggleChip(id, name) {
  const body = { id };

  if (status.value[name] === true) {
    body[name] = false;
  } else {
    body[name] = true;
  }

  fetch(`http://127.0.0.1:5000/badge/${id}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  status.value[name] = !status.value[name];
}
</script>
<template>
  <div class="chip-container">
    <v-chip
      :class="status.is_started ? 'active' : ''"
      @click="toggleChip(badge.id, 'is_started')"
    >
      Started </v-chip
    ><v-chip
      :class="status.is_next ? 'active' : ''"
      @click="toggleChip(badge.id, 'is_next')"
    >
      Next </v-chip
    ><v-chip
      :class="status.is_purchased ? 'active' : ''"
      @click="toggleChip(badge.id, 'is_purchased')"
    >
      Purchased
    </v-chip>
  </div>
</template>

<style scoped>
.chip-container {
  display: flex;
  gap: 20px;
}

.active {
  background: var(--rebel-dark-teal);
}
</style>
