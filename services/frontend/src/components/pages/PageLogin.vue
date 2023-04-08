<template>
  <article>
    <div class="container" :class="{'sign-up-active' : signUp}">
      <div class="overlay-container">
        <div class="overlay">
          <div class="overlay-left">
            <h2>Welcome Back!</h2>
            <p>Please login with your personal info</p>
            <button class="invert" id="signIn" @click="signUp = false">Sign In</button>
          </div>
          <div class="overlay-right">
            <h2>Hello, Friend!</h2>
            <p>Please enter your personal details</p>
            <button class="invert" id="signUp" @click="signUp = true">Sign Up</button>
          </div>
        </div>
      </div>
      <form class="sign-up" @submit.prevent="submitForm">
        <h2>Create login</h2>
        <div>Use your email for registration</div>
        <input type="text" placeholder="Name" v-model="name" />
        <input type="email" placeholder="Email" v-model="email" />
        <input type="password" placeholder="Password" v-model="password" />
        <div>
          <select id="native-language" v-model="nativeLanguage" >
            <option value="" disabled selected>Native language</option>
            <option value="English">English</option>
            <option value="Spanish">Spanish</option>
            <option value="French">French</option>
            <option value="German">German</option>
            <option value="Ukrainian">Ukrainian</option>
            <option value="Arabic">Arabic</option>
          </select>
        </div>
        <div>
          <select id="goal-level" v-model="goalLevel">
            <option value="" disabled selected>Goal Level</option>
            <option value="A1">A1</option>
            <option value="A2">A2</option>
            <option value="B1">B1</option>
            <option value="B2">B2</option>
            <option value="C1">C1</option>
            <option value="C2">C2</option>
          </select>
        </div>
        <div>
          <select id="current-level" v-model="currentLevel">
            <option value="" disabled selected>Current Level</option>
            <option value="A1">A1</option>
            <option value="A2">A2</option>
            <option value="B1">B1</option>
            <option value="B2">B2</option>
            <option value="C1">C1</option>
            <option value="C2">C2</option>
          </select>
        </div>
        <button class="sign-up-btn " type="submit">Sign Up</button>
      </form>
      <form class="sign-in" @submit.prevent="submitLogin">
        <h2>Sign In</h2>
        <div>Use your account</div>
        <input type="email" placeholder="Email" v-model="loginEmail" />
        <input type="password" placeholder="Password" v-model="loginPassword" />
        <a href="#">Forgot your password?</a>
        <button class="sign-in-btn" type="submit" id="signInBtn">Sign In</button>
      </form>
    </div>
  </article>
</template>
<script>
export default {
  data: () => {
    return {
      signUp: false,
      name: '',
      email: '',
      password: '',
      nativeLanguage: '',
      goalLevel: '',
      currentLevel: '',
      loginEmail: '',
      loginPassword: '',
    }
  },
  methods: {
    async submitForm() {
      const data = {
        user_name: this.name,
        email: this.email,
        password: this.password,
        native_language: this.nativeLanguage,
        goal_level: this.goalLevel,
        user_level: this.currentLevel,
      };
      try {
        const response = await fetch('http://192.168.0.163:8081/register', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(data),
        });
        if (!response.ok) {
          throw new Error('Registration failed');
        }
        console.log('Registration successful');
      } catch (error) {
        console.error(error);
      }
    },
    async submitLogin() {
      const data = {
        grant_type: "",
        username: this.loginEmail,
        password: this.loginPassword,
        scope: "",
        client_id: "",
        client_secret: null,
      };
      try {
        const response = await fetch('http://192.168.0.163:8081/login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(data),
        });
        if (!response.ok) {
          throw new Error('Login failed');
        }
        console.log('Login successful');
      } catch (error) {
        console.error(error);
      }
    },
  },
}
</script>
<style lang="scss" scoped>
.container {
  position: relative;
  width: 768px;
  height: 480px;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 15px 30px rgba(0, 0, 0, .2),
  0 10px 10px rgba(0, 0, 0, .2);
  background: linear-gradient(to bottom, #efefef, #ccc);
  .overlay-container {
    position: absolute;
    top: 0;
    left: 50%;
    width: 50%;
    height: 100%;
    overflow: hidden;
    transition: transform .5s ease-in-out;
    z-index: 100;
  }
  .overlay {
    position: relative;
    left: -100%;
    height: 100%;
    width: 200%;
    background: linear-gradient(to bottom right, #a1a1a1, #484848);
    color: #fff;
    transform: translateX(0);
    transition: transform .5s ease-in-out;

  }
  @mixin overlays($property) {
    position: absolute;
    top: 0;
    display: flex;
    align-items: center;
    justify-content: space-around;
    flex-direction: column;
    padding: 70px 40px;

    text-align: center;
    transform: translateX($property);
    transition: transform .5s ease-in-out;
  }
  .overlay-left {
    @include overlays(-20%);
    padding: 25% 5% 15% 5%;
  }
  .overlay-right {
    @include overlays(0);
    right: 0;
    padding: 25% 5% 15% 20%;
  }
}
h2 {
  margin: 0;
}
p {
  margin: 20px 0 30px;
}
a {
  color: #222;
  text-decoration: none;
  margin: 15px 0;
  font-size: 1rem;
}
button {
  border-radius: 20px;
  border: 1px solid #494949;
  background-color: #727272;
  color: #fff;
  font-size: 1rem;
  font-weight: bold;
  padding: 10px 40px;
  letter-spacing: 1px;
  text-transform: uppercase;
  cursor: pointer;
  transition: transform .1s ease-in;
  &:active {
    transform: scale(.9);
  }
  &:focus {
    outline: none;
  }
}
button.invert {
  background-color: transparent;
  border-color: #fff;
}
form {
  position: absolute;
  top: 0;
  display: flex;
  align-items: center;
  justify-content: space-around;
  flex-direction: column;
  padding: 15% 12% 15% 12%;

  text-align: center;
  background: linear-gradient(to bottom, #efefef, #ccc);
  transition: all .5s ease-in-out;
  div {
    font-size: 1rem;
  }
  input {
    background-color: #eee;
    border: none;
    padding: 8px 15px;
    margin: 6px 0;
    width: calc(100% - 30px);
    border-radius: 15px;
    border-bottom: 1px solid #ddd;
    box-shadow: inset 0 1px 2px rgba(0, 0, 0, .4),
    0 -1px 1px #fff,
    0 1px 0 #fff;
    overflow: hidden;
    &:focus {
      outline: none;
      background-color: #fff;
    }
  }
}
.sign-in {
  left: -4%;
  z-index: 2;
}
.sign-up {
  top:-5%;
  left: 2%;
  z-index: 1;
  opacity: 0;
  padding-left: 20px ;}
.sign-up-active {
  .sign-in {
    transform: translateX(100%);
  }
  .sign-up {
    transform: translateX(100%);
    opacity: 1;
    z-index: 5;
    animation: show .5s;
  }
  .overlay-container {
    transform: translateX(-100%);
  }
  .overlay {
    transform: translateX(50%);
  }
  .overlay-left {
    transform: translateX(0);
  }
  .overlay-right {
    transform: translateX(20%);
  }
}
@keyframes show {
  0% {
    opacity: 0;
    z-index: 1;
  }
  49% {
    opacity: 0;
    z-index: 1;
  }
  50% {
    opacity: 1;
    z-index: 10;
  }
}
select {

  background-color: #eee;
  border: none;
  padding: 8px 48px 0 10px;
  margin: 6px 0;
  height: 32px;
  width: 180px;
  color:gray;
  border-radius: 15px;
  border-bottom: 1px solid #ddd;
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, .4),
  0 -1px 1px #fff,
  0 1px 0 #fff;
  overflow: hidden;
  &:focus {
    outline: none;
    background-color: #fff;}



}
.sign-up-btn{
  margin-top: 5px;
}

</style>
