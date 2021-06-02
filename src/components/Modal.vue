<template>
  <div class="registration" :class="{ hide: hideModal }">
    <div class="background"></div>
    <div class="content">
      <Btn class="close" @click="hide()">
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

  data() {
    return {
      hideModal: false,
    };
  },

  methods: {
    hide() {
      this.hideModal = true;
    },
  },
};
</script>

<style scoped>
.close {
  background: var(--darker);
  position: absolute;
  right: 10px;
  top: 10px;
}

.registration {
  z-index: 10;
}

.background {
  background: var(--gradient);
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

.hide {
  z-index: -10;
  opacity: 0;
}

.modalcontainer {
  width: 80%;
  background: var(--darker);
  padding: 100px;
  border-radius: 10px;
  text-align: center;
  box-shadow: var(--shadow);
  color: white;
  font-size: 1.3rem;
}
</style>
