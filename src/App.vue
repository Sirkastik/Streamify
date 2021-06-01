<template>
  <div class="container">
    <Navbar />
    <div class="content">
      <Player />
      <List />
    </div>
  </div>
</template>

<script>
import Navbar from "./components/Navbar";

import Player from "./components/PlayerDiv";

import List from "./components/MusicList";

export default {
  name: "App",
  components: {
    Navbar,
    Player,
    List,
  },
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Acme&display=swap");
* {
  --main: #011b26ab;
  --shadow: 1px 1px 3px 1px hsla(0, 0%, 0%, 0.473);
  --accent: #fe4f46;
  --darker: #011b26;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Acme", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
}

body {
  height: 100vh;
  width: 100vw;
  background: url(./assets/bg3.jpg) no-repeat;
  background-position: center;
  background-size: cover;
  background-attachment: fixed;
  overflow: auto;
}

.container {
  height: 100vh;
  width: 100vw;
  overflow: auto;
}

.content {
  display: flex;
  flex-wrap: wrap;
}

/* media queries */

@media (max-width: 800px) {
  body {
    background: url(./assets/bg5.jpg) no-repeat;
    background-position: center;
    background-size: cover;
    background-attachment: fixed;
  }
}
</style>