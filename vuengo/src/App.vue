<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <a href="http://127.0.0.1:8000/">Add</a>
  </nav>
  <router-view/>
</template>

<style lang="scss">
* {margin: 0; padding: 0; box-sizing: border-box;}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 10px;
  background-color: #0f1113;
  margin: 0%;

  a {
    font-weight: bold;
    color: #a0a0a0;

    &.router-link-exact-active {
      color: #fff;
    }
  }
}
</style>
