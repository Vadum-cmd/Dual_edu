<template>
  <div class="profile-page">
    <div class="avatar-container">
      <div class="avatar-wrapper"><img class="avatar" :src="avatarUrl" alt="Avatar"></div>
    </div>
    <div class="nickname-container"><h2 class="nickname">{{ nickname }}</h2></div>
    <div class="xp-bar">
      <div class="progress" :style="{ width: xpPercentage }"> Level {{ level }} - {{ xp }}/{{ xpToNextLevel }} XP</div>
    </div>
    <div class="profile-lines">
      <div class="profile-line"><h3>Your goal:</h3>
        <p>{{ goal }}</p></div>
      <div class="profile-line"><h3>Your english level:</h3>
        <p>{{ englishLevel }}</p></div>
      <div class="profile-line"><h3>Your native language:</h3>
        <p>{{ nativeLanguage }}</p></div>
      <div class="profile-line"><h3>Your email:</h3>
        <p>{{ email }}</p></div>
    </div>
  </div>
</template>
<script>export default {
  name: "ProfilePage",
  data() {
    return {
      avatarUrl: "https://img.freepik.com/free-vector/cute-cat-gaming-cartoon_138676-2969.jpg?w=826&t=st=1677163950~exp=1677164550~hmac=d8a31715c4c9cfd71e82ff5b33d305e7b88eb649c0c5a79d1eba2f01203ae84d",
      nickname: "John",
      level: 5,
      xp: 120,
      xpToNextLevel: 200,
      goal: "Reach level C4.",
      englishLevel: "A1",
      nativeLanguage: "Spanish",
      email: "john.down@example.com"
    };
  }, computed: {
    xpPercentage() {
      return `${Math.floor((this.xp / this.xpToNextLevel) * 100)}%`;
    }
  }
};</script>
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
  width: 100%;
  height: 100%;
  object-fit: cover;
  scale: 200%;
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
  height: 25px;
  background-color: #ddd;
  margin-bottom: 20px;
}

.progress {
  height: 100%;
  background-color: #666;
  color: white;
  display: flex;
  justify-content: center;
  align-items: center;
  font-weight: bold;
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
