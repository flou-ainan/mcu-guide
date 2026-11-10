# 🛡️ Guia Marvel Studios MCU - Timeline & Scraper

Guia cinematográfico interativo do Universo Cinematográfico Marvel (MCU) com suporte à **Ordem de Lançamento** e **Ordem Cronológica**, filtros por Fase, checklist de progresso salvo localmente, capas oficiais em alta resolução, sinopses sem spoiler em português e trailers oficiais integrados.

Pronto para deploy direto no **GitHub Pages**!

---

## 📁 Estrutura dos Arquivos

| Arquivo | Descrição |
|---|---|
| `scraper.py` | Script Python autônomo que realiza o scraping de capas oficiais (IMDb) e trailers oficiais (YouTube), consolidando tudo com sinopses sem spoiler em PT-BR. |
| `mcu_data.json` | Dataset JSON completo com **52 produções** (filmes e séries da Fase 1 à Fase 5/6), capas em alta definição, links de trailer e metadados. |
| `data.js` | Exportação JavaScript dos dados para permitir execução 100% offline (mesmo abrindo direto via dois cliques no navegador, sem erro de CORS). |
| `index.html` | Aplicação web interativa estilizada com visual oficial Marvel Studios, Tailwind CSS, FontAwesome e player de trailer em pop-up. |

---

## 🚀 Como Executar o Scraper Localmente

Se quiser atualizar os dados ou rodar o scraper novamente:

```bash
# Execução normal (utiliza cache inteligente para ser rápido)
python3 scraper.py

# Para forçar nova busca completa na web
python3 scraper.py --force
```

O script atualizará automaticamente o `mcu_data.json` e o `data.js`.

---

## 💻 Testando o Site Localmente

Você tem duas opções simples:

### Opção 1: Abrir direto
Dê um duplo clique no arquivo `index.html` ou abra pelo navegador:
```bash
google-chrome index.html
```

### Opção 2: Servidor local HTTP
```bash
python3 -m http.server 8000
```
Acesse em seu navegador: [http://localhost:8000](http://localhost:8000)

---

## 🌐 Como Subir no GitHub Pages

1. Crie um repositório no seu GitHub (exemplo: `mcu-guide`).
2. No terminal deste projeto, faça o commit e envie os arquivos:
   ```bash
   git add .
   git commit -m "feat: site MCU com scraper de capas, trailers e sinopses sem spoiler"
   git branch -M main
   git remote add origin https://github.com/SEU_USUARIO/mcu-guide.git
   git push -u origin main
   ```
3. No GitHub:
   - Acesse **Settings** > **Pages**
   - Em **Build and deployment** > **Source**, selecione **Deploy from a branch**
   - Escolha a branch **main** e a pasta **/ (root)**
   - Clique em **Save**
4. Em poucos segundos, seu site estará no ar na URL:  
   `https://SEU_USUARIO.github.io/mcu-guide/`

---

## ✨ Funcionalidades do Site

- 🎬 **Ordem de Lançamento vs Cronológica**: Alternância em 1 clique com explicações sobre spoilers e evolução técnica.
- 📺 **Séries em Visual Compacto**: Séries formatadas de forma sutil com `<small>`, além de botão rápido **"Ocultar Séries"**.
- 🖼️ **Capas Oficiais**: Miniaturas em alta definição nos detalhes expansíveis de cada obra.
- 🍿 **Trailers Oficiais**: Botão para assistir em pop-up/modal direto na página ou abrir no YouTube.
- 📖 **Sinopses Sem Spoiler**: Textos em português cuidadosamente elaborados para apresentar apenas a premissa.
- 🔍 **Busca em Tempo Real & Filtro de Fases**: Filtre da Fase 1 à Fase 6 ou busque por nome de personagens e títulos.
- 💾 **Checklist & Progresso Persistente**: Marcação de filmes/séries assistidos com contador percentual salvo no `localStorage`.
