import { defineStore } from "pinia";

export const useBadgeStore = defineStore("badge", {
  state: () => ({
    badges: [],
    patchData: [],
    loading: false,
  }),
  getters: {
    sectionNames() {
      const allSections = this.badges.map((badge) => badge.section);
      return [...new Set(allSections)];
    },
    inProgress() {
      return this.badges.filter(
        (badge) => badge.complete === false && badge.is_started === true
      );
    },
    upNext() {
      return this.badges.filter((badge) => badge.is_next === true);
    },
    shoppingList() {
      return this.badges.filter(
        (badge) => badge.complete === true && badge.is_purchased !== true
      );
    },
  },
  actions: {
    async getBadges() {
      this.loading = true;
      const response = await fetch("http://127.0.0.1:5000/badges");
      this.badges = await response.json();
      this.loading = false;
    },

    async getPatchData() {
      const response = await fetch("http://127.0.0.1:5000/patches");
      const data_json = await response.json();
      this.patchData = data_json["patches"];
    },

    async getBadge(id) {
      const response = await fetch("http://127.0.0.1:5000/badge/" + id);
      const data = await response.json();
      return data;
    },
    async updateBadge(ev, field, id) {
      console.log(ev.target.value);
      console.log(field);
      console.log(id);

      let value = null;
      switch (field) {
        case "complete":
          value = ev.target.checked;
          break;
        case "rating":
        case "link":
        case "notes":
          value = ev.target.value;
          break;
      }

      const body = {
        id,
      };
      body[field] = value;
      console.log(body);
      fetch(`http://127.0.0.1:5000/badge/${id}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body),
      });
    },
  },
});
