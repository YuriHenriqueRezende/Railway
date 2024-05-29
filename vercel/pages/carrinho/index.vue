<script setup lang="ts">
import { computed } from "#imports";
import { carrinho, type CarrinhoLivro } from "~/estoque/carrinho";
const { getCarrinho, removertLivroCarrinho, getValorLivro } = carrinho();
import { BACKEND_URL } from "~/models/app";

const itensNoCarrinho: Array<CarrinhoLivro> = getCarrinho();
const valorTotal = computed(()=> getValorLivro());

console.log("itens No carrinho.....", itensNoCarrinho);

const deletarDoCarrinho = (itemParaRemover: CarrinhoLivro)=> {
    removertLivroCarrinho({
        livro: itemParaRemover.livro,
        quantidade: 0
    });
}

const salvarPedido = async ()=> {
  const livrosID = itensNoCarrinho.map(item => item.livro.id);
   useFetch(`${BACKEND_URL}/emprestimos/`, {
    method: 'POST',
    body: { 
      livroFK: livrosID,
      data_inicio: '2024-05-27',
      data_fim: '2024-05-31',
      status: 'E',
      usuarioFK: '7',
    }
  })
  navigateTo('/login/login_emprestimo');
}   

</script>

<template>
  <main class="carrinho-container flex flex-column align-items-center">
    <h2 class="mt-4 mb-4"> Seu carrinho de Emprestimo</h2>
    <table >
        <thead>
            <tr>
              <td>Item</td>
              <td>Livro</td>
              <td>Titulo</td>
              <td>Quantidade</td>
              <td>Preço</td>
              <td>Ações</td>
            </tr>
        </thead>
      <tbody>
        <tr v-for="(itemCarrinho ,index) in itensNoCarrinho" :key="index">
          <td>{{ index }}</td>
          <td><img class="fotoProduto" :src="itemCarrinho.livro.fotosFK[0]" alt="foto produto" /></td>
          <td>{{ itemCarrinho.livro.titulo }}</td>
          <td>{{ itemCarrinho.quantidade }}</td>
          <td>R$ {{ itemCarrinho.quantidade * itemCarrinho.livro.preco }}</td>
          <td>
            <Button @click="deletarDoCarrinho(itemCarrinho)"  label=""><i class="pi pi-trash"></i></Button>
          </td>
        </tr>
        <section class="flex flex-row align-items-center justify-content-center valor-total ">
            <span class="mr-2">Valor Total: </span>
            <span> R${{ valorTotal }}</span>
        </section>
      </tbody>    
    </table>
    <Button @click="salvarPedido" class="mt-2 botao-pedido bg-primary" label="Fechar Emprestimo"></Button>
</main>

</template>

<style scoped lang="scss">
.carrinho-container {
  margin: 0;
  width: 100vw;
  min-height: calc(100vh - 80px);
  background-color: red;
  background-image: url("carrinho.jpg");
  background-repeat: repeat;
  background-size: cover;
}
table{
    background-color: white;
    border-radius: 1rem;
}
thead{
    font-weight: bold;
    tr{
        border-bottom: 2px solid black
    }
}
td{
    padding: 1rem;
}

.fotoProduto{
    width: 50px;
    height: 50px;
}

Button{
    background-color: white;
    color: rgb(114, 15, 15);
    border: none;
}
.valor-total{
    font-weight: bold;
    
}

.botao-pedido{
    width: 250px;
    height: 50px;
}
</style>