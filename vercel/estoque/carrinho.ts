import type { Livro } from "~/models/livros";

export type CarrinhoLivro = {
    livro: Livro;
    quantidade: number;
}

export type Carrinho = {
    livros: Array<CarrinhoLivro>;
}
 
export const carrinho = defineStore('CarrinhoStore',{
    state: (): Carrinho => ({
        livros: []
    }),
    actions:{
        adicionar(novoLIvro: Livro){
            const livroExistente = this.getLivroCarrinho(novoLIvro);
            if(livroExistente){
                livroExistente.quantidade += 1;
                this.livros = [
                    ...this.livros.filter(item=>item.livro.id !== livroExistente.livro.id),
                    livroExistente
                ];
            }
            else {
                this.livros.push({
                    quantidade:1,
                    livro: novoLIvro
                });
            }
        },
        removertLivroCarrinho(carrinhoLivro: CarrinhoLivro){
            const posicaoNoCarrinho = this.getLivroDoCarrinhoIndex(carrinhoLivro.livro);
            this.livros.splice(posicaoNoCarrinho,1);

            if(carrinhoLivro.quantidade){
                this.livros = [
                    ...this.livros,
                    carrinhoLivro
                ];
            }

        }
    },
    getters: {
        getLivroCarrinho: (carrinho:Carrinho) => (livroEncontrar: Livro)=>{
            return carrinho.livros.find(item=>item.livro.id === livroEncontrar.id);
        },
        getLivroDoCarrinhoIndex: (carrinho: Carrinho) => (livroEncontrar: Livro)=>{
            return carrinho.livros.findIndex(item=>item.livro.id === livroEncontrar.id);
        },
        getCarrinho: (carrinho: Carrinho) => () : Array<CarrinhoLivro> => {
            return carrinho.livros;
        },
        getValorLivro: (carrinho: Carrinho) => () : Number => {
            let soma = 0;
            carrinho.livros.forEach(item=>{
                soma += (item.livro.preco * item.quantidade)
            })
            return soma;
        }
    }
})