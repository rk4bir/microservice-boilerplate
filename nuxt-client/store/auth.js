export const state = () => ({
  user: null,
})

export const mutations = {
  updateUser (state, value) {
    state.user = value
  },
  resetUser (state) {
    state.user = null
  },
  logOut (state) {
    state.user = null
  }
}
