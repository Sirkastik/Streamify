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
import Navbar from "./components/navbar";

import Player from "./components/Player";

import List from "./components/List";

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
  font-family: "Acme", sans-serif;
}

body {
  height: 100vh;
  width: 100vw;
  background: url(./assets/bg3.jpg) no-repeat;
  background-position: center;
  background-size: cover;
  background-attachment: fixed;
}

.container {
  display: grid;
  width: 100vw;
  height: 100vh;
}

.content {
  display: grid;
  width: 100%;
  grid-template-columns: 1fr 1.5fr;
}

button {
  cursor: pointer;
}

/* media queries*/

@media (max-width: 800px) {
  body {
    background: url(./assets/bg5.jpg) no-repeat;
    background-position: center;
    background-size: cover;
    background-attachment: fixed;
  }

  .content {
    display: flex;
    flex-direction: column;
  }

  .List {
    display: none;
  }

  #display {
    display: block;
  }
}
</style>
