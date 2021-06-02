<template>
  <div class="List">
    <!-- list div navigation -->
    <div class="listNav">
      <!-- functionality buttons -->
      <div class="btns">
        <Btn @click="sortlist">
          <i class="fas fa-sort-alpha-up"></i>
        </Btn>
        <Btn>
          <form action="#">
            <label for="input">
              <i class="fas fa-plus"></i>
            </label>
            <input type="file" id="input" multiple accept="audio/*" />
          </form>
        </Btn>
        <Btn>
          <form class="example" action="#">
            <input type="text" placeholder="Search music..." name="search" />
            <button type="submit"><i class="fa fa-search"></i></button>
          </form>
        </Btn>
      </div>
      <!-- dropdown button -->
      <DropBtn>
        <template v-slot:button>
          <button class="dropbtn">
            All Music<i class="fas fa-sort-down"></i>
          </button>
        </template>
        <template v-slot:links>
          <a href="#" @click="showAll">All Music</a>
          <a href="#" @click="showFav">Favourites</a>
          <a href="#" @click="showAdded">Added Music</a>
        </template>
      </DropBtn>
    </div>

    <div class="songList favSongs" v-if="favList">
      <ul>
        <li
          v-for="song in favSongs"
          v-bind:key="song.songIndex"
          :class="{ fav: song.fav }"
        >
          <div class="left" @click="$emit('playSong', song.songIndex)">
            {{ song.songTitle }} - {{ song.artistName }}
          </div>
          <div class="right">
            <span>{{ song.duration }}</span>
            <Btn class="favBtn" @click="$emit('likeSong', song.songIndex)">
              <i class="fas fa-heart"></i>
            </Btn>
          </div>
        </li>
      </ul>
    </div>

    <!-- list div -->
    <div class="songList allSongs" v-if="allSongs">
      <ul>
        <li
          v-for="song in songs"
          v-bind:key="song.songIndex"
          :class="{ fav: song.fav }"
        >
          <div class="left" @click="$emit('playSong', song.songIndex)">
            {{ song.songTitle }} - {{ song.artistName }}
          </div>
          <div class="right">
            <span>{{ song.duration }}</span>
            <Btn class="favBtn" @click="$emit('likeSong', song.songIndex)">
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

  props: {
    songs: Array,
  },

  /* components */
  components: {
    Btn,
    DropBtn,
  },

  data() {
    return {
      allSongs: true,

      favList: false,

      addedList: false,

      favsongs: [],
    };
  },

  methods: {
    sortlist() {
      this.$emit("sortSongs");
    },

    showAll() {
      this.allSongs = true;
      this.favList = false;
      this.addedList = false;
    },
    showFav() {
      this.allSongs = false;
      this.addedList = false;
      this.favList = true;
    },
    showAdded() {
      this.addedList = true;
      this.allSongs = false;
      this.favList = false;
    },
  },

  computed: {
    favSongs() {
      return this.songs.filter((song) => song.fav);
    },
  },
};
</script>

<style scoped>
.dropbtn {
  background: none;
  color: white;
  padding: 5px 20px;
  font-size: 16px;
  border-radius: 8px;
  border: 2px solid white;
  cursor: pointer;
  display: flex;
  gap: 5px;
}

/* Links inside the dropdown */
.dropdown-content a {
  color: white;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  border-radius: inherit;
}

/* Change color of dropdown links on hover */
.dropdown-content a:hover {
  background-color: var(--darker);
  color: var(--accent);
}
/* Change the background color of the dropdown button when the dropdown content is shown */
.dropdown:hover .dropbtn {
  border: 2px solid#fe5046;
  color: #fe5046;
}

#input {
  display: none;
}

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

.favBtn {
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

.fav .favBtn {
  color: #fe5046;
}
</style>