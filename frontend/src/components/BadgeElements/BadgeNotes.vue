<script setup>
import { ref } from "vue";
const { value, id } = defineProps(["value", "id"]);
const textContent = ref(value);
import { useBadgeStore } from "@/stores/BadgeStore";

const badgeStore = useBadgeStore();
</script>
<template>
  <div class="notes-container">
    <v-textarea
      label="Notes"
      variant="outlined"
      v-model="textContent"
      @blur="(event) => badgeStore.updateBadge(event, 'notes', id)"
    />
  </div>
</template>

<style scoped>
.notes-container {
  padding: 2rem 0;
}
</style>
