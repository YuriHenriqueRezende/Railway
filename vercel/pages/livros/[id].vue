<script setup>

    const route = useRoute();

    const { data: livro } = await useFetch(`http://127.0.0.1:8000/api/auth/livros/${route.params.id}`, {key: 'tripRequest'});
    const { data: autor } = await useFetch (`http://127.0.0.1:8000/api/auth/usuarios/${livro.value.autor}`)
    console.log(livro.value.autor)

</script>


<template>
    <main class="main flex flex-column align-items-center">
        <div class="book-container">
        <h1> {{ livro.titulo }} </h1>
        <img :src="livro.fotosFK" alt="solicitante">
        <p> Descrição: {{ livro.descricao }} </p>
        <p> Numero de Paginas: {{ livro.numero_pagina }} </p>
        <p> Formato: {{ livro.formato }} </p>
        <p> Numero da edição: {{ livro.numero_edicao }} </p>
        <p> Autor: {{ autor.nome }} </p>
        <img :src="autor.foto" alt="solicitante">
        <p> biografia: {{ autor.biografia }} </p>
        <p> Ano de Publicação: {{ livro.publicacao }} </p>
        <p> Preço: {{ livro.preco }} </p>
        <p> Quantidade: {{ livro.quantidade }} </p>
        
    </div>

    </main>

</template>

<style scoped lang="scss">
.main {
margin: 0;
  width: 100vw;
  min-height: calc(100vh - 80px);
  background-color: rgb(255, 255, 255);
  background-image: url("fundo.jpg");
  background-repeat: repeat;
  background-size: cover;
}

.book-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    text-align: center; 
}

.book-title {
    font-size: 2rem;
    margin-bottom: 10px;
    color: #333;
}

.book-image {
    width: 100%;
    max-width: 300px;
    height: auto;
    display: block;
    margin: 0 auto 20px;
    border-radius: 10px;
}

.book-description,
.book-pages,
.book-format,
.book-edition,
.book-author,
.book-publication,
.book-category,
.book-price,
.book-quantity {
    font-size: 1rem;
    margin-bottom: 10px;
    color: #555;
}

.book-description {
    margin-top: 20px;
    font-style: italic;
}

.book-price {
    font-size: 1.5rem;
    font-weight: bold;
    color: #e91e63;
}

</style>