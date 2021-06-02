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
    <DropBtn id="user">
      <template v-slot:button>
        <button class="dropbtn">
          <i class="far fa-user-circle"></i>
        </button>
      </template>
      <template v-slot:links>
        <a href="#" @click="toggleModal">Account</a>
      </template>
    </DropBtn>

    <Modal class="modal" v-if="showRegister">
      <form action="#" method="POST">
        <p id="username">
          <label>Username <input type="text" name="username" /></label>
        </p>
        <p>
          <label>Password <input type="password" name="password" /></label>
        </p>
        <p>
          <label
            >Confirm password <input type="password" name="confirm-pass"
          /></label>
        </p>
        <input type="button" name="button" value="Register" id="register" />
        <p>
          Already have an account?
          <span @click="toggleLogin">Sign In</span>
        </p>
      </form>
    </Modal>
    <Modal v-if="showLogin">
      <form action="#" method="POST">
        <p id="username">
          <label>Username <input type="text" name="username" /></label>
        </p>
        <p>
          <label>Password <input type="password" name="password" /></label>
        </p>
        <input type="button" name="button" value="Login" id="Login" />
        <p>
          Don't have an account?
          <span @click="toggleRegister">Sign Up</span>
        </p>
      </form>
    </Modal>
  </div>
</template>

<script>
import DropBtn from "./DropBtn";

import Modal from "./Modal";

export default {
  name: "Navbar",
  components: {
    Modal,
    DropBtn,
  },

  data() {
    return {
      showRegister: false,
    };
  },

  methods: {
    toggleModal() {
      this.showRegister = !this.showRegister;
    },
  },
};
</script>

<style scoped>
/*----- navbar style -----*/

.navbar {
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

/* Dropdown Style */
.dropbtn {
  border: none;
  outline: none;
  background: none;
  background: none;
  color: white;
  padding: 5px 20px;
  font-size: 1.7rem;
  cursor: pointer;
}

/* dropdown content style */
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
  color: var(--accent);
}

/* Modal style */
.modal {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
}
</style>