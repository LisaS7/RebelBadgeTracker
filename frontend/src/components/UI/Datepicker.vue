<script setup>
import { ref } from "vue";
import { parseISODate } from "@/utils/functions";
const { current, id } = defineProps(["current", "id"]);

const date = ref(parseISODate(current));
const showPicker = ref(false);

function changeDate(id, date) {
  console.log(date);
}

function togglePicker() {
  showPicker.value = !showPicker.value;
}
</script>

<template>
  <span @click="togglePicker">
    <v-icon icon="mdi-calendar-range" size="large"></v-icon>
    {{ date ? date.toDateString() : "Choose date" }}
  </span>
  <v-overlay v-model="showPicker" class="align-center justify-center">
    <v-date-picker
      v-if="showPicker"
      @change="changeDate(id, date)"
      v-model="date"
    >
    </v-date-picker>
  </v-overlay>
</template>

<style scoped></style>
