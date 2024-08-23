<script setup>
import BaseCard from "../Base/BaseCard.vue";
import BadgeRating from "./BadgeRating.vue";
import Datepicker from "../UI/Datepicker.vue";
import BadgeTags from "./BadgeTags.vue";
import BadgeNotes from "./BadgeNotes.vue";
import { handleChange } from "@/utils/functions";

const { badge } = defineProps(["badge"]);
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
          <td><BadgeRating :id="badge.id" :current="badge.rating" /></td>
        </tr>
        <tr>
          <td><v-icon icon="mdi-check-outline" size="large"></v-icon></td>
          <td>Complete</td>
          <td class="d-flex flex-row align-items-center justify-content-start">
            <v-checkbox
              @change="handleChange($event, 'complete', badge.id)"
              v-model="badge.complete"
            ></v-checkbox>
            <Datepicker :id="badge.id" :current="badge.date" type="badge" />
          </td>
        </tr>
        <tr>
          <td><v-icon icon="mdi-tag-outline" size="large"></v-icon></td>
          <td>Tags</td>
          <td><BadgeTags :badge="badge" /></td>
        </tr>
        <tr>
          <td><v-icon icon="mdi-link-variant" size="large"></v-icon></td>
          <td>Link</td>
          <td>{{ badge.link }}</td>
        </tr>
        <tr>
          <td></td>
          <td></td>
          <td><BadgeNotes :id="badge.id" :value="badge.notes" /></td>
        </tr>
      </tbody>
    </v-table>
  </BaseCard>
</template>

<style scoped>
.v-checkbox {
  height: 110%;
  width: 3rem;
  margin-left: -10px;
}
</style>
