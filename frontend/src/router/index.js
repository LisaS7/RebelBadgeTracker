import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import BadgeList from "@/views/BadgeListAll.vue";
import SectionDetails from "@/views/SectionDetails.vue";
import BadgeDetails from "@/views/BadgeDetails.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/badges/all",
      name: "badges_all",
      component: BadgeList,
    },
    {
      path: "/section/:name",
      name: "section",
      component: SectionDetails,
    },
    {
      path: "/badge/:id",
      name: "badge_detail",
      component: BadgeDetails,
    },
  ],
});

export default router;
