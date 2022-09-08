<template>
  <div class="container py-5 z-depth-1">
    <section class="px-md-5 mx-md-5 text-center text-lg-left dark-grey-text">
        <div class="row d-flex justify-content-center">
        <div class="col-md-6">
            <form class="text-center">
            <p class="h4 mb-4">Log In</p>
            <input type="text" id="defaultRegisterFormEmail" name="logusername" class="form-control mb-4" placeholder="Username">
            <input type="password" id="defaultRegisterFormPassword" name="logpassword" class="form-control" v-model="pass1" placeholder="Password" aria-describedby="defaultRegisterFormPasswordHelpBlock">
            <small id="defaultRegisterFormPhoneHelpBlock" class="form-text text-danger mb-4">{{message}}</small>
            <button class="btn btn-info my-4 btn-block" name="formpurpose" value="loginval" type="submit">Log in</button>
            </form>
        </div>
        </div>
    </section>
    </div>
</template>

<script>
export default {
  name: "HelloWorld",
  props: {
    msg: String,
  },
};
</script>

<style>

</style>
