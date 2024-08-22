<script setup>
import BaseCard from "../Base/BaseCard.vue";
const { badge } = defineProps(["badge"]);

function handleChange(ev, field, id) {
  let value = null;
  switch (field) {
    case "complete":
      value = ev.target.checked;
      break;
  }
  fetch(`http://127.0.0.1:5000/badge/${id}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      id: id,
      field: value,
    }),
  });
}
</script>
<template>
  <BaseCard title="Details">
    <v-table>
      <tbody>
        <tr>
          <td>
            <v-icon icon="mdi-book-outline" size="large"></v-icon>
          </td>
          <td>Book</td>
          <td>{{ badge.book }}</td>
        </tr>
        <tr>
          <td><v-icon icon="mdi-chart-pie-outline" size="large"></v-icon></td>
          <td>Section</td>
          <td>{{ badge.section }}</td>
        </tr>
        <tr>
          <td>
            <v-icon icon="mdi-thumbs-up-down-outline" size="large"></v-icon>
          </td>
          <td>Rating</td>
          <td>{{ badge.rating }}</td>
        </tr>
        <tr>
          <td><v-icon icon="mdi-check-outline" size="large"></v-icon></td>
          <td>Complete</td>
          <td>
            {{ badge.complete
            }}<v-checkbox
              @change="handleChange($event, 'complete', badge.id)"
            ></v-checkbox>
          </td>
        </tr>
        <tr>
          <td><v-icon icon="mdi-tag-outline" size="large"></v-icon></td>
          <td>Tags</td>
          <td></td>
        </tr>
        <tr>
          <td><v-icon icon="mdi-link-variant" size="large"></v-icon></td>
          <td>Link</td>
          <td>{{ badge.link }}</td>
        </tr>
      </tbody>
    </v-table>
  </BaseCard>
</template>

<style scoped>
.v-checkbox {
  height: 110%;
}
</style>
