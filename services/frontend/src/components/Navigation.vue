<template>
  <header :class="{ 'scrolled-nav': scrolledNav}">
    <nav>
      <div class="branding">
        <div class="h">Re&joy</div>
      </div>
      <ul v-show="!mobile" class="navigation">
        <li>
          <router-link class="link" to="/">
            <font-awesome-icon icon="fa-solid fa-book-open"/>
            Books
          </router-link>
        </li>
        <li>
          <router-link class="link" to="/vocabulary">
            <font-awesome-icon icon="fa-solid fa-clipboard"/>
            My vocabulary
          </router-link>
        </li>
        <li v-if="isAutorize">

          <div class="profile">
            <div class="nickname">
              <font-awesome-icon icon="fa-solid fa-circle" style="scale: 300%; margin-right: 15px"/>
              Nickname

            </div>

            <div class="dropdown">
              <button @click="toggle()">
                <font-awesome-icon icon="fa-solid fa-square-caret-down"/>
              </button>
              <div class="dropdown-content" v-if="active">
                <router-link class="drop_menu" to="/profile">
                  <font-awesome-icon icon="fa-solid fa-user"/>
                  Profile
                </router-link>
                <router-link class="drop_menu" to="/settings">
                  <font-awesome-icon icon="fa-solid fa-gear"/>
                  Settings
                </router-link>
                <router-link class="drop_menu" to="/test">
                  <font-awesome-icon icon="fa-solid fa-puzzle-piece"/>
                  Game
                </router-link>
                <router-link class="drop_menu" to="/" @click="logout">
                  <font-awesome-icon icon="fa-solid fa-circle-xmark"/>
                  Logout
                </router-link>
              </div>
            </div>
          </div>
        </li>
        <li v-else>
          <router-link class="link" to="/login">
            <font-awesome-icon icon="fa-solid fa-arrow-right-to-bracket"/>
            Login
          </router-link>
        </li>

      </ul>
      <div class="icon">
        <i @click="toggleMobileNav" v-show="mobile" class="" :class="{'icon-active': mobileNav}">
          <font-awesome-icon icon="fa-solid fa-bars"/>
        </i>

      </div>
      <transition name="mobile-nav">
        <ul v-show="mobileNav" class="dropdown-nav">
          <li>
            <router-link class="link" to="/">
              <font-awesome-icon icon="fa-solid fa-book-open"/>
              Books
            </router-link>
          </li>
          <li>
            <router-link class="link" to="/vocabulary">
              <font-awesome-icon icon="fa-solid fa-clipboard"/>
              My vocabulary
            </router-link>
          </li>
          <li v-if="isAutorize">

            <div class="profile">
              <div class="nickname">
                <font-awesome-icon icon="fa-solid fa-circle" style="scale: 300%; margin-right: 15px"/>
                Nickname

              </div>

              <div class="dropdown">
                <button @click="toggle()">
                  <font-awesome-icon icon="fa-solid fa-square-caret-down"/>
                </button>
                <div class="dropdown-content" v-if="active">
                  <router-link class="drop_menu" to="/profile">
                    <font-awesome-icon icon="fa-solid fa-user"/>
                    Profile
                  </router-link>
                  <router-link class="drop_menu" to="/settings">
                    <font-awesome-icon icon="fa-solid fa-gear"/>
                    Settings
                  </router-link>
                  <router-link class="drop_menu" to="/test">
                    <font-awesome-icon icon="fa-solid fa-puzzle-piece"/>
                    Game
                  </router-link>
                  <router-link class="drop_menu" to="/" @click="logout">
                    <font-awesome-icon icon="fa-solid fa-circle-xmark"/>
                    Logout
                  </router-link>
                </div>
              </div>
            </div>
          </li>
          <li v-else>
            <router-link class="link" to="/login">
              <font-awesome-icon icon="fa-solid fa-arrow-right-to-bracket"/>
              Login
            </router-link>
          </li>

        </ul>
      </transition>
    </nav>
  </header>

</template>

<script>



import router from "@/components/router";

export default {

  name: "Navig-ation",
  data() {
    return {
      scrolledNav: null,
      mobile: null,
      mobileNav: null,
      windowWidth: null,
      active: false,
      isAutorize: false
    }
  },
  created() {
    window.addEventListener('resize', this.checkScreen)
    this.checkScreen()

  },
  mounted() {
    const jwt = localStorage.getItem("jwt");

    this.isAutorize = jwt !== 'null';

    window.addEventListener('scroll', this.updateScroll);
  },
  methods: {
    toggleMobileNav() {
      this.mobileNav = !this.mobileNav;
    },
    updateScroll() {
      const scrollPosition = window.scrollY;
      if (scrollPosition > 50) {
        this.scrolledNav = true;
        return;
      }
      this.scrolledNav = false;
    },
    checkScreen() {
      this.windowWidht = window.innerWidth;
      if (this.windowWidht <= 750) {
        this.mobile = true;
        return;
      }
      this.mobile = false;
      this.mobileNav = false;
      return;
    },
    toggle() {
      this.active = !this.active
    },
    logout() {
      localStorage.removeItem('jwt');
      this.isAutorize=false;
      location.reload();
      router.push('/login');
    }
  }


}

</script>

<style lang="scss" scoped>
header {
  background-color: rgba(0, 0, 0, 0.8);
  z-index: 99;
  width: 100%;
  position: fixed;
  transition: 0.5s ease all;
  color: #fff;

  nav {
    position: relative;
    display: flex;
    flex-direction: row;
    padding: 12px 0;
    transition: 0.5s ease all;
    width: 90%;
    margin: 0 auto;
    @media (min-width: 1140px) {
      max-width: 1140px;
    }

    ul,
    .link {
      color: #fff;
      list-style: none;
      text-decoration: none;
    }

    li {
      text-transform: uppercase;
      padding: 16px;
      margin-left: 16px;
    }

    .link {
      font-size: 14px;
      transition: 0.5s ease all;
      padding-bottom: 4px;
      border-bottom: 1px solid transparent;

      &:hover {
        color: #00afea;
        border-color: #00afea;

      }
    }

    .nickname {
      font-size: 14px;
    }

    .profile {
      position: relative;
      display: inline-flex;

    }

    .dropdown button {
      scale: 130%;
      margin-left: 10px;
    }

    .dropdown button:hover {
      color: #00afea;
    }

    .dropdown {
      margin-left: 5px;
      position: relative;
      display: inline-block;
    }

    .dropdown-content {
      display: block;
      position: absolute;
      background-color: #656565;
      min-width: 130px;
      box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
      z-index: 1;
      margin-top: 9px;
    }


    .dropdown-content .drop_menu {
      color: black;
      padding: 12px 16px;
      text-decoration: none;
      display: block;

    }


    .dropdown-content .drop_menu:hover {
      background-color: #f1f1f1
    }


    .branding {
      display: flex;
      align-items: center;
    }

    .navigation {
      display: flex;
      align-items: center;
      flex: 1;
      justify-content: flex-end;
    }

    .icon {
      display: flex;
      align-items: center;
      position: absolute;
      top: 0;
      right: 24px;
      height: 100%;

      i {
        cursor: pointer;
        font-size: 24px;
        transition: .8s ease all;
      }

      .icon-active {
        transform: rotate(180deg);
      }

      .dropdown-nav {
        display: flex;
        flex-direction: column;
        position: fixed;
        width: 100%;
        max-width: 250px;
        height: 100%;
        background-color: white;
        top: 0;
        left: 0;

        li {
          margin-left: 0;

          .link {
            color: black;
          }
        }
      }
    }

    .mobile-nav-enter-active,
    .mobile-nav-leave-active {
      transition: 1s ease all;
    }

    .mobile-nav-enter-from,
    .mobile-nav-leave-to {
      transform: translateX(-250px);
    }

    .mobile-nav-enter-to {
      transform: translateX(0);
    }
  }
}

.scrolled-nav {
  background-color: black;
  box-shadow: - 4px 6px -1px rgba(0, 0, 0, 0.1), 0, 2px, 4px, -1px, rgba(0, 0, 0, 0.6);

  nav {
    padding: 8px 0;

    .branding {
      .h {
        width: 40px;
        box-shadow: - 4px 6px -1px rgba(0, 0, 0, 0.1), 0, 2px, 4px, -1px, rgba(0, 0, 0, 0.6);
      }
    }
  }
}
</style>
