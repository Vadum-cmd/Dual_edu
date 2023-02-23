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
          translation: 'Not aware or concerned about what is happening',
          lvl: 'B2',
          familiar: false
        },
        {id: 16, word: 'Pensive', translation: 'Engaged in deep or serious thought', lvl: 'B2', familiar: false},
        {
          id: 17,
          word: 'Quintessential',
          translation: 'The most perfect or typical example of a quality or class',
          lvl: 'C1',
          familiar: false
        },
        {
          id: 18,
          word: 'Rancorous',
          translation: 'Characterized by bitterness or resentment',
          lvl: 'C1',
          familiar: false
        },
        {
          id: 19,
          word: 'Sycophant',
          translation: 'A person who acts obsequiously towards someone important in order to gain advantage',
          lvl: 'C1',
          familiar: false
        },
        {
          id: 20,
          word: 'Taciturn',
          translation: 'Reserved or uncommunicative in speech; saying little',
          lvl: 'B2',
          familiar: false
        },
        {
          id: 21,
          word: 'Ubiquitous',
          translation: 'Present, appearing, or found everywhere',
          lvl: 'C1',
          familiar: false
        },
        {
          id: 22,
          word: 'Vex',
          translation: 'Make (someone) feel annoyed, frustrated, or worried, especially with trivial matters',
          lvl: 'C1',
          familiar: false
        },
        {
          id: 23,
          word: 'Wily',
          translation: 'Skilled at gaining an advantage, especially deceitfully',
          lvl: 'C1',
          familiar: false
        },
        {
          id: 24,
          word: 'Xenophobia',
          translation: 'Dislike of or prejudice against people from other countries',
          lvl: 'C1',
          familiar: false
        },
        {
          id: 25,
          word: 'Yoke',
          translation: 'A wooden crosspiece that is fastened over the necks of two animals and attached to the plow or cart that they are to pull',
          lvl: 'C1',
          familiar: false
        }, {
          id: 26,
          word: 'Zealous',
          translation: 'Having or showing zeal, great energy or enthusiasm in pursuit of a cause or an objective',
          lvl: 'B2',
          familiar: false
        },
      ],
      searchTerm: '',
      currentPage: 1,
      pageSize: 12,
    };
  },
  computed: {
    filteredWords() {
      return this.words.filter((word) =>
          word.word.toLowerCase().includes(this.searchTerm.toLowerCase())
      );
    },
    pageCount() {
      return Math.ceil(this.filteredWords.length / this.pageSize);
    },
    displayedWords() {
      const startIndex = (this.currentPage - 1) * this.pageSize;
      return this.filteredWords.slice(startIndex, startIndex + this.pageSize);
    },
  },
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

/* Styles for the current page indicator */
.pagination span {
  background-color: black;
  color: white;
  padding: 5px 10px;
  margin: 0 5px;
}
</style>