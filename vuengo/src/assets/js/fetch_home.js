document.addEventListener("DOMContentLoaded", () => {
    
    const table = document.querySelector(".content_response table");
    const api_route = "http://127.0.0.1:8000/api/get";
    
    const see_more = document.querySelector(".see-more");
    const close_see_more_button = document.querySelector(".see-more button");
    const registro_ans_span = document.querySelector(".see-more .registro_ans span");


    // função que vai permitir o usuário ver mais sobre a empresa selecionada
    function abrir_see_more(registro, see_more_content=see_more) {
        fetch(`http://127.0.0.1:8000/api/get?registro_ans=${registro.registro_ans}&id=${registro.id}`)
        .then(response => response.json())
        .then(see_more => {
            // adicionando os valores na primeira tablela
            let tr_1 = document.querySelector(".primeira .values");
            tr_1.innerHTML = `
                <th>${see_more[0].cnpj}</th>
                <th>${see_more[0].razao_social}</th>
                <th>${see_more[0].nome_fantasia}</th>
                <th>${see_more[0].modalidade}</th>
                <th>${see_more[0].logradouro}</th>
            `;

            // adicionando os valores na segunda tablela
            let tr_2 = document.querySelector(".segunda .values");
            tr_2.innerHTML = `
                <th>${see_more[0].numero}</th>
                <th>${see_more[0].complemento}</th>
                <th>${see_more[0].bairro}</th>
                <th>${see_more[0].cidade}</th>
                <th>${see_more[0].uf}</th>
                <th>${see_more[0].cep}</th>
                <th>${see_more[0].ddd}</th>
            `;

            // adicionando os valores na terceira tablela
            let tr_3 = document.querySelector(".terceira .values");
            tr_3.innerHTML = `
                <th>${see_more[0].telefone}</th>
                <th>${see_more[0].fax}</th>
                <th>${see_more[0].endereco_eletronico}</th>
                <th>${see_more[0].representante}</th>
                <th>${see_more[0].cargo_representante}</th>
                <th>${see_more[0].data_registro_ans}</th>
            `;
        });
        
        // animação do 'see_more' (aparecer)
        see_more_content.style.display = "block";
        see_more_content.setAttribute('opening', "");
        

        registro_ans_span.innerHTML = registro.registro_ans;
    };

    // fazendo a busca
    fetch(api_route)
    .then(response => response.json())
    .then(todos_registros => {
        todos_registros.forEach(registro => {
            // criando o elemento 'tr' para exibir as informações
            // buscadas na tela de inicio
            let tr = document.createElement('tr');
            tr.classList.add("row_data");
            tr.innerHTML = `
                <th>${registro.registro_ans}</th>
                <th>${registro.nome_fantasia}</th>
                <th>${registro.uf}</th>
                <th>${registro.cep}</th>
                <th>${registro.ddd}</th>
                <th>${registro.telefone}</th>
                <th>${registro.endereco_eletronico}</th>
            `;
            tr.addEventListener("click", () => {
                abrir_see_more(registro);
            })
            // adicionando na tabela
            table.append(tr);
        });
    })
    .catch(e => {console.log(e)})

    // animação do 'see_more' (desaparecer)
    close_see_more_button.addEventListener('click', () => {
        see_more.removeAttribute("opening");
        see_more.setAttribute('closing', "");
        see_more.addEventListener("animationend", () => {
            see_more.style.display = 'none';
            see_more.removeAttribute("closing");
        });
    });

    
    
    // aqui eu vou fazer a pesquisa
    const select = document.querySelector(".search select");
    const search_button = document.querySelector(".search button");
    
    select.addEventListener("change", () => {
        
        // console.log(value)
    });
    
    search_button.addEventListener("click", () => {
        const search_input = document.querySelector(".search input");
        const select_value = select.options[select.selectedIndex].value;

        const all_row_data = document.querySelectorAll(".row_data");


        fetch(api_route)
        .then(response => response.json())
        .then(todos_registros => {
            todos_registros.forEach(registro => {
                all_row_data.forEach(row_data => {
                    row_data.remove();
                });
                for ([key, value] of Object.entries(registro)) {
                    if (key == select_value) {
                        if (String(value.toUpperCase()).includes(String(search_input.value.toUpperCase()))) {
                            let tr = document.createElement('tr');
                            tr.classList.add("row_data");
                            tr.innerHTML = `
                                <th>${registro.registro_ans}</th>
                                <th>${registro.nome_fantasia}</th>
                                <th>${registro.uf}</th>
                                <th>${registro.cep}</th>
                                <th>${registro.ddd}</th>
                                <th>${registro.telefone}</th>
                                <th>${registro.endereco_eletronico}</th>
                            `;
                            tr.addEventListener("click", () => {
                                abrir_see_more(registro);
                            })
                            // adicionando na tabela
                            table.append(tr);
                        }
                        
                    }
                }
            });
        })
        .catch(e => {console.log(e)})
    })

});
