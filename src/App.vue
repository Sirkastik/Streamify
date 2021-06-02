<template>
  <div class="container">
    <Navbar />
    <div class="content">
      <Player 
      :songs="songs"
      />
      <List :songs="songs" />
    </div>
  </div>
</template>

<script>
import Navbar from "./components/Navbar";

import Player from "./components/PlayerDiv";

import List from "./components/MusicList";

export default {
  name: "App",

  /* components */
  components: {
    Navbar,
    Player,
    List,
  },

  data() {
    return {
      currentIndex: 0,

      songs: [
        {
          songTitle: "Alarm",
          artistName: "Anne Marie",
          src: require("./assets/audio (1).mp3"),
          songIndex: 0,
          fav: true,
        },
        {
          songTitle: "Hold On",
          artistName: "Chord Overstreet",
          src: require("./assets/audio (2).mp3"),
          songIndex: 1,
          fav: false,
        },
        {
          songTitle: "Subeme La Radio",
          artistName: "Enrique Iglesias",
          src: require("./assets/audio (3).mp3"),
          songIndex: 2,
          fav: false,
        },
        {
          songTitle: "Mi Gente",
          artistName: "J Balvin_ Willy William",
          src: require("./assets/audio (4).mp3"),
          songIndex: 3,
          fav: false,
        },
        {
          songTitle: "If the World was Ending",
          artistName: "JP Saxe",
          src: require("./assets/audio (5).mp3"),
          songIndex: 4,
          fav: false,
        },
        {
          songTitle: "You Say",
          artistName: "Lauren Daigle",
          src: require("./assets/audio (6).mp3"),
          songIndex: 5,
          fav: false,
        },
        {
          songTitle: "Maybe Don't",
          artistName: "Maisie Peters ft JP Saxe",
          src: require("./assets/audio (7).mp3"),
          songIndex: 6,
          fav: false,
        },
        {
          songTitle: "Care For You",
          artistName: "Mario",
          src: require("./assets/audio (8).mp3"),
          songIndex: 7,
          fav: false,
        },
        {
          songTitle: "Scared To Be Lonely",
          artistName: "Martin Garrix_Dua Lipa",
          src: require("./assets/audio (9).mp3"),
          songIndex: 8,
          fav: false,
        },
        {
          songTitle: "Perfect",
          artistName: "Ed Sheeran",
          src: require("./assets/audio (10).mp3"),
          songIndex: 9,
          fav: false,
        },
        {
          songTitle: "Let Me Live",
          artistName: "Rudimental_Major Lazer ft Anne Marie",
          src: require("./assets/audio (11).mp3"),
          songIndex: 10,
          fav: false,
        },
        {
          songTitle: "Fire on fire",
          artistName: "Sam Smith",
          src: require("./assets/audio (12).mp3"),
          songIndex: 11,
          fav: false,
        },
        {
          songTitle: "Snowman",
          artistName: "Sia",
          src: require("./assets/audio (13).mp3"),
          songIndex: 12,
          fav: true,
        },
      ],
    };
  },   

};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Acme&display=swap");

/* global styles */
* {
  --main: #011b26ab;
  --shadow: 1px 1px 3px 1px hsla(0, 0%, 0%, 0.473);
  --accent: #fe4f46;
  --darker: #011b26;
  --gradient: radial-gradient(
    circle,
    rgba(255, 255, 255, 1) 0%,
    rgba(254, 79, 70, 1) 100%
  );
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: "Acme", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  scroll-behavior: smooth;
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
  /* changing background */
  body {
    background: url(./assets/bg5.jpg) no-repeat;
    background-position: center;
    background-size: cover;
    background-attachment: fixed;
  }
}
</style>