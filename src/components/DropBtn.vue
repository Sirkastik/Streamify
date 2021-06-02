<template>
    <div class="dropdown">
      <slot name="button"></slot>
      <div class="dropdown-content">
        <slot name="links"></slot>
      </div>
    </div>
</template>

<script>
export default {
    name: "DropBtn"
}
</script>

<style scoped>
button {
  outline: none;
  border: none;
}

/* The container <div> - needed to position the dropdown content */
.dropdown {
  position: relative;
  display: inline-block;
}

.down {
  display: grid;
  justify-content: space-around;
}

/* Dropdown Content (Hidden by Default) */
.dropdown-content {
  left: -80px;
  display: none;
  position: absolute;
  background-color: var(--main);
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
  z-index: 1;
  border-radius:10px;
}

/* Show the dropdown menu on hover */
.dropdown:hover .dropdown-content {
  display: block;
}


</style>