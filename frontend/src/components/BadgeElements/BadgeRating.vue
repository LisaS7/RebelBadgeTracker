<script setup>
import { useBadgeStore } from "@/stores/BadgeStore";
import { ref } from "vue";
const ratings = ref(["None", "✖️", "🟢", "🟡", "🟠", "🔴"]);
const props = defineProps(["current", "id"]);
const current = ref(props.current);
const selected = ref(current);

const badgeStore = useBadgeStore();
</script>

<template>
  <select
    label="Select"
    @change="(event) => badgeStore.updateBadge(event, 'rating', props.id)"
    v-model="selected"
  >
    <option v-for="rating in ratings" :value="rating">{{ rating }}</option>
  </select>
</template>
