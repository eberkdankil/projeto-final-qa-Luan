# projeto-final-qa-Luan
Repositório para a entrega da atividade avaliativa


## 1. Apresentação

**Nome:**  
Luan Rodrigues Amorim

**Curso:**  
Gestão de Tecnologia da Informação - 5º Semestre

**Experiência com a Disciplina:**  
Minha experiência com a disciplina de *Quality Assurance* foi incrível, pois pude entender como são feitos os testes para garantir que um software entregue aquilo que foi prometido, sem erros.  
Utilizando vários métodos e ferramentas ao longo das aulas, percebi que não existe um único jeito de testar um programa, mas sim boas práticas a serem seguidas, como documentação, planejamento de testes e relatórios sobre o que foi testado.  
Pode não ser uma área que eu siga a fundo, mas sem dúvidas foi um grande aprendizado — e conhecimento nunca é demais.

---

## 2. O que é Quality Assurance (QA)?

*Quality Assurance* é o processo que garante a entrega de um produto com qualidade, funcionando conforme o esperado.  
Um exemplo simples: imagine pedir uma comida em um restaurante sem um chef que verifique os pratos. Quando chegam, estão mal montados, com gosto ruim e ingredientes errados.  
Agora, com um chef que garante a qualidade, o prato vem impecável, e você volta ao restaurante.  
O QA em software funciona da mesma forma: os profissionais testam, identificam erros e ajudam o time de desenvolvimento a entregar um produto confiável e funcional.

---

## 3. Conceitos Aprendidos Durante o Semestre

### ✅ Qualidade em Software e Cultura de Qualidade
Qualidade em software é garantir que o produto atenda aos requisitos funcionais e não funcionais, como desempenho e segurança.  
A cultura de qualidade envolve a adoção contínua de boas práticas pela equipe, como testes, revisão de código e integração contínua.

---

### ✅ Tipos de Testes

- **Unitário**: Testes feitos em uma função específica para validar sua funcionalidade.  
- **Integração**: Verifica se os módulos do sistema funcionam bem em conjunto.  
- **Sistema**: Testa o sistema completo, como um todo.  
- **Aceitação**: Valida se o software atende às expectativas do cliente.  
- **Regressão**: Garante que novas mudanças não afetem funcionalidades antigas.  
- **Exploratório**: Testes livres, onde o testador busca falhas sem um roteiro fixo.

---

### ✅ Planejamento de Testes

- **Critérios de aceitação**: Definem se uma funcionalidade está pronta para entrega.  
- **Plano de teste**: Documento com escopo, estratégia e recursos do teste.  
- **Casos de teste**: Descrição dos testes, com objetivos, passos e resultados esperados.

---

### ✅ Ferramentas de Testes Utilizadas

- **Google Colab**: Utilizado para escrever scripts Python de testes.  
- **GitHub**: Controle de versão e colaboração em projetos.  
- **Visual Studio Code**: Editor leve e completo para desenvolvimento.  
- **Postman**: Teste e automação de requisições de APIs.

---

### ✅ Automação de Testes e CI/CD

Automatizar testes permite execuções rápidas e repetíveis, reduzindo erros humanos.  
Com integração ao **CI/CD**, os testes são feitos automaticamente a cada alteração no código, garantindo mais segurança e qualidade contínua nas entregas.

---

### ✅ Monitoramento e Controle de Qualidade

Envolve o uso de:
- **Métricas** (como cobertura de testes e taxa de falhas);  
- **Rastreamento de bugs** (para registrar e resolver erros);  
- **Observabilidade** (logs, métricas e traces para entender o comportamento do sistema em tempo real).

---

## 4. Ferramentas e Sites Utilizados

- [Google Colab](https://colab.research.google.com/)  
- [GitHub](https://github.com/)  
- [UptimeRobot](https://uptimerobot.com/)  
- [Katalon Recorder - Chrome Web Store](https://chromewebstore.google.com/detail/katalon-recorder-selenium/ljdobmomdgdljniojadhoplhkpialdid)  
- [Postman](https://www.postman.com)  
- [Visual Studio Code](https://code.visualstudio.com)

---

## 5. Explicação dos Testes Entregues

### 1 🔹 Nome do teste: Teste de Requisição com Requests

**Objetivo:**  
Testar se uma requisição GET para uma API pública retorna uma resposta válida (status 200) e com dados no formato esperado (JSON).

**Biblioteca Python utilizada:**  
`requests`

**Resultado esperado:**  
A API deve retornar status code `200` e exibir os dados JSON esperados da URL consultada.

**Link para o arquivo:**  
[teste_requisicao_api](Testes/teste_01.py)

**Link Colab**

[Colab](https://colab.research.google.com/drive/1FHLaRFcEFW-IwomhqpPWR5g_UD9IWAGU?usp=sharing)

---

### 2 🔹 Nome do teste: Teste Unitário de Soma

**Objetivo:**  
Verificar se a função `somar(a, b)` retorna o valor correto ao somar dois números, cobrindo diferentes cenários (positivos, negativos e zero).

**Biblioteca Python utilizada:**  
`pytest`

**Resultado esperado:**  
A função deve retornar a soma correta dos dois valores fornecidos em cada caso de teste.

**Link para o arquivo:**  
[teste_unitario_soma](Testes/Teste_02.py)

**Link Colab**

[Colab](https://colab.research.google.com/drive/1ApNJ7SFieJurQNPpl8V8L5OrUnzz_J8j?usp=sharing)

---

### 3 🔹 Nome do teste: Teste Automatizado com Selenium

**Objetivo:**  
Simular o acesso ao Google, realizar uma busca por “Quality Assurance” e validar se a navegação funciona corretamente.

**Biblioteca Python utilizada:**  
`selenium`

**Resultado esperado:**  
A automação deve abrir o navegador, preencher o campo de busca, enviar a pesquisa e exibir o título da página de resultados.

**Link para o arquivo:**  
[teste_busca_google](Testes/Teste_03.py)

**Provas**

![image](https://github.com/user-attachments/assets/96ba5b54-6b39-4195-b785-5ee29cac898c)

**Resposta**

DevTools listening on ws://127.0.0.1:57342/devtools/browser/a150a819-12b2-4f30-a96c-90634cd43774
[4856:19000:0522/210928.824:ERROR:net\socket\ssl_client_socket_impl.cc:877] handshake failed; returned -1, SSL error code 1, net_error -101
[4856:19000:0522/210928.829:ERROR:net\socket\ssl_client_socket_impl.cc:877] handshake failed; returned -1, SSL error code 1, net_error -101
[4856:19000:0522/210928.839:ERROR:net\socket\ssl_client_socket_impl.cc:877] handshake failed; returned -1, SSL error code 1, net_error -101
[4856:19000:0522/210928.844:ERROR:net\socket\ssl_client_socket_impl.cc:877] handshake failed; returned -1, SSL error code 1, net_error -101
**Título da página: Quality Assurance - Pesquisa Google**

---

##  6. Conclusão Final

###  O que você aprendeu de mais importante?
Aprendi que a garantir a qualidade daquilo que você quer entregar, vai ser o diferencial entre mim e os concorrentes.

##  Como você enxerga a área de QA no seu futuro profissional?
A área de QA pode não ser o que eu vá seguir no futuro, mas estarei levando o aprendizado para todos os projetos que eu fazer ou participar daqui em diante

##  Qual ferramenta ou tema mais chamou sua atenção e por quê?

O tema de CI/DI, pois como pretendo seguir com a carreira de DevOps, ver a explicação de como é aplicada a entrega continua e a integração continua no mertcado de trabalho me deixa ainda mais animado para estudar sobre o assunto e aplica-lo quando possível.

