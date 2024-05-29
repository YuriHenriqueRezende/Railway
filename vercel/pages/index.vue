<script setup lang="ts">
import { getLivro } from '~/services/livros';
import { type Livro } from '~/models/livros';
import { type Ref, ref } from 'vue';

enum STATUS {
    P = "Pendente",
    C = "Cancelado(a)",
    A = "Aprovado(a)"
}

enum FORMATOS {
    E = "E-BOOK",
    F = "FISICO"
}

const livros: Ref<Array<Livro>> = ref([])
getLivro().then

const livroteste: Livro = {
    id: 1,
    titulo: "teste",
    descricao: "teste",
    numero_pagina: 1,
    formato: FORMATOS.E,
    numero_edicao: 1,
    autor: "a",
    publicacao: 2021,
    categoriaFK: {
        id: 1,
        nome: "a"
    },
    status: STATUS.P,
    preco: 1,
    fotosFK: [
        "https://m.media-amazon.com/images/I/919dh4AX2hL._SY425_.jpg",
    ],
    quantidade: 2,
}

const atualizarLivro = () => {
    getLivro().then((LivroEncontrado) => {
        console.log("livros encontrados: ", LivroEncontrado?.results);
        livros.value = LivroEncontrado?.results ?? [];
    });
};
atualizarLivro()

const painel = ref();
const toggle = (event: any) => {
    painel.value.toggle(event);
}
</script>

<template>
    <main class="home-container flex flex-column align-items-center">
        <div class="chatbot">
            <Button type="button" icon="pi pi-comment" label="Chatbot" @click="toggle" />
            <OverlayPanel ref="painel">
                <iframe allow="microphone;" width="350" height="430"
                    src="https://console.dialogflow.com/api-client/demo/embedded/6e039547-3682-42f8-896d-1301cbf9970d">
                </iframe>
            </OverlayPanel>
        </div>
        <h2 class="mt-4 mb-4">SERAIVA</h2>
        <div class="grid align-items-center justify-content-center">
            <div v-for="(livro,index) in livros">
                <itemlivro :key="index" class="col-4" :livro="livro"/>
            </div>
        </div>
    </main>
</template>

<style scoped lang="scss">
.home-container {
  margin: 0;
  width: 100vw;
  min-height: calc(100vh - 80px);
  background-color: rgb(255, 255, 255);
  background-image: url("teste.jpg");
  background-repeat: repeat;
  background-size: cover;
}
.chatbot{
    position: fixed;
    top: 0;
    right: 0;
    margin: 1rem
}
</style>

