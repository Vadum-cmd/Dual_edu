<template>
  <div class="profile-page">
    <div v-if="level <= 10" class="avatar-container">
      <img class="avatar" src="../avatars/avatar2.png" alt="Avatar">
    </div>
    <div v-else class="avatar-container">
      <img class="avatar" src="../avatars/avatar1.png" alt="Avatar">
    </div>

    <div class="nickname-container"><h2 class="nickname">{{ nickname }}</h2></div>
    <div class="xp-bar">
      <div class="progress" :style="{ width: xpPercentage }"> {{ xp }}/{{ xpToNextLevel }} XP</div>
    </div>
    <div>
      Level {{level}}
    </div>
    <div class="profile-lines">
      <div class="profile-line"><h3>Your goal:</h3>
        <p>{{ goal.toUpperCase() }}</p></div>
      <div class="profile-line"><h3>Your english level:</h3>
        <p>{{ englishLevel.toUpperCase() }}</p></div>
      <div class="profile-line"><h3>Your native language:</h3>
        <p>{{ nativeLanguage }}</p></div>
      <div class="profile-line"><h3>Your email:</h3>
        <p>{{ email }}</p></div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: "ProfilePage",
  data() {
    return {
      imagePath:'',
      nickname: "",
      level: null,
      xp: null,
      xpToNextLevel: null,
      goal: "",
      englishLevel: "",
      nativeLanguage: "",
      email: "",
      url:process.env.VUE_APP_URL
    };
  },
  computed: {
    xpPercentage() {
      return `${Math.floor((this.xp / this.xpToNextLevel) * 100)}%`;
    },
  },
  created() {
    const jwt = localStorage.getItem("jwt");
    axios.get(this.url+`/profile`,{
      headers: {
        'Cookie': jwt,
      },
      withCredentials: true,
    })
        .then(response => {
          const data = response.data;
          this.nickname = data.user_name;
          this.level = Math.floor(data.experience / 100)+1 ;
          this.xp = data.experience % 100;
          this.xpToNextLevel = 100 ;
          this.goal = data.goal_level;
          this.englishLevel = data.user_level;
          this.nativeLanguage = data.native_language;
          this.email = data.email;
        })
        .catch(error => {
          console.log(error);
        });
  }
};
</script>
<style scoped>
.profile-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #f4f4f4;
  padding: 30px;
  width: 70vh;
  border-radius: 30%;
}

.avatar-container {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}
.avatar-wrapper {
  border: 5px solid #575454;
  width: 100px;
  height: 100px;
  border-radius: 50%;
  overflow: hidden;
}
.avatar {
  width: 50%;
  height: 50%;
  object-fit: cover;

}
.nickname-container {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
  width: 100%;
}
.nickname {
  margin: 0;
  font-family: Arial, sans-serif;
  text-align: center;
}
.xp-bar {
  width: 80%;
  height: 28px;
  background-color: #cecece;
  margin-bottom: 20px;
  border-radius: 25px;
}
.progress {
  height: 100%;
  background-color: #595959;
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: bold;
  font-size: 12px;
  border-radius: 25px;
}
.profile-lines {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  width: 100%;
}
.profile-line {
  width: 100%;
  margin-bottom: 20px;
}
.profile-line h3 {
  margin: 0;
  font-family: Arial, sans-serif;
}
.profile-line p {
  margin: 0;
  font-family: Arial, sans-serif;
  color: #666;
  line-height: 1.5;
}</style>