<template>
  <div class="List">
    <ListButtons />
    <div class="songList">
      <ul>
        <li v-for="song in songs" v-bind:key="song">
          <div class="left">{{ song.songName }} - {{ song.artistName }}</div>
          <div class="right">
            <span>{{ song.duration }}</span>
            <button id="fav">
              <i class="fas fa-heart"></i>
            </button>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import ListButtons from "./ListButtons";

export default {
  name: "List",
  components: {
    ListButtons,
  },

  data() {
    return {
      songs: [
        {
          songName: "Someone You Loved",
          artistName: "Lewis Capaldi",
          duration: "3:35",
        },
        {
          songName: "No Time To Die",
          artistName: "Billie Eilish",
          duration: "3:35",
        },
        {
          songName: "Loco Contigo",
          artistName: "DJ Snake_ J. Balvin_ Tyga",
          duration: "3:35",
        },
        {
          songName: "Takeaway",
          artistName: "The Chainsmokers_ ILLENIUM",
          duration: "3:35",
        },
        {
          songName: "Tick Tock",
          artistName: "Clean Bandit and Mabel",
          duration: "3:35",
        },
        { songName: "_My Last Words_", artistName: "Dax", duration: "3:35" },
        {
          songName: "I Like It",
          artistName: "Cardi B_ Bad Bunny _ J Balvin",
          duration: "3:35",
        },
        {
          songName: "Lovely",
          artistName: "Billie Eilish_ Khalid",
          duration: "3:35",
        },
        {
          songName: "Hold On",
          artistName: "Chord Overstreet",
          duration: "3:35",
        },
        {
          songName: "Peer Pressure",
          artistName: "James Bay",
          duration: "3:35",
        },
        {
          songName: "Freaking Me Out",
          artistName: "Ava Max",
          duration: "3:35",
        },
        {
          songName: "RITMO",
          artistName: "Black Eyed Peas_ J Balvin",
          duration: "3:35",
        },
        {
          songName: "Shape of You",
          artistName: "Ed Sheeran",
          duration: "3:35",
        },
      ],
    };
  },
};
</script>

<style scoped>
.List {
  width: 90%;
  margin: 20px 20px;
}

.songList {
  height: 72vh;
  overflow-y: scroll;
  scrollbar-color: var(--main) #fe4f468c;
}

li {
  display: flex;
  justify-content: space-between;

  cursor: pointer;
  color: white;
  list-style: none;
  padding: 10px 20px;
  margin: 10px;
  background: var(--main);
  box-shadow: var(--shadow);
  border-radius: 10px;
  font-size: 0.95rem;
}

.right span {
  margin-right: 20px;
}

button {
  font-size: 0.7rem;
  color: rgba(255, 255, 255, 0.507);
  outline: none;
  border: none;
  padding: 5px;
  background: none;
}

button:hover {
  color: var(--accent);
  background: var(--darker);
}

li:hover {
  color: var(--accent);
  background: var(--darker);
}



</style>