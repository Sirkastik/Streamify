<template>
  <div class="registration">
    <form action="#" method="post">
      <p id="username">
        <label>Username <input type="text" name="username"/></label>
      </p>
      <p>
        <label>Email <input type="email" name="email"/></label>
      </p>
      <p>
        <label>Password <input type="password" name="password"/></label>
      </p>
      <p>
        <label
          >Confirm password <input type="password" name="confirm-pass"
        /></label>
      </p>
      <input type="button" name="button" value="Register" id="register" />
    </form>
  </div>
</template>

<script>
export default {
  name: "Modal",
};
</script>

<style scoped>

form {
  text-align: center;
}

#register {
  font-size: 1rem;
  border-radius: 5px;
  color: white;
  outline: none;
  border: none;
  padding: 5px 10px;
  margin: 8px;
  background: hsla(0, 4%, 10%, 0.575);
  box-shadow: 1px 1px 2px 1px hsla(0, 10%, 47%, 0.514);
}
</style>
