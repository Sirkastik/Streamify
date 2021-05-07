<template>
  <div class="Player">
    <div class="info">
      <button id="display">
        <i class="fas fa-ellipsis-v"></i>
      </button>
      <h3 id="song-name">{{ songName }}</h3>
      <h4 id="artist-name">{{ artistName }}</h4>
    </div>
    <div class="cover"></div>
    <audio src="../assets/Chord_Overstreet-Hold_On.mp3"></audio>
    <div id="progressBar">
      <div id="progress"></div>
    </div>
    <div id="controls">
      <PlayerButtons />
    </div>
  </div>
</template>

<script>
import PlayerButtons from "./PlayerButtons";

export default {
  name: "Player",
  components: {
    PlayerButtons,
  },
  data() {
    return {
      songName: "Jeffery",
      artistName: "Young Thug",
    };
  },
};

</script>

<style scoped>

.info {
  position: relative;
}

.info button {
  position: absolute;
  left: -130%;
  display: none;

  font-size: 0.8rem;
  border-radius: 5px;
  color: white;
  outline: none;
  border: none;
  padding: 5px 10px;
  margin: 8px;
  background: var(--main);
  box-shadow: 1px 1px 3px 1px hsla(0, 0%, 0%, 0.473);
}



/*----- player style -----*/

.Player {
  padding: 20px;
  display: flex;
  gap: 15px;
  flex-direction: column;
  align-items: center;
  height: 84vh;
}

#song-name,
#artist-name {
  text-align: center;
  color: white;
  padding: 3px;
  text-shadow: 2px 2px 3px hsla(0, 0%, 0%, 0.473);
}

.cover {
  border-radius: 10px;
  box-shadow: var(--shadow);

  width: 70%;
  height: 100%;
  background: url(../assets/cover.jpg);
  background-position: center;
  background-size: cover;
}

#progressBar {
  border-radius: 10px;
  height: 3px;
  width: 80%;
  background-color: white;
}

#progress {
  background-color: var(--accent);
  border-radius: inherit;
  height: 100%;
  width: 50%;
  transition: width 0.1s linear;
}

</style>
