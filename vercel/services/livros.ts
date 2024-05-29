import { backend } from "~/models/links";
import type { Livro } from "~/models/livros";
import type { pagina } from "~/models/pagina";

export const getLivro = (pagina:number=1): Promise<pagina<Livro>|null> => {
    return useFetch<pagina<Livro>>(`${backend}/livros?page=${pagina}`)
        .then(resposta=> {
            return Promise.resolve(resposta.data.value);
        })
        .catch(error=>{
            console.log("error",error);
            return Promise.resolve(null);
        })
};