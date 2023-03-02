<template>
<div>
<input type="text" v-model="searchTerm" placeholder="Search words...">
<table>
  <thead>
  <tr>
    <th>№</th>
    <th>Word</th>
    <th>Translation</th>
    <th>lvl</th>
    <th>Mark as Familiar</th>
  </tr>
  </thead>
  <tbody>
  <tr v-for="(word, index) in displayedWords" :key="word.id">
    <td>{{ (currentPage - 1) * pageSize + index + 1 }}</td>
    <td>{{ word.word }}</td>
    <td>{{ word.translation }}</td>
    <td>{{ word.lvl }}</td>
    <td><input type="checkbox" v-model="word.familiar"></td>
  </tr>
  </tbody>
</table>
<div class="pagination">
  <button :disabled="currentPage === 1" @click="currentPage--">Prev</button>
  <span>{{ currentPage }}</span>
  <button :disabled="currentPage === pageCount" @click="currentPage++">Next</button>
</div>
</div>
</template>
<script>
export default {
  data() {
    return {
      words: [
        {id: 1, word: 'Abate', translation: 'To decrease in intensity or amount', lvl: 'A1', familiar: false},
        {id: 2, word: 'Benevolent', translation: 'Kind and generous', lvl: 'B2', familiar: false},
        {id: 3, word: 'Cacophony', translation: 'Harsh, unpleasant sound', lvl: 'A1', familiar: false},
        {id: 4, word: 'Divergent', translation: 'Moving apart from a common point', lvl: 'B2', familiar: false},
        {id: 5, word: 'Ephemeral', translation: 'Lasting for a short time', lvl: 'C1', familiar: false},
        {id: 6, word: 'Fastidious', translation: 'Very attentive to detail', lvl: 'C1', familiar: false},
        {id: 7, word: 'Gregarious', translation: 'Sociable and outgoing', lvl: 'B2', familiar: false},
        {id: 8, word: 'Histrionic', translation: 'Overly dramatic or theatrical', lvl: 'C1', familiar: false},
        {
          id: 9,
          word: 'Iconoclast',
          translation: 'Someone who attacks established beliefs or institutions',
          lvl: 'C1',
          familiar: false
        },
        {id: 10, word: 'Jocular', translation: 'Joking or humorous', lvl: 'B2', familiar: false},
        {id: 11, word: 'Kismet', translation: 'Fate or destiny', lvl: 'C1', familiar: false},
        {id: 12, word: 'Luminous', translation: 'Bright or shining', lvl: 'B1', familiar: false},
        {id: 13, word: 'Mendacious', translation: 'Not telling the truth', lvl: 'C1', familiar: false},
        {id: 14, word: 'Nefarious', translation: 'Evil or immoral', lvl: 'C1', familiar: false},
        {
          id: 15,
          word: 'Oblivious',
          translation: 'Not aware or concerned about what is happening', lvl: 'B2',
          familiar: false
        },
        {id: 16, word: 'Panacea', translation: 'A solution or remedy for all problems', lvl: 'C1', familiar: false},
        {id: 17, word: 'Quintessential', translation: 'The most typical or ideal example', lvl: 'C1', familiar: false},
        {id: 18, word: 'Rancor', translation: 'Bitterness or resentment', lvl: 'C1', familiar: false},
        {id: 19, word: 'Sycophant', translation: 'Someone who flatters to gain advantage', lvl: 'C1', familiar: false},
        {id: 20, word: 'Truculent', translation: 'Aggressively defiant or hostile', lvl: 'C1', familiar: false}
      ],
      searchTerm: '',
      currentPage: 1,
      pageSize: 10,
      familiarWords: [],
    };
  },
  computed: {
    filteredWords() {
      if (!this.searchTerm) {
        return this.words;
      }
      return this.words.filter(word => {
        return word.word.toLowerCase().includes(this.searchTerm.toLowerCase()) ||
            word.lvl.toLowerCase().includes(this.searchTerm.toLowerCase());
      });
    },
    pageCount() {
      return Math.ceil(this.filteredWords.length / this.pageSize);
    },
    displayedWords() {
      const startIndex = (this.currentPage - 1) * this.pageSize;
      const endIndex = startIndex + this.pageSize;
      return this.filteredWords.slice(startIndex, endIndex);
    }
  },
  watch: {
    filteredWords() {
      this.currentPage = 1;
    },
    words: {
      handler() {
        this.familiarWords = this.words.filter(word => word.familiar);
      },
      deep: true
    }
  }
};
</script>

<style lang="scss">
table {
  width: 150vh;
  margin-top: 20px;
  background-color: white;

  th, td {
    padding: 10px;
    text-align: left;
    border: 1px solid #ccc;
  }

  th {
    background-color: #f1f1f1;
    font-weight: bold;
  }

  tbody tr:hover {
    background-color: #f5f5f5;
  }
}


input[type="text"] {
  padding: 10px;
  width: 100%;
  margin-top: 50px;
  margin-bottom: 5px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;

  &:focus {
    outline: none;
    border-color: #66afe9;
    box-shadow: 0 0 5px #66afe9;
  }
}

.pagination {
  margin-left: 42%;
  margin-top: 12px;
}

.pagination button {
  background-color: white;
  border: 1px solid black;
  padding: 5px 10px;
  margin: 0 5px;
  cursor: pointer;
}


.pagination span {
  background-color: black;
  color: white;
  padding: 5px 10px;
  margin: 0 5px;
}
</style>
