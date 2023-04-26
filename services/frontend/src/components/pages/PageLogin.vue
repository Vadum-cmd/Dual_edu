<template>
  <article>
    <ModalWindow v-model:is-active="verification">
      <div class="verification_window_container">
        <div class="verification_window">
          <h1>Hello, please verify your email address.</h1>
          <p>Check inbox messages <i>(if it is not there check spam)</i>.</p>
          <button class="close" @click="verification = false">
            <font-awesome-icon :icon="['fas', 'circle-xmark']"/>
          </button>
        </div>
      </div>
    </ModalWindow>
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
      <form class="sign-up" @submit.prevent="submitRegister">
        <h2>Create account</h2>
        <div>Use your email for registration</div>
        <input type="text" placeholder="Name" v-model="name"/>
        <input type="email" placeholder="Email" v-model="email"/>
        <input type="password" placeholder="Password" v-model="password"/>
        <div>
          <select id="native-language" v-model="nativeLanguage">
            <option value="" disabled selected>Native language</option>
            <option value="Spanish">Spanish</option>
            <option value="Ukrainian">Ukrainian</option>
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
        <input type="email" placeholder="Email" v-model="loginEmail"/>
        <input type="password" placeholder="Password" v-model="loginPassword"/>
        <div class="forgot-password" @click="forgotPassword = true">Forgot your password?</div>
        <button class="sign-in-btn" type="submit" id="signInBtn">Sign In</button>
        <ModalWindow v-model:is-active="forgotPassword">

          <h2>Reset Password</h2>
          <div>Enter your email address to reset your password</div>
          <input type="email" placeholder="Email" v-model="resetEmail"/>
          <button class="reset-password-btn" @click="resetPassword" id="resetPasswordBtn">Reset Password</button>
          <button class="cancel-link" @click="forgotPassword = false">
            <font-awesome-icon :icon="['fas', 'circle-xmark']"/>
          </button>

        </ModalWindow>

      </form>
    </div>
  </article>
</template>
<script>

import ModalWindow from "@/components/UI/ModalWindow.vue";



export default {
  components: {ModalWindow},
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
      forgotPassword: false,
      resetEmail: '',
      scope: '',
      grant_type: '',
      client_id: '',
      client_secret: '',
      is_superuser: false,
      is_verified: false,
      is_active: true,
      url: process.env.VUE_APP_URL,
      verification:false
    }
  },
  methods: {
    async submitRegister() {
      if (!this.name || !this.email || !this.password || !this.nativeLanguage || !this.goalLevel || !this.currentLevel) {
        alert('Please fill in all required fields');
        return;
      }
      try {
        const data = {
          "email": this.email,
          "password": this.password,
          "is_active": this.is_active,
          "is_superuser": this.is_superuser,
          "is_verified": this.is_verified,
          "user_name": this.name,
          "native_language": this.nativeLanguage,
          "goal_level": this.goalLevel,
          "user_level": this.currentLevel
        };
        await fetch(this.url + `/register`, {
          body: JSON.stringify(data),
          method: 'POST',
          headers: {'accept': 'application/json', 'Content-Type': 'application/json'},
          credentials: 'include'
        });
        this.verification=true;

      } catch (error) {
        console.error(error);
      }
    },

    async submitLogin() {
      try {
        if (!this.forgotPassword) {
          if (!this.loginEmail || !this.loginPassword) {
            alert('Please fill in all required fields');
            return;
          }

          await fetch(this.url + `/login`, {
            method: 'POST',
            headers: {'accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'},
            body: `grant_type=${this.grant_type}&username=${this.loginEmail}&password=${this.loginPassword}&scope=${this.scope}&client_id=${this.client_id}&client_secret=${this.client_secret}`,
            credentials: 'include',
            mode: "no-cors"
          });

          const cookies = document.cookie.split('; ');
          const jwtCookie = cookies.find(cookie => cookie.startsWith('user_auth='));
          const jwt = jwtCookie.split('=')[1];
          localStorage.setItem('jwt', jwt);

          // Wait for 1 second to allow the JWT to be set in localStorage
          await new Promise(resolve => setTimeout(resolve, 0));

          // Redirect to /home after the page reloads
          window.location.href = '/home';

        }
        this.loginEmail = '';
        this.loginPassword = '';
        this.forgotPassword = false;
      } catch (error) {
        console.error(error);
      }
    },
    async resetPassword() {
      try {
        const response = await fetch(this.url + `/forgot-password`, {
          body: JSON.stringify({email:`${this.resetEmail}`}),
          method: 'POST',
          headers: {'Content-Type': 'application/json'},
        });
        if (!response.ok) {
          throw new Error('Password reset request failed');
        }
        console.log('Password reset request successful');
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
    z-index: 2;
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

  align-items: center;
  justify-content: space-around;
  box-sizing: border-box;


  text-align: center;
  background: linear-gradient(to bottom, #efefef, #ccc);
  transition: all .5s ease-in-out;
  height: 100%;

  div {
    font-size: 1rem;
  }

  input, select {
    background-color: #eee;
    border: none;
    padding: 8px 48px 0 10px;
    margin: 12px 4px;
    height: 32px;

    color: gray;
    border-radius: 15px;
    border-bottom: 1px solid #ddd;
    box-shadow: inset 0 1px 2px rgba(0, 0, 0, .4),
    0 -1px 1px #fff,
    0 1px 0 #fff;
    overflow: hidden;
    display: block;
    box-sizing: border-box;
    width: 100%;

    &:focus {
      outline: none;
      background-color: #fff;
    }
  }
}

.sign-in {
  left: -4%;
  z-index: 2;

  padding: 20% 10%;

  a {
    cursor: pointer;
  }

  .reset-password-btn {
    margin: 10px;
  }

}

.sign-in-btn {
  margin-top: 10px;

}

.sign-up {
  top: -5%;
  left: 2%;
  z-index: 1;
  opacity: 0;

  padding: 15% 6.421%;
}

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

.reset-password-btn {
  scale: 70%;
}


.sign-up-btn {
  margin-top: 5px;
}

.forgot-password:hover {
  color: #00afea;
}

.cancel-link:hover {
  color: #00afea;
  cursor: pointer;
}

.cancel-link {

  border-radius: 50px;

}
.verification_window_container {
  display: flex;
  justify-content: center;
  align-items: center;
}

.verification_window {
  background-color: white;
  padding: 20px;
  text-align: center;
}

</style>
