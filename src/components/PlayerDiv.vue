<template>
  <div class="player" :class="{ play: progressPercent != 0 && isPlaying }" > 
    <!-- song info -->
    <div class="info">
      <h3 id="title"> {{ songs[index].title }} </h3>  <!-- {{ songs[index].title }} -->
      <h4 id="artist"> {{ songs[index].artist }} </h4>  <!-- {{ songs[index].artist }} -->
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
      <Btn id="delete">
        <i class="fas fa-trash"></i>
      </Btn>
      <Btn id="prev" @click="emitprev">
        <i class="fas fa-step-backward"></i>  
      </Btn>
      <Btn id="play"  @click="emitplay" v-if="!isPlaying"> 
        <i class="fas fa-play"></i>
      </Btn>
      <Btn id="pause" @click="emitpause" v-if="isPlaying"> 
        <i class="fas fa-pause"></i>
      </Btn>
      <Btn id="next" @click="emitnext">  
        <i class="fas fa-step-forward"></i>
      </Btn>
      <Btn id="fav" @click="$emit('likeCurrent')" > <!-- :class="{ fav: songs[index].isFav }" -->
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
    songs: {
      type: Array,
    },
    isPlaying: {
      type: Boolean,
    },
    progressTime: {
      type: String,
    },
    totalDuration: {
      type: String,
    },
    progressPercent: {
      type: Number,
    },
    index: {
      type: Number,
    },
  },

  /* components */
  components: {
    Btn,
  },

  methods: {
    emitprev() {
      this.$emit('playPrev');
    },
    emitnext() {
      this.$emit('playNext');
    },
    emitplay() {
      this.$emit('playCurrent');
    },
    emitpause() {
      this.$emit('pauseCurrent');
    },

    emitshuffle() {
      console.log('shuffling');
      this.$emit('shuffleList');
    },
  },

 
};
</script>

<style scoped>

#delete {
  color: grey;
}

.fav {
  color: #fe5046;
} 
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

#title,
#artist {
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