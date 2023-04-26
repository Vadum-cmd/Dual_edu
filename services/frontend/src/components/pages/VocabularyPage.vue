<template>
  <table>
    <thead>
    <tr>
      <th class="number">№</th>
      <th class="word">Word</th>
      <th class="translation">Translation</th>
      <th class="level" style="width:10%">lvl</th>
    </tr>
    </thead>
    <tbody>
    <tr v-for="(word, index) in displayedWords" :key="word.id">
      <td class="number">{{ (currentPage - 1) * pageSize + index + 1 }}</td>
      <td>{{ word.word }}</td>
      <td>{{ word.translation }}</td>
      <td class="level">{{ word.word_level }}</td>
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
      pageSize: 10,
      currentPage: 1,
      showObject: false,
      levelDownload:[],
      url:process.env.VUE_APP_URL
    };
  },
  created() {
    const jwt = localStorage.getItem("jwt");
    axios.get(this.url+`/vocabulary`,{
      headers: {
        'Cookie': jwt,
      },
      withCredentials: true,
    })
        .then(response => {
          this.words = response.data;

        })
        .catch(error => {
          console.error(error);
        });
  },
  computed: {
    displayedWords() {
      const startIndex = (this.currentPage - 1) * this.pageSize;
      const endIndex = startIndex + this.pageSize;
      return this.words.slice(startIndex, endIndex);
    },
    pageCount() {
      return Math.ceil(this.words.length / this.pageSize);
    }
  },
  methods: {
    async downloadTable() {
      const jwt = localStorage.getItem("jwt");
      const levels_str = this.levelDownload.join(' ');
      const url = this.url+`/vocabulary/download/?levels_str=${levels_str}`;

      try {
        const response = await axios.get(url, {
          headers: {
            'Accept-Language': 'en,ru-RU;q=0.9,ru;q=0.8,en-US;q=0.7,uk;q=0.6',
            'Connection': 'keep-alive',
            'Cookie': jwt,
            'Referer': 'http://192.168.1.103:8081/docs',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
            'accept': 'application/json'
          },
          responseType: 'blob',
          withCredentials: true,
        });

        const url1 = window.URL.createObjectURL(response.data);
        const link = document.createElement('a');
        link.href = url1;
        link.setAttribute('download', 'table.xlsx');
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
      } catch (error) {
        console.log(error);
      }
    },
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
.download{
  display: inline-block;
}
.levels {
  color: white;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}
@media (max-width: 1225px){
  .level{
    display: none;
  }
  .number{
    display: none;
  }
  table{
    width: 100%;
  }
}
</style>
