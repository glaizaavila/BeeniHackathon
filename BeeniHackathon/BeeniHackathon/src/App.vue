<template>
  <div>
    <h1 class="green">Hello! </h1>
  </div>
  <br />
  <div>
    <RouterLink to="/create" id="candidateCreate">Create Candidate</RouterLink>
    <RouterLink to="/list" id="candidateList">View Candidate List</RouterLink>
  </div>
  <br />
  <main>
    <!-- <RouterView @route-change="handleRouteChange"/> -->
    <RouterView />
  </main>
</template>

<script>
// import { ref } from 'vue';
// import { useRoute } from 'vue-router';

// const isMainVisible = ref(false);
// const route = useRoute();

// const handleRouteChange = () => {
//   if (route.path === '/create' || route.path === '/list') {
//     isMainVisible.value = true;
//   } else {
//     isMainVisible.value = false;
//   }
// };

// handleRouteChange();
</script>

<style scoped>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 20px;
}

body {
  margin: 0;
  background: #eee;
}

header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
