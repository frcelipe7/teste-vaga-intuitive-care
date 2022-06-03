<template>
  <div class="home">
    <div class="topo">
      <img alt="Vue logo" src="../assets/intuitive-care-logo.png">
    </div>
    
    <div class="block">
      <div class="content_top">
        <h2>Relação de Operadoras Ativas ANS</h2>
        <div class="search">
          <select name="select" id="select">
            <option value="registro_ans">Registro ANS</option>
            <option value="nome_fantasia">Nome Fantasia</option>
            <option value="uf">UF</option>
            <option value="cep">CEP</option>
            <option value="ddd">DDD</option>
            <option value="telefone">Telefone</option>
            <option value="endereco_eletronico">Endereço eletrônico</option>
          </select>
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" 
          fill="currentColor" class="bi bi-search" 
          viewBox="0 0 16 16">
            <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85
             3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5
             5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
          </svg>
          <input type="text" name="search" id="search" placeholder="Pesquisar">
          <button type="submit">Buscar</button>
        </div>
      </div>
      <div class="content_response">
        <table>
          <tr class="top-index">
            <th>Registro ANS</th>
            <th>Nome Fantasia</th>
            <th>UF</th>
            <th>CEP</th>
            <th>DDD</th>
            <th>Telefone</th>
            <th>Endereço eletrônico</th>
          </tr>
        </table>
      </div>
    </div>

    <div class="see-more">
      <h2 class="registro_ans">Registro ANS: <span></span></h2>
      <button>
        <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" 
        fill="currentColor" class="bi bi-x-circle" viewBox="0 0 16 16">
          <path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/>
          <path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707
          8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 
          8 4.646 5.354a.5.5 0 0 1 0-.708z"/>
        </svg>
      </button>
      <table class="primeira">
        <tr class="top-index">
          <th>CNPJ</th>
          <th>Razão Social</th>
          <th>Nome Fantasia</th>
          <th>Modalidade</th>
          <th>Logradouro</th>
        </tr>
        <tr class="values"></tr>
      </table>
      <table class="segunda">
        <tr class="top-index">
          <th>Número</th>
          <th>Complemento</th>
          <th>Bairro</th>
          <th>Cidade</th>
          <th>UF</th>
          <th>CEP</th>
          <th>DDD</th>
        </tr>
        <tr class="values"></tr>
      </table>
      <table class="terceira">
        <tr class="top-index">
          <th>Telefone</th>
          <th>Fax</th>
          <th>Endereço Eletrônico</th>
          <th>Representante</th>
          <th>Cargo Representante</th>
          <th>Data de Registro ANS</th>
        </tr>
        <tr class="values"></tr>
      </table>
    </div>
  </div>

</template>

<script src="../assets/js/fetch_home.js"></script>

<style lang="scss">
body {background-color: rgb(234, 234, 234);}
.topo {
  background-color: #fff; padding-top: 5px;
  width: 100%; height: 65px;
  box-shadow: 0 4px 4px rgb(192, 192, 192);
}
.block {
  width: 95%; background-color: #fff; min-height: 500px; height: auto;
  margin: auto; margin-top: 30px; border-radius: 5px;
  box-shadow: 0px 0px 4px rgb(192, 192, 192);
  padding: 20px 10px; margin-bottom: 30px;

  .content_top {
    display: flex; justify-content: space-between;

    h2 {color: #707df4; font-weight: 400;}

    .search {
      display: flex; align-items: center;
      
      svg, svg path {width: 25px; height: 25px;}

      input {
        border: 1.5px dashed rgb(172, 172, 172);
        transition: .3s; margin-left: 10px;
        width: 300px; height: 30px; padding: 0 5px;
      }

      button {
        height: 30px; background-color: rgb(0, 184, 0);
        border: none; margin-left: 10px; padding: 0 10px;
        cursor: pointer;
      }
    }
  }

  .content_response {
    min-height: 420px; width: 100%; margin-top: 20px;
    border: 1.5px dashed rgb(172, 172, 172); height: auto;

    table {
      width: 100%; height: auto;

      tr {
        height: 30px; background-color: rgb(234, 234, 234); 
        transition: .2s; cursor: pointer;
      
        svg, svg path {
          fill: rgb(0, 184, 0); width: 25px; height: 25px; padding-top: 2px;
        }
      }
      tr:hover {background-color: rgb(134, 134, 134); color: #fff}

      .top-index {background-color: rgb(52, 52, 52); color: #fff; cursor: default;}
      .top-index:hover {background-color: rgb(52, 52, 52);}
    }
  }
}

.see-more {
  width: 80%; height: 500px; position: fixed; padding: 20px;
  background-color: rgb(140, 140, 140); border-radius: 5px;
  z-index: 100; top: 50px; margin: 10%; margin-top: 50px; display: none;
  
  h2 {margin-bottom: 10px;}

  button {
    position: absolute; right: 20px; top: 15px; padding: 0%;
    display: flex; align-items: center; justify-content: center;
    border-radius: 50px; background-color: transparent; border: none;
    cursor: pointer;
  }

  table {
    width: 100%;
    
    th {padding: 10px; background-color: rgb(184, 184, 184);}

    .top-index th {background-color: rgb(52, 52, 52); color: #fff; cursor: default;}
  }
}

.see-more[closing] {
  animation: closing .3s forwards;
}

@keyframes closing {
  0% {opacity: 1;}
  100% {opacity: 0;}
}

.see-more[opening] {
  animation: opening .3s forwards;
}

@keyframes opening {
  0% {opacity: 0;}
  100% {opacity: 1;}
}
</style>
