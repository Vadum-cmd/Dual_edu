<template>
  <div class="board">
    <div class="slider">
      <transition-group name="slide" tag="div">
        <div v-for="(slide, index) in filteredSlides" :key="index" class="slide-container">
          <h2 class="slide-title">{{ slide.title }}</h2>
          <p class="slide-text">{{ slide.text }}</p>
        </div>
      </transition-group>
      <div class="dots">
        <span v-for="(slide, index) in slides" :key="index" :class="{ active: currentSlideIndex === index }" @click="currentSlideIndex = index"></span>
      </div>
      <button class="prev-btn" @click="prevSlide">&#8249;</button>
      <button class="next-btn" @click="nextSlide">&#8250;</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentSlideIndex: 0,
      slides: [
        {
          title: "Introducing our Website",
          text: "Welcome to our website dedicated to helping people read books in a language other than their own. Our platform is designed to make it easier for you to enjoy books in English, regardless of your language proficiency level."
        },
        {
          title: "How It Works",
          text: "Our website works in a simple and effective way. First, you can upload a book in English and indicate your level of proficiency in the language. Then, as you read, our platform will automatically detect potentially unknown words and translate them for you. This way, you can focus on enjoying the story without worrying about language barriers."
        },
        {
          title: "Personalized Dictionary",
          text: "Our platform also creates a personalized dictionary for you based on the words you encounter while reading. This dictionary can be accessed at any time, allowing you to review the words you learned and improve your vocabulary in English."
        },
        {
          title: "Learning Games",
          text: "To make learning even more fun, our platform offers a game that is based on the words in your personalized dictionary. You can play games that help you learn new words and retain them for future use."
        },
        {
          title: "Free to Use",
          text: "And the best part is that our website is completely free to use! All you need to do is register on our website to gain access to all these amazing features and tools."
        },
        {
          title: "Call to Register",
          text: "So why wait? Join our community of language learners and start reading books in English like a pro! Register now on our website and start exploring the world of English literature."
        }
      ],
      isNotAutorize:false
    };
  },
  computed: {
    filteredSlides() {
      const slideCount = 1; // Number of slides to show at a time
      const startIndex = this.currentSlideIndex;
      const endIndex = (this.currentSlideIndex + slideCount - 1) % this.slides.length;
      if (startIndex <= endIndex) {
        return this.slides.slice(startIndex, endIndex + 1);
      } else {
        return this.slides.slice(startIndex).concat(this.slides.slice(0, endIndex + 1));
      }
    }
  },
  methods: {
    prevSlide() {
      this.currentSlideIndex =
          this.currentSlideIndex === 0
              ? this.slides.length - 1
              : this.currentSlideIndex - 1;
    },
    nextSlide() {
      this.currentSlideIndex =
          this.currentSlideIndex === this.slides.length - 1? 0: this.currentSlideIndex + 1;
    }
  },
  mounted() {
    const jwt = localStorage.getItem('jwt')
    if(jwt!=null && this.isNotAutorize===false){
      localStorage.removeItem('jwt');
      this.isNotAutorize=true;
      window.location.reload()
    }
  }
};
</script>

<style>
.board {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0,0,0,0.3);
}

.slider {
  position: relative;
  width: 60%;
  height: 60%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.slide-container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.slide-title {
  font-size: 2.5rem;
  font-weight: bold;
  color: #dddddd;
}

.slide-text {
  font-size: 1.5rem;
  font-weight: 300;
  color: #dddddd;
  margin-top: 1rem;
}

.dots {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 2rem;
}

.dots span {
  display: block;
  width: 1rem;
  height: 1rem;
  border-radius: 50%;
  margin: 0 0.5rem;
  background-color: #ccc;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.dots span.active {
  background-color: white;
}

.prev-btn,
.next-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  width: 3rem;
  height: 3rem;
  border: none;
  border-radius: 50%;
  background-color: rgba(255,255,255,0.8);
  font-size: 2rem;
  color: #333;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.prev-btn:hover,
.next-btn:hover {
  background-color: rgba(255,255,255,0.9);
}

.prev-btn {
  left: -4.5rem;
}

.next-btn {
  right: -4.5rem;
}

.indicator {
  position: absolute;
  bottom: 0;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 1rem;
}

.indicator span {
  display: block;
  width: 0.5rem;
  height: 0.5rem;
  background-color: #ccc;
  border-radius: 50%;
  margin: 0 0.5rem;
  transition: background-color 0.3s ease;
}

.indicator span.active {
  background-color: #333;
}
</style>

