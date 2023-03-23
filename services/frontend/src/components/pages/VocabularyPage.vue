<template>
  <table>
    <thead>
    <tr>
      <th>№</th>
      <th>Word</th>
      <th>Translation</th>
      <th style="width:10%">lvl</th>
      <th style="width:15%">Mark as Familiar</th>
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

  <div class="download">
    <button @click="downloadTable" @mouseover="showObject = true">Download File</button>
    <div class="levels" v-if="showObject">
      <div v-for="option in options" :key="option.key">
        <input type="checkbox" :id="option.value" :value="option.value" v-model="levelDownload">
        <label :for="option.value">{{ option.value }}</label>
      </div>
      <button @click="showObject = false">Close</button>
    </div>
  </div>


</template>
<script>
import axios from "axios";

export default {
  data() {
    return {
      options: [
        { key: 1, value: 'A1'},
        { key: 2, value: 'A2'},
        { key: 3, value: 'B1'},
        { key: 4, value: 'B2'},
        { key: 5, value: 'C1'},
        { key: 6, value: 'C2'},
      ],


      words: [],
      searchTerm: '',
      pageSize: 5,
      currentPage: 1,
      showObject: false,
      levelDownload: "B1"
    };
  },
  created() {
    axios.get('http://192.168.1.104:8081/vocabulary')
        .then(response => {
          this.words = response.data;
        })
        .catch(error => {
          console.error(error);
        });
  },
  computed: {
    displayedWords() {
      const filteredWords = this.words.filter(word => {
        return word.word.toLowerCase().includes(this.searchTerm.toLowerCase());
      });
      const startIndex = (this.currentPage - 1) * this.pageSize;
      return filteredWords.slice(startIndex, startIndex + this.pageSize);
    },
    pageCount() {
      return Math.ceil(this.displayedWords.length / this.pageSize);
    }
  },
  methods: {
    downloadTable() {
      const this_url = http://192.168.1.104:8081/vocabulary/download/?user_id=1&level="${this.levelDownload.join(' ')}";

      console.log(this_url);
      axios({
        url: this_url,
        method: 'GET',
        responseType: 'blob',
      }).then((response) => {
        const url = window.URL.createObjectURL(new Blob([response.data]));
        const link = document.createElement('a');
        link.href = url;
        link.setAttribute('download', 'table.xlsx');
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
      });
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


.pagination span {
  background-color: black;
  color: white;
  padding: 5px 10px;
  margin: 0 5px;
}
.download{
  display: inline-block;
}
.levels {
  color: white;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
</style>