<script setup>
import BaseCard from "../Base/BaseCard.vue";

const items = [
  { title: "Rating" },
  {
    title: "Complete",

    icon: "",
  },
  {
    title: "Tags",

    icon: "",
  },
];
</script>
<template>
  <BaseCard title="Details">
    <v-table>
      <tbody>
        <tr>
          <td>
            <v-icon icon="mdi-book-outline" size="large"></v-icon>
          </td>
          <td>Link</td>
          <td></td>
        </tr>
        <tr>
          <td><v-icon icon="mdi-chart-pie-outline" size="large"></v-icon></td>
          <td>Section</td>
          <td></td>
        </tr>
        <tr>
          <td>
            <v-icon icon="mdi-thumbs-up-down-outline" size="large"></v-icon>
          </td>
          <td>Rating</td>
          <td></td>
        </tr>
        <tr>
          <td><v-icon icon="mdi-check-outline" size="large"></v-icon></td>
          <td>Complete</td>
          <td></td>
        </tr>
        <tr>
          <td><v-icon icon="mdi-tag-outline" size="large"></v-icon></td>
          <td>Tags</td>
          <td></td>
        </tr>
        <tr>
          <td><v-icon icon="mdi-link-variant" size="large"></v-icon></td>
          <td>Link</td>
          <td></td>
        </tr>
      </tbody>
    </v-table>
  </BaseCard>
</template>
