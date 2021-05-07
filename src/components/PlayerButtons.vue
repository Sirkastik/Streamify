<template>
  <div class="buttons">
    <button id="shuffles">
      <i class="fas fa-random"></i>
    </button>
    <button id="prev">
      <i class="fas fa-step-backward"></i>
    </button>
    <button id="play-pause">
      <i class="fas fa-play"></i>
    </button>
    <button id="next">
      <i class="fas fa-step-forward"></i>
    </button>
    <button id="fav">
      <i class="fas fa-heart"></i>
    </button>
  </div>
</template>

<script>
export default {
  name: "PLayerButtons",
};
</script>

<style scoped>

.buttons {
  display: flex;
}

button {
  display: grid;
  justify-content: space-around;

  font-size: 1rem;
  border-radius: 5px;
  color: white;
  outline: none;
  border: none;
  padding: 5px 10px;
  margin: 8px;
  background: var(--main);
  box-shadow: 1px 1px 3px 1px hsla(0, 0%, 0%, 0.473);
}

button:hover {
  color: var(--accent);
  background: var(--darker);
}

</style>