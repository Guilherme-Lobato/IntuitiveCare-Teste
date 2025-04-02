<template>
  <div class="search-container">
    <h2>Busca de Operadoras</h2>
    <input
      v-model="searchTerm"
      @input="handleSearch"
      placeholder="Digite para buscar operadoras..."
      class="search-input"
    />

    <div class="results">
      <table v-if="operadoras.length > 0">
        <thead>
          <tr>
            <th>Registro ANS</th>
            <th>Razão Social</th>
            <th>Nome Fantasia</th>
            <th>Cidade</th>
            <th>UF</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="operadora in operadoras" :key="operadora.Registro_ANS">
            <td>{{ operadora.Registro_ANS }}</td>
            <td>{{ operadora.Razao_Social }}</td>
            <td>{{ operadora.Nome_Fantasia }}</td>
            <td>{{ operadora.Cidade }}</td>
            <td>{{ operadora.UF }}</td>
          </tr>
        </tbody>
      </table>
      <p v-else>Nenhuma operadora encontrada.</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "OperadorasSearch",
  data() {
    return {
      searchTerm: "",
      operadoras: [],
    };
  },
  methods: {
    async handleSearch() {
      try {
        const response = await fetch(
          `http://localhost:8000/api/operadoras?termo=${this.searchTerm}`
        );
        this.operadoras = await response.json();
      } catch {
        this.operadoras = [];
      }
    },
  },
  mounted() {
    this.handleSearch();
  },
};
</script>

<style scoped>
.search-container {
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
}

.search-input {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

th {
  background-color: #f5f5f5;
}

tr:hover {
  background-color: #f9f9f9;
}
</style>
