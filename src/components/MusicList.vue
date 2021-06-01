<template>
  <div class="List">
    <div class="listNav">
      <div class="btns">
        <Btn>
          <i class="fas fa-sort-alpha-up"></i>
        </Btn>
        <Btn>
          <i class="fas fa-plus"></i>
        </Btn>
        <Btn>
          <form class="example" action="#">
            <input type="text" placeholder="Search music..." name="search" />
            <button type="submit"><i class="fa fa-search"></i></button>
          </form>
        </Btn>
      </div>
      <div class="dropdown">
        <DropBtn />
      </div>
    </div>

    <div class="songList">
      <ul>
        <li v-for="song in songs" v-bind:key="song.src" @click="play(song)">
          <div class="left">{{ song.songTitle }} - {{ song.artistName }}</div>
          <div class="right">
            <span>{{ song.duration }}</span>
            <Btn id="favBtn">
              <i class="fas fa-heart"></i>
            </Btn>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import DropBtn from "./DropBtn";

import Btn from "./Btn";

export default {
  name: "MusicList",
  components: {
    Btn,
    DropBtn,
  },

  data() {
    return {
      current: {},

      currentTime: 0,

      isPlaying: false,

      index: 0,

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
    play(song) {
      this.current = song;
      this.player.src = this.current.src;

      this.player.play();
    },
  },
};
</script>

<style scoped>
.List {
  flex-grow: 1.8;
  margin: 20px 20px;
}

.listNav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.songList {
  height: 72vh;
  overflow-y: scroll;
  scrollbar-color: var(--main) #fe4f468c;
}

li {
  display: flex;
  justify-content: space-between;

  color: white;
  list-style: none;
  padding: 10px 20px;
  margin: 10px;
  background: var(--main);
  box-shadow: var(--shadow);
  border-radius: 10px;
  font-size: 0.95rem;
}

li > * {
  cursor: pointer;
}

.right span {
  margin-right: 20px;
}

#favBtn {
  background: none;
  box-shadow: none;
  padding: 0;
}

li:hover {
  color: var(--accent);
  background: var(--darker);
}


/* search button */

form input {
  background: none;
  outline: none;
  border: none;
  color: white;
}

form button {
  cursor: pointer;
  border: none;
  background: none;
  color: white;
}

form button:hover {
  color: var(--accent);
}

</style>