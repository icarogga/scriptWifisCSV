<h1 align="center">Scrit Wifis CSV</h1>

<h4 align="center"> 
	Concluído ✔️
</h4>

---

   <h2 align="center">Tópicos 📋</h2>

   <p>
   
   - [Sobre 📖](#sobre-)
   - [Funcionalidades 🛠️](#funcionalidades-%EF%B8%8F)
   - [Tecnologias 📲](#tecnologias-)
   - [Como utilizar 🤔](#como-utilizar-)

   </p>

---
<h2 align="center">Sobre 📖</h2>
   
<p align="center">
  Software desenvolvido com python com o intuito de pegar todos os dados que o comando do terminal Linux "sudo iwlist scan |grep -e ESSID -e Quality" retorna. Este script irá
  pegar estes dados e montar uma tabela com os ESSID, as qualidades das respectivas redes e a coluna "class" que terá o valor da variável <strong>className</strong>.
  
  A tabelá sera distribuída da seguinte forma:
  
   RedeA | RedeB | RedeC | classs

 90    |  70   |  20   | quarto

 85    |  65   |  0    | quarto
</p>

---

<h2 align="center">Funcionalidades 🛠️</h2>

   <p>

- Ter acesso as redes wifis disponíveis
- Ver o ESSID de todas as redes wifi disponíveis
- Ver a qualidade da conexão de todas as redes wifi disponíveis
- Transformar todos os dados de ESSID, qualidade de rede em um arquivo csv

   </p>

---

<h2 align="center">Tecnologias 📲</h2>

   <p>

Linguagem: 
-   **[PYTHON](https://www.python.org)**
   
Bibliotecas: 
-   **[SUBPROCESS](https://docs.python.org/3/library/subprocess.html)**
-   **[PANDAS](https://pandas.pydata.org)**
-   **[NUMPY](https://numpy.org)**
-   **[OS](https://docs.python.org/3/library/os.html)**
-   **[TIME](https://docs.python.org/3/library/time.html)**

   </p>

---

<h2 align="center">Como utilizar 🤔</h2>

  <h4>Pré-requisitos:</h4>
  
  <p>
   
   Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
   [Git](https://git-scm.com) e [Python](https://www.python.org/downloads/). 
   Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/)
   
   É necessário também estar utilizando o sistema operacional Linux;
   
  </p>
  
   ```
   
   - Clone este repositório:
   $ git clone https://github.com/icarogga/fotoVilela.git 😉
   
   - Abra o arquivo script.py no VSCode

   - Abra o terminal do VSCode e digite "python3 script.py" 
   
   ```

---

## 💪 Como contribuir para o projeto

1. Faça um **fork** do projeto.
2. Crie uma nova branch com as suas alterações: `git checkout -b my-feature`
3. Salve as alterações e crie uma mensagem de commit contando o que você fez: `git commit -m "feature: My new feature"`
4. Envie as suas alterações: `git push origin my-feature`
> Caso tenha alguma dúvida confira este [guia de como contribuir no GitHub](./CONTRIBUTING.md)

---

   ## 🦸 Autor

   Este projeto foi desenvolvido com o ❤️ por **[@Ícaro Coêlho](https://github.com/icarogga?tab=following)** 👋🏽 Entre em contato!
   
   [![Linkedin Badge](https://img.shields.io/badge/-Ícaro-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/ícaro-coelho-3a5b60206/)](https://www.linkedin.com/in/ícaro-coelho-3a5b60206/) 
[![Gmail Badge](https://img.shields.io/badge/-icarogga@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:icarogga@gmail.com)](mailto:icarogga@gmail.com)

---

## 📝 Licença

Este projeto esta sobe a licença [MIT](./LICENSE).

<img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen">

---


