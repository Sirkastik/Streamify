<template>
  <div class="container">
    <Navbar />
    <button @click="showPlayer" id="ellipsis">
      <i class="fas fa-ellipsis-h"></i>
    </button>
    <div class="content">
      <Player v-if="show" />
      <List v-if="appear"/>
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

  data() {
    return {
      show: true,
      appear: true,
    };
  },

  methods: {
    showPlayer() {
      this.show = !this.show;
      this.appear = !this.show;
    },
  },
};
</script>

<style>
#ellipsis {
  position: absolute;
  top: 12%;
  left: 3%;
  display: none;

  font-size: 0.8rem;
  border-radius: 5px;
  color: white;
  outline: none;
  border: none;
  padding: 5px 10px;
  margin: 8px;
  background: var(--main);
}

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
  width: 100vw;
  height: 100vh;
}

.content {
  display: flex;
  flex-wrap: wrap;
}

button {
  cursor: pointer;
}

/* media queries */

@media (max-width: 800px) {
  body {
    background: url(./assets/bg5.jpg) no-repeat;
    background-position: center;
    background-size: cover;
    background-attachment: fixed;
  }

  #ellipsis {
    display: block;
  }

}


</style>
