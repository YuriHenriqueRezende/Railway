import type { Livro } from "./livros";
import type { usuario } from "./usuario";

export enum BIBLIOTECA {
    "DEVOLVIDO" = "D",
    "ATRASADO" = "A",
    "EMPRESTADO" = "E",
}

export type emprestimo = {
    LIVROFK: Livro;
    usuarioFK: usuario;
    data_inicio: string;
    data_fim: string;
    status: BIBLIOTECA;
}

