# 🎓 ICOL - Instituto de Capacitação e Orientação Livre (Front-End)

Este é o repositório oficial do Front-End da plataforma do **ICOL**, um instituto focado em transformar vidas através da capacitação profissional, educação e acolhimento presencial na cidade de Franca-SP.

A interface foi projetada para ser leve, acessível (focada também no público 50+) e otimizada para rodar de forma fluida em computadores com hardware modesto, seguindo princípios rigorosos de UX e UI.

## 🚀 Tecnologias Utilizadas

* **HTML5 Semântico:** Estruturação sólida e acessível.
* **Tailwind CSS:** Estilização via script com paleta de cores customizada da marca.
* **Vanilla JavaScript:** Lógica de interface sem dependência de bibliotecas pesadas.
* **Phosphor Icons / SVG:** Iconografia moderna e escalável.

## ✨ Principais Funcionalidades

* **Dashboards Baseados em Perfis:** Interfaces exclusivas e regras de negócio visuais separadas para **Alunos**, **Responsáveis**, **Professores** e **Coordenadores**.
* **Acessibilidade Integrada:** Controles de contraste e usabilidade desenhados especialmente para o módulo *Projeto Bem-Viver* (público 50+).
* **Modo Escuro (Dark Mode):** Alternância de tema persistente em toda a aplicação utilizando `localStorage`, reduzindo a fadiga visual.
* **Mural de Avisos:** Sistema integrado de notificações e controle de eventos.
* **Responsividade Total:** Layout fluido que se adapta a dispositivos móveis, tablets e desktops.

## 📁 Estrutura do Projeto

O projeto segue uma arquitetura limpa de pastas para facilitar a manutenção e escalabilidade:

```text
📦 front-end-icol
 ┣ 📂 aluno          # Dashboards e sub-páginas exclusivas do Aluno (Notas, Calendário, Frequência)
 ┣ 📂 assets         # Scripts globais e estilos auxiliares (ex: theme.js)
 ┣ 📂 coordenador    # Painel administrativo (Cursos, Mural, Professores, Relatórios)
 ┣ 📂 icol           # Arquivos de mídia e institucionais (Imagens, Logos)
 ┣ 📂 professor      # Área do docente (Turmas, Diário de Classe, Notas)
 ┣ 📂 responsavel    # Acompanhamento do aluno (Avisos, Frequência, Comportamento)
 ┣ 📜 cadastro.html          # Formulário público de inscrição nos projetos
 ┣ 📜 cursos_livres.html     # Landing page detalhada da modalidade
 ┣ 📜 login.html             # Tela de autenticação com seletor de perfil
 ┣ 📜 projeto_aleph.html     # Landing page detalhada da modalidade
 ┣ 📜 projeto_bem_viver.html # Landing page detalhada da modalidade
 ┗ 📜 tela_inicial.html      # Landing Page principal da instituição