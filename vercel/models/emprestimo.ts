import type { Livro } from "./livros"
import type { usuario } from "./usuario";

type emprestimo = {
    livroFK: Livro
    usuarioFK: usuario;
    data_inicio: number;
    data_fim: number;
}