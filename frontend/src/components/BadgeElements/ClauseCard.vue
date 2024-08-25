<script setup>
import { ref, onMounted } from "vue";
import BaseCard from "../Base/BaseCard.vue";
import Datepicker from "../UI/Datepicker.vue";

const props = defineProps(["clauses"]);
const clauses = ref(props.clauses);

function clauseComplete(clause) {
  fetch(`http://127.0.0.1:5000/clause/${clause.id}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      id: clause.id,
      complete: clause.complete,
    }),
  });
}
</script>
<template>
  <BaseCard title="Clauses">
    <v-table>
      <tbody>
        <tr v-for="clause in clauses" :key="clause.id">
          <td>
            <v-checkbox
              @change="clauseComplete(clause)"
              @click="$emit('clauseComplete', !clause.complete, clause.factor)"
              v-model="clause.complete"
            ></v-checkbox>
          </td>
          <td>{{ clause.description }}</td>
          <td>
            <Datepicker :id="clause.id" :current="clause.date" type="clause" />
          </td>
        </tr>
      </tbody>
    </v-table>
  </BaseCard>
</template>
