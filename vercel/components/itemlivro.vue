<script setup lang="ts">
import { ref } from 'vue';
import { type Livro } from '~/models/livros';
import { carrinho } from "~/estoque/carrinho";

// Busca os livros da API
const { data: error } = await useFetch<Livro[]>('http://127.0.0.1:8000/api/auth/livros');

const { adicionar, getCarrinho } = carrinho();

type propType = {
    livro: Livro;
}

const props = defineProps<propType>();

// Estado para verificar se o item foi adicionado ao carrinho
const itemAdicionado = ref(false);

const adicionarItem = () => {
    adicionar(props.livro);
    itemAdicionado.value = true;
    console.log("CARRINHO ATUAL: ", getCarrinho());
}

// Verifica se há um erro na requisição
if (error.value) {
    console.error('Erro ao buscar livros:', error.value);
}
</script>


<template>
    <section class="cartao flex flex-column align-items-center justify-content-center" v-if="props.livro">
        <div class="livro-imagem">
            <NuxtLink :to="`/livros/${props.livro.id}`">
                <img :src="props.livro.fotosFK[0]" alt="Imagem do Livro"/>
            </NuxtLink>
        </div>
        <div>
            <h4>{{ props.livro.titulo }}</h4>
        </div>
        <div class="flex flex-row">
            <span>R${{ props.livro.preco }} - </span>
            <div class="ml-2">
                <label>Qtd. Disponível: </label>
                <span>{{ props.livro.quantidade }}</span>
            </div>
        </div>
        <Button @click="adicionarItem" class="botao-add" label="Adicionar"/>
        <div v-if="itemAdicionado" class="checkbox-container">
            <label>
                <input type="checkbox" checked disabled> Adicionado ao Carrinho
            </label>
        </div>
    </section>
</template>


<style scoped lang="scss">
.cartao {
    width: 300px;
    height: 400px;
    background-color: white;
    border-radius: 1.5rem;
    margin: 1.5rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

.livro-imagem {
    width: 100%;
    height: 65%;
    max-width: 250px;
    max-height: 250px;
    img {
        width: 100%;
        height: 100%;
    }
}

.flex {
    display: flex;
}

.flex-column {
    flex-direction: column;
}

.flex-row {
    flex-direction: row;
}

.align-items-center {
    align-items: center;
}

.justify-content-center {
    justify-content: center;
}

.ml-2 {
    margin-left: 0.5rem;
}

.botao-add {
    width: 80%;
    height: 2rem;
    margin: 1rem;
}

.checkbox-container {
    margin-top: 1rem;
    label {
        font-size: 1rem;
        color: #555;
    }
    input[type="checkbox"] {
        margin-right: 0.5rem;
    }
}
</style>
