<template>
  <div class="navbar">
    <!--  Logo here -->
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
    <!--  Site name -->
    <h3>Streamify</h3>
    <!-- Drop button user account -->
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
    <!--  Sign up modal -->
    <Modal @close="hideModal" class="modal" v-if="showRegister">
      <form action="#" method="POST">
        <h2>Sign Up</h2>
        <div class="input-field focus username">
          <div class="icon">
            <i class="fas fa-user"></i>
          </div>
          <div>
            <h5>Username</h5>
            <input class="input" v-model="username" type="text" />
          </div>
        </div>
        <div class="input-field focus password">
          <div class="icon">
            <i class="fas fa-lock"></i>
          </div>
          <div>
            <h5>Password</h5>
            <input class="input" v-model="password" type="password" />
          </div>
        </div>
        <div class="input-field focus pass">
          <div class="icon">
            <i class="fas fa-lock"></i>
          </div>
          <div>
            <h5>Confirm password</h5>
            <input class="input" v-model="passConfirm" type="password" />
          </div>
        </div>
        <input
          type="button"
          @click="hideModal"
          class="btn"
          name="button"
          value="Register"
          id="register"
        />
        <p>
          Already have an account?
          <span class="link" @click="switchModal">Sign In</span>
        </p>
      </form>
    </Modal>
    <Modal @close="hideModal" class="modal" v-if="showLogin">
      <form action="#" method="POST">
        <h2>Sign In</h2>
        <div class="input-field focus username">
          <div class="icon">
            <i class="fas fa-user"></i>
          </div>
          <div>
            <h5>Username</h5>
            <input class="input" v-model="username" type="text" />
          </div>
        </div>
        <div class="input-field focus pass">
          <div class="icon">
            <i class="fas fa-lock"></i>
          </div>
          <div>
            <h5>Password</h5>
            <input class="input" v-model="password" type="password" />
          </div>
        </div>
        <input
          type="button"
          @click="hideModal"
          class="btn"
          name="button"
          value="Login"
          id="register"
        />
        <p>
          Already have an account?
          <span class="link" @click="switchModal">Sign In</span>
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
      showLogin: false,

      // to use as v-model in forms
      username: "",
      password: "",
      passConfirm: "",

      // sign in/up reponse
      user_id: 0,
    };
  },

  methods: {
    toggleModal() {
      this.showRegister = !this.showRegister;
    },

    switchModal() {
      this.showRegister = !this.showRegister;
      this.showLogin = !this.showLogin;
    },

    signout() {
      this.$store.dispatch("update_user");
      document.cookie = "id=;username=;Max-Age=-99999999;";
    },

    signup() {
      fetch("http://localhost:5000/create_user", {
        method: "POST",
        credentials: "include",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          username: this.username,
          password: this.password,
        }),
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.error) {
            console.log(data.error);
            return;
          }
          /*
            id": id,
            "created_at": created_at,
            "username": username,
            "password": password,
        */
          data.response; //is above object
          document.cookie = `id=${data.response.id};user=${this.username}`;
          this.$store.dispatch("update_user");
        })
        .catch((error) => console.log(error));
    },

    deleteUser(user_id) {
      if (user_id) {
        fetch("http://localhost:5000/delete_user/" + user_id, {
          method: "DELETE",
          headers: {
            "Content-Type": "multipart/form-data",
          },
          credentials: "include",
        })
          .then(async (response) => response.json)
          .then((data) => {
            if (data.error) {
              console.log(data.error);
            }
            alert(data.response);
          });
      }
    },

    signin() {
      fetch(`http://localhost:5000/get_user/${this.username}`, {
        method: "POST",
        headers: {
          "Content-Type": "multipart/form-data",
        },
        credentials: "include",
      })
        .then((response) => response.json())
        .then((data) => {
          if (data.error) {
            console.log(data.error);
            return;
          }
          /*
            id": id,
            "created_at": created_at,
            "username": username,
            "password": password,
        */
          data.response; //is above object
          document.cookie = `id=${data.response.id};user=${this.username}`;
          this.$store.dispatch("update_user");
        })
        .catch((error) => console.log(error));
    },

    hideModal() {
      this.showRegister = false;
      this.showLogin = false;
    },
  },
};
</script>

<style scoped>
/* form style */

form h2 {
  font-size: 2.9rem;
  text-transform: uppercase;
  margin: 20px 0;
}

.input-field {
  display: grid;
  grid-template-columns: 7% 93%;
  margin: 25px 0;
  padding: 5px 0;
  border-bottom: 2px solid grey;
}

.input-field.focus div h5 {
  top: -5px;
  font-size: 15px;
}

.input-field.username {
  margin-top: 0;
}

.input-field.pass {
  margin-bottom: 4px;
}

.icon {
  display: flex;
  justify-content: center;
  align-items: center;
}

.input-field > div {
  position: relative;
  height: 45px;
}

.input-field > div h5 {
  position: absolute;
  left: 10px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--main);
  font-size: 1.2rem;
  transition: 0.3s;
}

.input {
  font-size: 1.2rem;
  position: absolute;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  border: none;
  outline: none;
  background: none;
  padding: 0.5rem 0.7rem;
  color: var(--darker);
}

.btn {
  background: var(--darker);
  color: white;
  box-shadow: var(--shadow);
  text-transform: uppercase;
  display: block;
  width: 100%;
  height: 50px;
  border-radius: 25px;
  margin: 20px 0;
  font-size: 1.2rem;
  outline: none;
  border: none;
  transition: 0.5s;
}

.btn:hover {
  background: var(--accent);
  color: var(--darker);
}

.link {
  cursor: pointer;
  transition: 0.5s;
  color: var(--accent);
}

.link:hover {
  color: var(--main);
  text-shadow: 1px 1px 3px 1px hsl(0, 0%, 100%);
}

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
  width: 100%;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
}
</style>