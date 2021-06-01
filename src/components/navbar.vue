<template>
  <div class="navbar">
    <svg
      version="1.1"
      id="Layer_1"
      xmlns="http://www.w3.org/2000/svg"
      xmlns:xlink="http://www.w3.org/1999/xlink"
      x="0px"
      y="0px"
      viewBox="0 0 64 80"
      style="enable-background: new 0 0 64 80"
      xml:space="preserve"
    >
      <path
        d="M2.9,23.9c-0.8,0-1.5,0.7-1.5,1.5v13.2c0,0.8,0.7,1.5,1.5,1.5s1.5-0.7,1.5-1.5V25.4C4.4,24.6,3.8,23.9,2.9,23.9z"
      />
      <path
        d="M11.2,19.4c-0.8,0-1.5,0.7-1.5,1.5v22.2c0,0.8,0.7,1.5,1.5,1.5s1.5-0.7,1.5-1.5V20.9C12.7,20,12.1,19.4,11.2,19.4z"
      />
      <path
        d="M19.5,12.3c-0.8,0-1.5,0.7-1.5,1.5v36.3c0,0.8,0.7,1.5,1.5,1.5S21,51,21,50.2V13.8C21,13,20.4,12.3,19.5,12.3z"
      />
      <path
        d="M27.8,23.2c-0.8,0-1.5,0.7-1.5,1.5v14.7c0,0.8,0.7,1.5,1.5,1.5s1.5-0.7,1.5-1.5V24.7C29.3,23.8,28.7,23.2,27.8,23.2z"
      />
      <path
        d="M36.2,26.3c-0.8,0-1.5,0.7-1.5,1.5v8.3c0,0.8,0.7,1.5,1.5,1.5s1.5-0.7,1.5-1.5v-8.3C37.7,27,37,26.3,36.2,26.3z"
      />
      <path
        d="M44.5,17.9c-0.8,0-1.5,0.7-1.5,1.5v25.2c0,0.8,0.7,1.5,1.5,1.5s1.5-0.7,1.5-1.5V19.4C46,18.6,45.3,17.9,44.5,17.9z"
      />
      <path
        d="M52.8,23.2c-0.8,0-1.5,0.7-1.5,1.5v14.7c0,0.8,0.7,1.5,1.5,1.5s1.5-0.7,1.5-1.5V24.7C54.3,23.8,53.6,23.2,52.8,23.2z"
      />
      <path
        d="M61.1,26c-0.8,0-1.5,0.7-1.5,1.5v9c0,0.8,0.7,1.5,1.5,1.5s1.5-0.7,1.5-1.5v-9C62.6,26.6,61.9,26,61.1,26z"
      />
    </svg>
    <h3>Streamify</h3>
    <div class="dropdown">
      <button class="dropbtn">
        <i class="far fa-user-circle"></i>
      </button>

      <div class="dropdown-content">
        <a href="#" @click="toggleModal">Account</a>
      </div>
    </div>
    <Modal id="modal" v-if="showModal" />
  </div>
</template>

<script>
import Modal from "./Modal";

export default {
  name: "Navbar",
  components: {
    Modal,
  },

  data() {
    return {
      showModal: false,
    };
  },

  methods: {
    toggleModal() {
      this.showModal = !this.showModal;
    },
  },
};
</script>

<style scoped>
#modal {
  position: absolute;
}

/*----- navbar style -----*/

.navbar {
  position: relative;
  background: var(--main);
  box-shadow: var(--shadow);
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0px 20px;
  margin-bottom: 10px;
}

svg {
  height: 3.5rem;
  fill: white;
}

h3 {
  font-size: 1.5rem;
  color: white;
}

button {
  border: none;
  outline: none;
  background: none;
}

.fa-user-circle {
  font-size: 1.7rem;
  color: white;
}

/* The container <div> - needed to position the dropdown content */
.dropdown {
  position: relative;
  display: inline-block;
}

/* Dropdown Content (Hidden by Default) */
.dropdown-content {
  display: none;
  position: absolute;
  background-color: var(--main);
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
  z-index: 1;
  left: -450%;
  top: 80%;
  border-radius: 10px;
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

/* Show the dropdown menu on hover */
.dropdown:hover .dropdown-content {
  display: block;
}

/* Change the background color of the dropdown button when the dropdown content is shown */
.dropdown:hover .fa-user-circle {
  color: #fe5046;
}
</style>