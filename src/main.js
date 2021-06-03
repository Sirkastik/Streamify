import '@fortawesome/fontawesome-free/css/all.css'
import '@fortawesome/fontawesome-free/js/all.js'

import { createApp } from 'vue'
import { createStore } from 'vuex'
import App from './App.vue'

const store = createStore({
  state: {
    user: {
      id: 0,
      username: ''
    }
  },

  geters: {
    get_user () {
      return state.user
    }
  },

  mutations: {
    set_user (state, username, id) {
      state.user = { id: id, username: username }
    }
  },

  actions: {
    update_user ({ commit }) {
      let cookie = document.cookie
      if (cookie.startsWith('id=')) {
        let cookie_strs = cookie.split(';')
        context.commit(
          'set_user',
          cookie_strs[0].slice('id='.length),
          cookie_strs[1].slice('user='.length)
        )
      }
    }
  }
})

createApp(App)
  .use(store)
  .mount('#app')
