<script setup>
import { ref } from "vue";
import { parseISODate, dateToString } from "@/utils/functions";
const { current, id, type } = defineProps(["current", "id", "type"]);

const date = ref(parseISODate(current));
const showPicker = ref(false);

function changeDate(id, date) {
  const dateStr = date ? dateToString(date) : null;
  fetch(`http://127.0.0.1:5000/${type}/${id}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      id: id,
      date: dateStr,
    }),
  });
}

function clearDate(id) {
  date.value = null;
  changeDate(id, null);
}

function togglePicker() {
  showPicker.value = !showPicker.value;
}
</script>

<template>
  <span @click="togglePicker">
    <v-icon icon="mdi-calendar-range" size="large" />
    {{ date ? date.toDateString() : "Choose date" }}
  </span>
  <v-overlay v-model="showPicker" class="align-center justify-center">
    <v-date-picker
      v-if="showPicker"
      @click="changeDate(id, date)"
      v-model="date"
    />
  </v-overlay>
  <span class="mx-4">
    <v-tooltip text="Clear date">
      <template v-slot:activator="{ props }">
        <v-btn v-bind="props" @click="clearDate(id)"
          ><v-icon icon="mdi-close-box-outline"
        /></v-btn>
      </template>
    </v-tooltip>
  </span>
</template>

<style scoped></style>
