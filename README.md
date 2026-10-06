# 🤖 Automação de Tarefas com Python

Projeto desenvolvido em Python com o objetivo de automatizar tarefas repetitivas realizadas no dia a dia de trabalho, reduzindo processos manuais e tornando as atividades mais rápidas e eficientes.

O projeto utiliza principalmente a biblioteca **PyAutoGUI** para controlar mouse e teclado e interagir com aplicações de forma automatizada.

## 📌 Sobre o Projeto

Durante minha rotina de trabalho, identifiquei algumas atividades que exigiam interações repetitivas, como copiar informações de um sistema para uma planilha Excel e responder e-mails de cancelamento.

A partir dessas necessidades, desenvolvi automações utilizando Python para reduzir a quantidade de tarefas manuais.

Atualmente, o projeto possui duas automações:

* **Excel Data Entry** — automatiza a transferência de informações de um sistema para uma planilha Excel.
* **Cancellation Notice** — automatiza parte do processo de resposta a e-mails relacionados a cancelamentos.

## 🚀 Automações

### 1. Excel Data Entry

**Arquivo:** `excel_data_entry.py`

Essa automação foi criada para facilitar o processo de transferência de informações de um sistema utilizado no trabalho para uma planilha Excel.

### Como funciona

O script:

1. Acessa o sistema.
2. Seleciona a informação necessária.
3. Copia os dados utilizando `Ctrl + C`.
4. Abre o Excel.
5. Seleciona a célula correspondente.
6. Cola a informação utilizando `Ctrl + V`.
7. Retorna ao sistema.
8. Repete o processo para outras informações.

### Benefícios

* Redução de tarefas repetitivas.
* Menor necessidade de copiar e colar informações manualmente.
* Economia de tempo.
* Maior padronização do processo.
* Aplicação prática de Python na rotina de trabalho.

---

### 2. Cancellation Notice

**Arquivo:** `cancellation_notice.py`

Essa automação foi criada para auxiliar no processo de resposta de e-mails relacionados a cancelamentos.

### Como funciona

O script:

1. Abre o navegador.
2. Acessa a interface de e-mail.
3. Abre as opções da mensagem.
4. Seleciona **Responder a todos**.
5. Acessa o campo de edição da mensagem.
6. Seleciona a área de texto.
7. Insere a data do cancelamento.

Essa automação ainda está em desenvolvimento e pode receber novas funcionalidades para tornar o processo mais completo e dinâmico.

## 🛠️ Tecnologias utilizadas

* **Python**
* **PyAutoGUI** — automação de mouse e teclado
* **Time** — controle de intervalos entre as ações

## 📂 Estrutura do projeto

```text
python-automation/
│
├── excel_data_entry.py
├── cancellation_notice.py
└── README.md
```

## ⚙️ Instalação

Certifique-se de ter o Python instalado em seu computador.

Depois, instale a biblioteca necessária:

```bash
pip install pyautogui
```

O módulo `time` já faz parte da biblioteca padrão do Python e não precisa ser instalado separadamente.

## ▶️ Como executar

Os scripts podem ser executados pelo terminal ou diretamente pelo VS Code.

### Excel Data Entry

```bash
python excel_data_entry.py
```

### Cancellation Notice

```bash
python cancellation_notice.py
```

## ⚠️ Observações importantes

As automações utilizam **coordenadas fixas da tela** para realizar os cliques.

Por isso, o funcionamento pode depender de fatores como:

* Resolução da tela.
* Posição das janelas.
* Layout das aplicações.
* Alterações na interface dos sistemas.
* Tempo de carregamento das páginas.

Para executar os scripts corretamente, é necessário que as aplicações estejam abertas e posicionadas conforme esperado pela automação.

Em versões futuras, as automações podem ser aprimoradas utilizando reconhecimento de imagens, navegação por teclado ou outras técnicas de identificação dinâmica dos elementos.

## 📈 Melhorias futuras

* [ ] Utilizar `datetime` para obter automaticamente a data atual.
* [ ] Substituir coordenadas fixas por reconhecimento de imagem.
* [ ] Adicionar uma tecla de emergência para interromper a automação.
* [ ] Implementar tratamento de erros.
* [ ] Criar funções reutilizáveis.
* [ ] Adicionar logs para acompanhar a execução.
* [ ] Utilizar `pandas` para manipulação de dados e planilhas.
* [ ] Tornar as automações mais independentes da resolução da tela.
* [ ] Automatizar completamente a criação das mensagens de cancelamento.
* [ ] Permitir configurações personalizadas para diferentes processos.

## 🎯 Objetivo e aprendizado

Este projeto faz parte do meu processo de aprendizado em **Python e automação**.

Além de praticar conceitos da linguagem, o objetivo é aplicar Python na resolução de problemas reais, identificando tarefas repetitivas e transformando processos manuais em fluxos automatizados.

Durante o desenvolvimento, estou praticando conceitos como:

* Automação de tarefas.
* Controle de mouse e teclado.
* Manipulação de aplicações.
* Lógica de programação.
* Organização de código.
* Identificação de oportunidades de automação.
* Resolução de problemas utilizando Python.

A ideia principal não é apenas fazer o código funcionar, mas **utilizar programação para melhorar processos e reduzir tarefas manuais no dia a dia**.

## 👨‍💻 Autor

**Giliarde Rodrigues**

Estudante de Engenharia de Software | Python | Automação

---

⭐ Projeto desenvolvido como parte da minha jornada de aprendizado em Python e aplicação de automação em situações reais.
