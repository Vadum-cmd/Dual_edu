<template>
  <div>
    <h1 class="title">Here are your books</h1>
    <div class="books" v-if="books && books.length > 0">
      <h2 class="subtitle">Available Books</h2>
      <ul>
        <li v-for="book in displayedBooks" :key="book.id" class="book-item">{{ book.book_title }}</li>
      </ul>
    </div>
    <div v-else>
      <h2 class="subtitle">No books available</h2>
    </div>
    <div class="pagination">
      <button :disabled="currentPage === 1" @click="currentPage--">Prev</button>
      <span>{{ currentPage }}</span>
      <button :disabled="currentPage === pageCount" @click="currentPage++">Next</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      base_url: process.env.VUE_APP_URL,
      file: null,
      formData: null,
      loading: false,
      books: [],
      isNotLogin: false,
      pageSize: 10,
      currentPage: 1,
    };
  },
  methods: {
    fetchBooks() {
      const jwt = localStorage.getItem("jwt");
      axios
          .get(this.base_url + `/books`, {
            headers: {
              Cookie: jwt,
            },
            withCredentials: true,
          })
          .then((response) => {
            this.books = response.data;
          })
          .catch((error) => {
            console.error("There was an error!", error);
          });
    },
  },
  computed: {
    displayedBooks() {
      const startIndex = (this.currentPage - 1) * this.pageSize;
      const endIndex = startIndex + this.pageSize;
      return this.books.slice(startIndex, endIndex);
    },
    pageCount() {
      return Math.ceil(this.books.length / this.pageSize);
    },
  },
  created() {
    this.fetchBooks();
  },
};
</script>

<style scoped>
.title {
  font-size: 3rem;
  font-weight: bold;
  color: #969696;
  margin-bottom: 2rem;
}

.subtitle {
  font-size: 2rem;
  color: #888;
  margin-top: 2rem;
  margin-bottom: 1rem;
}

.books {
  border: 2px solid #eee;
  padding: 2rem;
  border-radius: 5px;
  margin-bottom: 2rem;
}

ul {
  color: lightslategray;
}

.book-item {
  font-size: 1.5rem;
  margin-bottom: 1rem;
}
</style>
