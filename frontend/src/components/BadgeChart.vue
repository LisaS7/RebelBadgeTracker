<template>
  <Doughnut :data="data" :options="options" />
</template>

<script setup>
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";
import { Doughnut } from "vue-chartjs";
import { colorShade } from "@/utils/functions";
import { SECTION_COLOURS } from "@/utils/constants";

const props = defineProps(["badges"]);

const labels = props.badges.map((badge) => badge.name);
const values = props.badges.map((badge) => 1);

const colours = [];
props.badges.forEach((badge) => {
  const colour = SECTION_COLOURS[badge.section];
  if (badge.complete === true) {
    colours.push(colour);
  } else {
    const darker = colorShade(colour, -150);
    colours.push(darker);
  }
});

const data = {
  labels: labels,
  datasets: [
    {
      backgroundColor: colours,
      data: values,
    },
  ],
};

const options = {
  responsive: true,
  maintainAspectRatio: false,
  elements: { arc: { borderWidth: 0 } },
  plugins: { legend: { display: false } },
};

ChartJS.register(ArcElement, Tooltip, Legend);
</script>
