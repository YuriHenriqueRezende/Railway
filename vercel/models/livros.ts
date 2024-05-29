export enum STATUS {
    P = "Pendente",
    C = "Cancelado(a)",
    A = "Aprovado(a)"
}
enum FORMATOS {
    E = "E-BOOK",
    F = "FISICO"
}


export type categoria = {
    id: number;
    nome: string;
}

export type Livro = {
    id: number;
    titulo: string;
    descricao: string;
    numero_pagina: number;
    formato: FORMATOS;
    numero_edicao: number;
    autor: string;
    publicacao: number;
    categoriaFK: categoria;
    status: STATUS;
    preco: number;
    fotosFK: Array<string>;
    quantidade: number;
}