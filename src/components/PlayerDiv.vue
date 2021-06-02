<template>
  <div class="player" :class="{ play: progressPercent != 0 && isPlaying }">
    <!-- song info -->
    <div class="info">
      <h3 id="songTitle">{{ songs[index].songTitle }}</h3>
      <h4 id="artistName">{{ songs[index].artistName }}</h4>
    </div>

    <!-- cover image -->
    <div class="coverImg">
      <img src="../assets/cover.jpg" alt="cover" />
    </div>

    <!-- progress bar -->
    <div class="progressBox">
      <span> {{ progressTime }} </span>
      <div id="progressBar">
        <div id="progress"></div>
      </div>
      <span> {{ totalDuration }} </span>
    </div>

    <!-- control buttons -->
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

  props: {
    songs: Array,
  },

  /* components */
  components: {
    Btn,
  },

  data() {
    return {
      current: {},
      totalDuration: "0:00",
      currentTime: 0,
      progressTime: "0:00",
      isPlaying: false,
      index: 0,
      progressPercent: 0,
      player: new Audio(),

    };
  },

  methods: {
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
            this.index++;
            if (this.index > this.songs.length - 1) {
              this.index = 0;
            }

            this.current = this.songs[this.index];
            this.player.src = this.current.src;
            this.player.play();
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

    play() {
      this.current = this.songs[this.index];
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
      this.index++;
      if (this.index > this.songs.length - 1) {
        this.index = 0;
      }

      this.player.src = this.songs[this.index].src;
      this.player.play();
      this.updateInfo();
      this.checkEnd();
      this.isPlaying = true;
    },
    prev() {
      this.index--;
      if (this.index < 0) {
        this.index = this.songs.length - 1;
      }

      this.player.src = this.songs[this.index].src;
      this.player.play();
      this.updateInfo();
      this.checkEnd();
      this.isPlaying = true;
    },
  },
};
</script>

<style scoped>
/*----- player style -----*/

.player {
  color: white;
  flex-grow: 1.2;
  padding: 20px;
  display: flex;
  gap: 30px;
  flex-direction: column;
  align-items: center;
  height: 84vh;
}

#songTitle,
#artistName {
  text-align: center;
  color: white;
  padding: 5px;
  text-shadow: 2px 2px 3px hsla(0, 0%, 0%, 0.473);
}

.coverImg {
  box-shadow: var(--shadow);
  position: relative;
  width: 300px;
  height: 300px;
  border-radius: 50%;
}

.coverImg::after {
  content: "";
  background: var(--darker);
  border-radius: 50%;
  height: 20px;
  width: 20px;
  position: absolute;
  left: 50%;
  bottom: 50%;
  transform: translate(-42%, 40%);
}

.coverImg img {
  width: 100%;
  height: 100%;
  border-radius: inherit;

  object-fit: cover;
  object-position: center;

  animation: rotate 3s linear infinite;
  animation-play-state: paused;
}

.player.play .coverImg img {
  animation-play-state: running;
}

@keyframes rotate {
  from {
    transform: rotate(0deg);
  }

  to {
    transform: rotate(360deg);
  }
}

.progressBox {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
}

#progressBar {
  border-radius: 100px;
  height: 3px;
  width: 80%;
  background-color: white;
  margin: 0 5px;
}

#progress {
  background-color: var(--accent);
  border-radius: inherit;
  height: 100%;
  width: 0%;
  transition: width 0.1s linear;
}
</style>