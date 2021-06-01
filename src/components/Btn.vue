<template>
  <button>
    <slot></slot>
  </button>
</template>

<script>
export default {
  name: "Btn",
};
</script>

<style scoped>
/* Button style for button component */
button {
  cursor: pointer;
  font-size: 0.9rem;
  border-radius: 5px;
  color: white;
  outline: none;
  border: none;
  padding: 5px 10px;
  margin: 0 8px;
  background: var(--main);
  box-shadow: 1px 1px 3px 1px hsla(0, 0%, 0%, 0.473);
}

/* Change color and bg-color on hover */
button:hover {
  color: var(--accent);
  background: var(--darker);
}
</style>