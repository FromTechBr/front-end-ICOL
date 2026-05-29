# Estrutura do Projeto: Front-End ICOL

Este documento descreve a organização atual do repositório, detalhando o propósito de cada pasta e arquivo principal para facilitar a manutenção e o desenvolvimento contínuo da plataforma ICOL.

## 📂 Visão Geral dos Diretórios

### `/front`
Contém todo o código-fonte principal (HTML, CSS, JS) do frontend da plataforma.
- **`/aluno`**: Telas e sub-páginas do dashboard exclusivo para os alunos (ex: notas, faltas, horários, mural).
- **`/coordenador`**: Telas e sub-páginas do painel administrativo dos coordenadores (ex: gestão de professores, alunos, cursos e relatórios).
- **`/professor`**: Telas e sub-páginas do dashboard dos professores (ex: diário de classe, lançamento de notas e turmas).
- **`/responsavel`**: Telas e sub-páginas do dashboard para os pais/responsáveis acompanharem os alunos (ex: frequência, comportamento, avisos).
- **`/assets`**: Arquivos globais de estilos (CSS) e scripts (JS). Inclui o arquivo `theme.js` responsável pela lógica do modo claro/escuro.
- **Arquivos HTML na raiz do `/front`**:
  - `tela_inicial.html`: A landing page principal do instituto.
  - `login.html`: A tela de autenticação para acesso aos dashboards.
  - `cadastro.html`: O formulário público de inscrição nos projetos.
  - `projeto_aleph.html`, `cursos_livres.html`, `projeto_bem_viver.html`: Páginas detalhadas para cada projeto oferecido pelo ICOL.

### `/icol`
Armazena os recursos institucionais e arquivos de mídia do Instituto ICOL.
- **`/icol-imagens`**: Todas as imagens, logotipos (ex: `icol-colorida.png`, `icol-branca.png`) e gráficos utilizados em toda a interface do projeto.
- **`/icol-documentos`**: Documentos textuais, PDFs ou arquivos gerais de referência do instituto.

### `/references`
Pasta designada para armazenar materiais de referência, designs antigos, rascunhos ou documentos fornecidos como inspiração para o layout.

## 📄 Arquivos na Raiz
Os arquivos localizados diretamente na raiz (principalmente `.py` e `.ps1`) são scripts utilitários desenvolvidos durante o processo de construção e manutenção do projeto:
- **Scripts de Correção (ex: `fix_encoding.py`, `fix_fffd.py`)**: Utilizados para realizar varreduras e corrigir problemas de codificação de caracteres (UTF-8) em arquivos HTML antigos que possuíam caracteres corrompidos.
- **Scripts de Auditoria (ex: `audit.py`, `diagnose.py`)**: Utilizados para diagnosticar problemas e listar detalhes estruturais do projeto.
