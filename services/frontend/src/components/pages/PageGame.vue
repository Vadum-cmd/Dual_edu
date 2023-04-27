<template>
  <div class="container">
    <h1 class="title">Translation Challenge</h1>
    <p v-if="gameOver" class="score">Game Over! Your final score is {{ score }}.</p>
    <p v-else class="question">Translate the following word:</p>
    <div v-if="!gameOver" class="form-group">
      <p class="translation">{{ translation }}</p>
      <input type="text" class="form-control" v-model="guess" @keyup.enter="checkAnswer"/>
      <p v-if="attemptsLeft > 0" class="attempts">{{ attemptsLeft }} attempts left.</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      translation: null,
      guess: "",
      attemptsLeft: 3,
      score: 0,
      gameOver: false,
      book_id: null,
      url: process.env.VUE_APP_URL,
      jwt: localStorage.getItem('jwt')
    };
  },
  methods: {
    getNextWord() {
      axios.get(this.url + '/test', {
        headers: {
          'Cookie': this.jwt
        },
        withCredentials: true,
      }).then(response => {
        this.translation = response.data.word.word;
        this.book_id = response.data.book_id;
      }).catch(error => {
        console.log(error);
      });
    },
    checkAnswer() {
      if (this.attemptsLeft <= 1) {
        this.gameOver = true;
      }

      return axios.post(`${this.url}/test?en_word=${this.translation}&answer=${this.guess}&book_id=${this.book_id}`, {},
          {
            headers: {
              'Cookie': this.jwt,
            },
            withCredentials: true,
          }
      )
          .then(response => {
            if (response.status >= 200 && response.status < 300) {
              return response.data;
            } else {
              throw new Error('Network response was not ok');
            }
          })
          .then(data => {
            this.guess='';
            if (data.result) {
              this.score++;
              this.getNextWord();

            } else {
              this.attemptsLeft--;
              if (this.attemptsLeft === 0) {
                this.getNextWord();
              }
            }
          })
          .catch(error => {
            console.error(error);
          });

    }

  },
  mounted() {
    this.getNextWord();

  }
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
