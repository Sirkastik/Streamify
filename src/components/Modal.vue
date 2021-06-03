<template>
  <div class="registration">
    <div class="background"></div>
    <div class="content">
      <Btn class="close" @click="$emit('close')">
        <i class="fas fa-times"></i>
      </Btn>
      <div class="modalcontainer">
        <slot id="slot"></slot>
      </div>
    </div>
  </div>
</template>

<script>
import Btn from "./Btn";

export default {
  name: "Modal",

  /* components */
  components: {
    Btn,
  },

};
</script>

<style scoped>
.close {
  background: white;
  color: var(--darker);
  position: absolute;
  right: 10px;
  top: 10px;
}

.registration {
  z-index: 10;
}

.background {
  background: var(--darker);
  width: 100vw;
  height: 100vh;
  position: absolute;

}

.content {
  height: 100vh;
  position: relative;
  display: grid;
  justify-content: center;
  align-items: center;
}

.modalcontainer {
  width: 100%;
  background: white;
  padding: 100px;
  border-radius: 10px;
  text-align: center;
  box-shadow: var(--shadow);
  color: var(--darker);
  font-size: 1.3rem;
}
</style>
