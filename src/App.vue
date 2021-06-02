<template>
  <div class="container">
    <Navbar />
    <div class="content">
      <Player
        :songs="songs"
        :currentIndex="currentIndex"
        :progressTime="progressTime"
        :totalDuration="totalDuration"
        :isPlaying="isPlaying"
        :progressPercent="progressPercent"
        :index="currentIndex"
        @playPrev="prev"
        @playCurrent="play"
        @pauseCurrent="pause"
        @playNext="next"
        @likeCurrent="likeCurrent"
      />
      <!--@shuffleList="shuffle"-->

      <List
        :songs="songs"
        @sortSongs="sort"
        @playSong="setIndex"
        @likeSong="likeCurrent"
      />
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
          fav: true,
        },
        {
          songTitle: "Subeme La Radio",
          artistName: "Enrique Iglesias",
          src: require("./assets/audio (3).mp3"),
          songIndex: 2,
          fav: true,
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

      currentIndex: 0,

      current: {},

      totalDuration: "0:00",

      progressTime: "0:00",
      isPlaying: false,
      progressPercent: 0,
      currentTime: 0,

      player: new Audio(),

      az: true,
    };
  },

  methods: {
    play() {
      this.current = this.songs[this.currentIndex];
      this.player.src = this.current.src;
      this.player.play();
      this.player.currentTime = this.currentTime;
      this.updateInfo();
      this.checkEnd();
      this.isPlaying = true;
    },
    pause() {
      this.currentTime = this.player.currentTime;
      this.isPlaying = false;
      this.player.pause();
    },
    next() {
      this.currentIndex++;
      if (this.currentIndex > this.songs.length - 1) {
        this.currentIndex = 0;
      }

      this.player.src = this.songs[this.currentIndex].src;
      this.player.play();
      this.updateInfo();
      this.checkEnd();
      this.isPlaying = true;
    },
    prev() {
      this.currentIndex--;
      if (this.currentIndex < 0) {
        this.currentIndex = this.songs.length - 1;
      }

      this.player.src = this.songs[this.currentIndex].src;
      this.player.play();
      this.updateInfo();
      this.checkEnd();
      this.isPlaying = true;
    },

    likeCurrent(index) {
      if (index) {
        console.log(index);
        this.songs[index].fav = !this.songs[index].fav;
      } else {
        this.songs[this.currentIndex].fav = !this.songs[this.currentIndex].fav;
      }
    },

    formatTime(time) {
      var mins = ~~((time % 3600) / 60);
      var secs = ~~time % 60;
      var result = "";
      result += "" + mins + ":" + (secs < 10 ? "0" : "");
      result += "" + secs;
      return result;
    },

    checkEnd() {
      this.player.addEventListener(
        "ended",
        function () {
          this.currentIndex++;
          if (this.currentIndex > this.songs.length - 1) {
            this.currentIndex = 0;
          }

          this.current = this.songs[this.currentIndex];
          this.player.src = this.current.src;
          this.player.play();
          this.isPlaying = true;
        }.bind(this)
      );
    },

    updateInfo() {
      this.player.addEventListener(
        "timeupdate",
        function () {
          this.progressPercent =
            (this.player.currentTime / this.player.duration) * 100;
          const progress = document.querySelector("#progress");
          progress.style.width = `${this.progressPercent}%`;

          this.progressTime = this.formatTime(this.player.currentTime);
        }.bind(this)
      );

      this.player.addEventListener(
        "canplay",
        function () {
          this.totalDuration = this.formatTime(this.player.duration);
        }.bind(this)
      );
    },

    sort() {
      if (this.az == true) {
        this.songs.sort((a, b) => {
          let small_a = a.songTitle.toLowerCase(),
            small_b = b.songTitle.toLowerCase();
          this.az = false;

          if (small_a < small_b) {
            return -1;
          }
          if (small_a > small_b) {
            return 1;
          }
          return 0;
        });
      } else {
        this.songs.sort((a, b) => {
          let small_a = a.artistName.toLowerCase(),
            small_b = b.artistName.toLowerCase();
          this.az = true;

          if (small_a < small_b) {
            return -1;
          }
          if (small_a > small_b) {
            return 1;
          }
          return 0;
        });
      }
    },

    setIndex(index) {
      if (index == this.currentIndex) {
        if (this.isPlaying == true) {
          this.pause();
        } else {
          this.play();
        }
      } else {
        this.currentIndex = index;
        this.current = this.songs[index];
        this.player.src = this.current.src;
        this.player.play();
        this.isPlaying = true;
      }
    },
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