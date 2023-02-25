<template>
  <div class="container">
    <h1 class="title">Translation Challenge</h1>
    <p v-if="gameOver" class="score">Game Over! Your final score is {{ score }}.</p>
    <p v-else class="question">Translate the following word:</p>
    <div v-if="!gameOver" class="form-group">
      <p class="translation">{{ translation }}</p>
      <input type="text" class="form-control" v-model="guess" @keyup.enter="checkAnswer" />
      <p v-if="attemptsLeft > 0" class="attempts">{{ attemptsLeft }} attempts left.</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      translations: [
        { translation: "Кіт", keyword: "cat" },
        { translation: "Пeс", keyword: "dog" },
        { translation: "Тато", keyword: "father" },
        { translation: "Мама", keyword: "mother" },
        { translation: "Живородний", keyword: "viviparous" },
      ],
      currentQuestion: 0,
      guess: "",
      attemptsLeft: 3,
      score: 0,
      gameOver: false,
    };
  },
  computed: {
    translation() {
      return this.translations[this.currentQuestion].translation;
    },
  },
  methods: {
    checkAnswer() {
      const currentTranslation = this.translations[this.currentQuestion];
      if (this.guess === currentTranslation.keyword) {
        this.score++;
        this.currentQuestion++;
        this.guess = "";
        this.attemptsLeft = 3;
      } else {
        this.attemptsLeft--;
        if (this.attemptsLeft === 0) {
          this.currentQuestion++;
          this.guess = "";
          this.attemptsLeft = 3;
        }
      }
      if (this.currentQuestion === this.translations.length) {
        this.gameOver = true;
      }
    },
  },
};
</script>
<style>
.container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f2f2f2;
  border-radius: 5px;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.2);
}

.title {
  font-size: 2.5rem;
  margin-bottom: 20px;
  text-align: center;
}

.score {
  font-size: 1.5rem;
  text-align: center;
  margin-bottom: 20px;
}

.question {
  text-align: center;
  font-size: 1.5rem;
  margin-bottom: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.translation {
  font-size: 2rem;
  font-weight: bold;
  margin-bottom: 20px;
}

.form-control {
  font-size: 1.5rem;
  padding: 10px;
  border: none;
  border-radius: 5px;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.2);
  margin-bottom: 20px;
  text-align: center;
}

.attempts {
  font-size: 1.2rem;
  margin-top: 5px;
}
</style>