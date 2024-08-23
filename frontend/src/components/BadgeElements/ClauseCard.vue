<script setup>
import BaseCard from "../Base/BaseCard.vue";
import Datepicker from "../UI/Datepicker.vue";

const { clauses } = defineProps(["clauses"]);

function handleChange(id, type, newValue) {
  console.log(id);
  console.log(type);
  console.log(newValue);

  const body = {
    id,
  };
  body[type] = newValue;

  fetch(`http://127.0.0.1:5000/clause/${id}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
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
              @change="handleChange(clause.id, 'complete', clause.complete)"
              v-model="clause.complete"
            ></v-checkbox>
          </td>
          <td>{{ clause.description }}</td>
          <td>
            {{ clause.date }}
            <Datepicker :id="clause.id" :current="clause.date" type="clause" />
          </td>
        </tr>
      </tbody>
    </v-table>
  </BaseCard>
</template>
