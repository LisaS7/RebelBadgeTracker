<script setup>
import { RouterLink } from "vue-router";
const { sections } = defineProps(["sections"]);
</script>

<template>
  <nav class="navbar navbar-expand-lg navbar-dark sticky-top">
    <a class="navbar-brand" href="https://www.rebelbadgestore.com/"
      ><img src="@/assets/images/RebelLogo.svg"
    /></a>
    <button
      class="navbar-toggler"
      type="button"
      data-toggle="collapse"
      data-target="#navbarSupportedContent"
      aria-controls="navbarSupportedContent"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li id="nav-home" class="nav-item">
          <RouterLink to="/">
            <img src="@/assets/icons/home.svg" title="Home" />
          </RouterLink>
        </li>
        <li id="nav-all" class="nav-item">
          <RouterLink to="/badges/all">
            <img src="@/assets/icons/all_badges.svg" title="View All Badges" />
          </RouterLink>
        </li>

        <li id="nav-section" class="nav-item dropdown">
          <a
            class="nav-link dropdown-toggle"
            href="#"
            id="navbarDropdownSection"
            role="button"
            data-bs-toggle="dropdown"
            aria-haspopup="true"
            aria-expanded="false"
          >
            <img src="@/assets/icons/section.svg" title="Sections" />
          </a>
          <div class="dropdown-menu" aria-labelledby="navbarDropdown">
            <a
              v-for="section in sections"
              class="dropdown-item"
              :href="`/section/${section}`"
              >{{ section }}</a
            >
          </div>
        </li>
      </ul>
    </div>
  </nav>
</template>

<style scoped>
nav {
  background: var(--rebel-dark-teal);
  gap: 4rem;
}

nav ul {
  gap: 3rem;
  position: relative;
}

nav > .navbar-brand > img {
  margin-left: 6rem;
  width: 6rem;
}

.nav-item > a > img {
  width: 2rem;
}
</style>
