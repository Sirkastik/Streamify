<template>
  <div class="player">
    <div class="info">
      <h3 id="songTitle">{{ songs[index].songTitle }}</h3>
      <h4 id="artistName">{{ songs[index].artistName }}</h4>
    </div>
    <div class="coverImg"></div>
    <div id="progressBar">
      <div id="progress"></div>
    </div>

    <div id="controls">
      <Btn id="shuffle">
        <i class="fas fa-random"></i>
      </Btn>
      <Btn id="prev" @click="prev">
        <i class="fas fa-step-backward"></i>
      </Btn>
      <Btn id="play" @click="play" v-if="!isPlaying">
        <i class="fas fa-play"></i>
      </Btn>
      <Btn id="pause" @click="pause" v-if="isPlaying">
        <i class="fas fa-pause"></i>
      </Btn>
      <Btn id="next" @click="next">
        <i class="fas fa-step-forward"></i>
      </Btn>
      <Btn id="fav">
        <i class="fas fa-heart"></i>
      </Btn>
    </div>
  </div>
</template>

<script>
import Btn from "./Btn";

export default {
  name: "PlayerDiv",
  components: {
    Btn,
  },

  data() {
    return {
      current: {},

      currentTime: 0,

      isPlaying: false,

      index: 0,

      progressPercent: 0,

      songs: [
        {
          songTitle: "Alarm",
          artistName: "Anne Marie",
          src: require("../assets/audio (1).mp3"),
        },
        {
          songTitle: "Hold On",
          artistName: "Chord Overstreet",
          src: require("../assets/audio (2).mp3"),
        },
        {
          songTitle: "Subeme La Radio",
          artistName: "Enrique Iglesias",
          src: require("../assets/audio (3).mp3"),
        },
        {
          songTitle: "Mi Gente",
          artistName: "J Balvin_ Willy William",
          src: require("../assets/audio (4).mp3"),
        },
        {
          songTitle: "If the World was Ending",
          artistName: "JP Saxe",
          src: require("../assets/audio (5).mp3"),
        },
        {
          songTitle: "You Say",
          artistName: "Lauren Daigle",
          src: require("../assets/audio (6).mp3"),
        },
        {
          songTitle: "Maybe Don't",
          artistName: "Maisie Peters ft JP Saxe",
          src: require("../assets/audio (7).mp3"),
        },
        {
          songTitle: "Care For You",
          artistName: "Mario",
          src: require("../assets/audio (8).mp3"),
        },
        {
          songTitle: "Scared To Be Lonely",
          artistName: "Martin Garrix_Dua Lipa",
          src: require("../assets/audio (9).mp3"),
        },
        {
          songTitle: "Perfect",
          artistName: "Ed Sheeran",
          src: require("../assets/audio (10).mp3"),
        },
        {
          songTitle: "Let Me Live",
          artistName: "Rudimental_Major Lazer ft Anne Marie",
          src: require("../assets/audio (11).mp3"),
        },
        {
          songTitle: "Fire on fire",
          artistName: "Sam Smith",
          src: require("../assets/audio (12).mp3"),
        },
        {
          songTitle: "Snowman",
          artistName: "Sia",
          src: require("../assets/audio (13).mp3"),
        },
      ],

      player: new Audio(),

    };
  },

  methods: {
    play() {
      this.current = this.songs[this.index];
      this.player.src = this.current.src;
      this.player.play();
      this.player.currentTime = this.currentTime;

      this.player.addEventListener(
        "ended",
        function () {
          this.index++;
          if (this.index > this.songs.length - 1) {
            this.index = 0;
          }

          this.current = this.songs[this.index];
          this.player.src = this.current.src;
          this.player.play();
        }.bind(this)
      );

      this.player.addEventListener(
        "timeupdate",
        function () {
          this.progressPercent = (this.player.currentTime/this.player.duration)*100;
          const progress = document.querySelector('#progress');
          progress.style.width = `${this.progressPercent}%`;
          console.log(this.progressPercent);
        }.bind(this)
      );

      this.isPlaying = true;
    },
    pause() {
      this.currentTime = this.player.currentTime;
      this.isPlaying = false;
      this.player.pause();
    },
    next() {
      this.index++;
      if (this.index > this.songs.length - 1) {
        this.index = 0;
      }

      this.player.src = this.songs[this.index].src;
      this.player.play();
      this.isPlaying = true;
    },
    prev() {
      this.index--;
      if (this.index < 0) {
        this.index = this.songs.length - 1;
      }

      this.player.src = this.songs[this.index].src;
      this.player.play();
      this.isPlaying = true;
    },
  },
};
</script>

<style scoped>
/*----- player style -----*/

.player {
  flex-grow: 1.2;
  padding: 20px;
  display: flex;
  gap: 15px;
  flex-direction: column;
  align-items: center;
  height: 84vh;
}

#songTitle,
#artistName {
  text-align: center;
  color: white;
  padding: 3px;
  text-shadow: 2px 2px 3px hsla(0, 0%, 0%, 0.473);
}

.coverImg {
  border-radius: 10px;
  box-shadow: var(--shadow);

  width: 70%;
  height: 100%;
  background: url(../assets/cover.jpg);
  background-position: center;
  background-size: cover;
}

#progressBar {
  border-radius: 100px;
  height: 3px;
  width: 80%;
  background-color: white;
}

#progress {
  background-color: var(--accent);
  border-radius: inherit;
  height: 100%;
  width: 0%;
  transition: width 0.1s linear;
}
</style>