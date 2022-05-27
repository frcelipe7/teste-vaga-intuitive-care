<template>
  <div class="home">
    <div class="topo">
      <img alt="Vue logo" src="../assets/intuitive-care-logo.png">
    </div>
    
    <div class="block">
      <div class="content_top">
        <h2>Relação de Operadoras Ativas ANS</h2>
        <div class="search">
          <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" 
          fill="currentColor" class="bi bi-search" 
          viewBox="0 0 16 16">
            <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85
             3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5
             5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
          </svg>
          <input type="text" name="search" id="search" placeholder="Pesquisar">
        </div>
      </div>
      <div class="content_response">
        <table>
          <tr class="top-index">
            <th>Nome Fantasia</th>
            <th>Registro ANS</th>
            <th>UF</th>
            <th>CEP</th>
            <th>DDD</th>
            <th>Telefone</th>
            <th>Endereço eletrônico</th>
            <th>Saiba Mais</th>
          </tr>
          <tr>
            <td>E-Vida</td>
            <td>418374</td>
            <td>DF</td>
            <td>70730630</td>
            <td>61</td>
            <td>39668300</td>
            <td>governanca@evida.org.br</td>
            <td>
              <a href="/">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" 
                height="16" fill="currentColor" class="bi bi-arrow-right-square-fill"
                viewBox="0 0 16 16">
                  <path d="M0 14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2a2 2 0 
                  0 0-2 2v12zm4.5-6.5h5.793L8.146 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 
                  0 1 0 .708l-3 3a.5.5 0 0 1-.708-.708L10.293 8.5H4.5a.5.5 0 0 1 0-1z"/>
                </svg>
              </a>
            </td>
          </tr>
          <tr>
            <td>ABERTTA SAÚDE</td>
            <td>314668</td>
            <td>MG</td>
            <td>30150281</td>
            <td>31</td>
            <td>32484300</td>
            <td>abertta.ans@arcelormittal.com.br</td>
            <td>
              <a href="/">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" 
                height="16" fill="currentColor" class="bi bi-arrow-right-square-fill"
                viewBox="0 0 16 16">
                  <path d="M0 14a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2a2 2 0 
                  0 0-2 2v12zm4.5-6.5h5.793L8.146 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 
                  0 1 0 .708l-3 3a.5.5 0 0 1-.708-.708L10.293 8.5H4.5a.5.5 0 0 1 0-1z"/>
                </svg>
              </a>
            </td>
          </tr>
        </table>
      </div>
    </div>
  </div>
</template>


<style lang="scss">
body {background-color: rgb(234, 234, 234);}
.topo {
  background-color: #fff; padding-top: 5px;
  width: 100%; height: 65px;
  box-shadow: 0 4px 4px rgb(192, 192, 192);
}
.block {
  width: 95%; background-color: #fff; height: 500px;
  margin: auto; margin-top: 30px; border-radius: 5px;
  box-shadow: 0px 0px 4px rgb(192, 192, 192);
  padding: 20px 10px;

  .content_top {
    display: flex; justify-content: space-between;

    h2 {color: #707df4; font-weight: 400;}

    .search {
      display: flex; align-items: center;
      
      svg, svg path {width: 25px; height: 25px;}

      input {
        border: 1.5px dashed rgb(172, 172, 172);
        padding: 5px; transition: .3s; margin-left: 10px;
        width: 300px;
      }
    }
  }

  .content_response {
    height: 420px; width: 100%; margin-top: 20px;
    border: 1.5px dashed rgb(172, 172, 172);

    table {
      width: 100%; height: auto;

      tr {
        height: 30px; background-color: rgb(234, 234, 234); 
        transition: .2s;
      
        svg, svg path {
          fill: rgb(0, 184, 0); width: 25px; height: 25px; padding-top: 2px;
        }
      }
      tr:hover {background-color: rgb(134, 134, 134); color: #fff}

      .top-index {background-color: rgb(52, 52, 52); color: #fff;}
      .top-index:hover {background-color: rgb(52, 52, 52);}
    }
  }
}
</style>
