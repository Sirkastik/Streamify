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
      file: require("./assets/mp3/audio (1).mp3"),

      player: undefined,

      songs: [],

      num: "1",

      currentIndex: 0,

      current: {},

      totalDuration: "0:00",

      progressTime: "0:00",
      isPlaying: false,
      progressPercent: 0,
      currentTime: 0,

      az: true,
    };
  },

  created() {
    // populate the songs
    fetch("http://localhost:5000/tracks", {
      method: "GET",
      credentials: "include",
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.error) {
          console.log(data.error);
          return;
        }
        // save data to songs
        /*list of ojects
        "id": id,
        "artist": artist,
        "title": title,
        "track_link":track_link,
        "added_by": added_by,
        "created_at": created_at
        */
        this.songs = data.response[1];
      })
      .catch((error) => {
        console.log(error);
      });
  },

  methods: {
    play() {
      this.player = new Audio()
      this.player.play();
      this.player.currentTime = this.currentTime;
      this.updateInfo();
      this.checkEnd();
      this.isPlaying = true;
      console.log(this.player.src);
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
      this.player.play(this.songs[this.currentIndex].track_link);
      this.updateInfo();
      this.checkEnd();
      this.isPlaying = true;
    },
    prev() {
      this.currentIndex--;
      if (this.currentIndex < 0) {
        this.currentIndex = this.songs.length - 1;
      }

      this.player.play(this.songs[this.currentIndex].track_link);
      this.updateInfo();
      this.checkEnd();
      this.isPlaying = true;
    },

    likeCurrent(id) {
      if (id) {
        let index = id - 1;
        this.songs[index].isFav = !this.songs[index].isFav;
      } else {
        this.songs[this.currentIndex].isFav = !this.songs[this.currentIndex]
          .isFav;
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

          this.player.play(this.songs[this.currentIndex]);
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
          let small_a = a.title.toLowerCase(),
            small_b = b.title.toLowerCase();
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
          let small_a = a.artist.toLowerCase(),
            small_b = b.artist.toLowerCase();
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
      if (index - 1 == this.currentIndex) {
        if (this.isPlaying == true) {
          this.pause();
        } else {
          this.play();
        }
      } else {
        this.currentIndex = index - 1;
        console.log(this.songs[this.currentIndex]);
        this.current = this.songs[index];
        this.player.play(this.current.track_link);
        this.isPlaying = true;
      }
    },

    addToFavorites(){
      fetch("http://localhost:5000/favorites",{
        method:'POST',
        creadentials:'include',
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          user_id: "todo", // userID
          track_id: "todo", //trackID
        })
      }).then(async (response)=>response.json()).then((data)=>{
        if (data.error){
          console.log(data.error)
        }else{
          alert(data.succesful)
        }
      })
    },

    getFavorites(){
      fetch("http://localhost:5000/favorites/"+"todo:user_id",{
        method:'GET',
        creadentials:'include',
      }).then(async (response)=>response.json()).then((data)=>{
        if (data.error){
          console.log(data.error)
        }else{
          /**
           * "id": id,
            "artist": artist,
            "title": title,
            "track_link":track_link,
            "added_by": added_by,
            "created_at": created_at
           */
          data.response
        }
      })
    }
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