# Macro Hades — Automação de Ciclo de Morte/Respawn

Esse foi meu primeiro projeto de programação: um macro em Python que automatiza um ciclo repetitivo do jogo *Hades*, usando visão computacional para "enxergar" a tela e decidir suas ações, em vez de depender de cliques em posições fixas.

## O problema que resolvi

Um dos NPCs do jogo (Hipnos) só libera um diálogo importante de missão depois de várias interações repetidas, intercaladas por diálogos genéricos e sem valor. Ao invés de repetir esse processo manualmente dezenas de vezes, criei um macro que faz isso sozinho, enquanto eu faço outra coisa.

Esse não é um problema raro: relatos na comunidade do jogo (fóruns do Steam) descrevem esse favor como notoriamente demorado, com jogadores levando dezenas — em alguns casos, mais de 100 runs — para progredir, mesmo tendo completado tudo mais no jogo.

## Como funciona

O macro roda em ciclo contínuo:

1. **Detecta** (via reconhecimento de imagem) que o personagem renasceu após a morte
2. **Anda até o NPC** (Hipnos), com movimento cronometrado
3. **Interage e avança o diálogo** automaticamente
4. **Segue até o ponto de início de uma nova run**, entra no pacto e confirma
5. **Detecta** o início da run (novamente via reconhecimento de imagem)
6. **Detecta** se apareceu uma benção ou martelo de dedalo, e toma decisões diferente dependendo de qual aparecer (com navegação por teclado)
7. **Vai até uma área de perigo** e espera o personagem morrer
8. **Anda aleatoriamente** a cada 5 segundos para garantir a morte (via biblioteca random)
9. **Detecta a tela de morte** e reinicia o ciclo

Tudo isso é controlado por uma tecla de atalho (F8), que liga/desliga o macro a qualquer momento — inclusive no meio de uma ação em andamento, não só entre um ciclo e outro.

Uma verificação extra identifica quando o diálogo de missão específico aparece (por um ícone diferente sobre o NPC) e, quando detectado, desliga o macro automaticamente e registra quantos ciclos e quanto tempo foram necessários até aquele ponto.

## Tecnologias e bibliotecas usadas

| Biblioteca | Uso |
|---|---|
| `pyautogui` | Controle de mouse/teclado e captura de tela |
| `opencv-python` (`cv2`) | Reconhecimento de imagem na tela (template matching) |
| `numpy` | Conversão de formato de imagem entre bibliotecas |
| `keyboard` | Captura de hotkey global, mesmo com o jogo em foco |
| `customtkinter` | Interface gráfica com status ao vivo |
| `Pillow` (PIL) | Manipulação de imagens (logo, remoção de fundo) |
| `threading` | Execução do macro e da interface em paralelo |
| `time`, `random` | Controle de tempo e movimento aleatório |

## Estrutura do projeto

```
main.py         → ponto de entrada: inicia o macro (em thread) e a interface gráfica
script.py       → a "state machine": toda a sequência de ações do ciclo
hotkey.py       → estado compartilhado (ligado/desligado, contador, tempo) + hotkey F8
esperarf.py     → função de espera interrompível, sincronizada com o hotkey
detector.py     → reconhecimento de imagem na tela (visão computacional)
acoes.py        → ações de baixo nível (segurar tecla, detectar + agir, etc.)
interface.py    → interface gráfica (status, contador, tempo, log)
```

## Desafios técnicos que resolvi

- **Sincronização de tecla dupla (WASD diagonal):** o `pyautogui` tem uma pausa automática de 0.1s entre comandos, o que fazia o personagem desviar de rota ao segurar duas teclas ao mesmo tempo. Resolvido desativando essa pausa (`pyautogui.PAUSE = 0`).

- **Toques únicos ignorados pelo jogo:** `pyautogui.press()` executa `keyDown`+`keyUp` rápido demais para o jogo detectar. Resolvido substituindo por uma função própria que segura a tecla por um intervalo mínimo controlado.

- **Variação de layout entre execuções:** ao invés de mapear e detectar cada variação possível do primeiro ambiente do jogo, optei por um comportamento genérico com timeout de segurança — mais simples e igualmente robusto na prática.

- **Estado compartilhado entre arquivos:** usar `from arquivo import variavel` copia o valor no momento da importação, "congelando" um dado que muda ao longo da execução (como o estado ligado/desligado). Resolvido acessando sempre via `import arquivo` + `arquivo.variavel`, garantindo leitura do valor atual.

- **Interrupção responsiva em qualquer ponto do fluxo:** inicialmente o macro só conseguia pausar entre ciclos completos. Implementei uma função de espera fatiada (checagem a cada 0.1s) combinada com saída antecipada da função principal, permitindo interromper o macro em qualquer ponto do fluxo, sem deixar teclas presas.

- **Hotkey perdida durante movimentos longos:** o pressionamento de F8 era ocasionalmente ignorado especificamente durante movimentos de vários segundos com tecla segurada — provavelmente por repetição automática do sistema operacional competindo pela mesma fila de eventos de teclado. Resolvido trocando de detecção por evento (`add_hotkey`) para verificação ativa de estado (`is_pressed`) dentro do próprio loop de espera.

- **Interface gráfica e macro rodando em paralelo:** como o loop do macro é bloqueante (roda indefinidamente) e a interface gráfica também precisa de seu próprio loop contínuo, executei o macro em uma thread separada (`threading`), comunicando-se com a interface através de variáveis compartilhadas.

## Como rodar

**Opção 1 — Executável (mais simples):**

Baixe o `.exe` na pasta de releases e dê dois cliques. Não é necessário ter Python instalado.

**Opção 2 — Código-fonte:**

Abra um terminal (pode ser o terminal integrado do VS Code) na pasta do projeto e rode:

```bash
pip install pyautogui opencv-python keyboard customtkinter pillow
python main.py
```

Em ambos os casos, com o jogo aberto, você precisa estar posicionado no ponto de respawn do Zagreus, logo à frente da piscina de Estige (como mostrado no primeiro vídeo de demonstração), e apertar **F8** para ligar o macro e **F8** novamente para desligar a qualquer momento.


## Demonstração


https://github.com/user-attachments/assets/9ba0cf42-a56a-420f-ad0a-de2bba9ad4e8



https://github.com/user-attachments/assets/6d8a56d9-538c-4a35-8d2d-91546d663e3f

<br><br>

> **Nota:** o antivírus do Windows pode sinalizar o executável como suspeito — isso é um falso positivo comum em arquivos gerados pelo PyInstaller, não indicativo de vírus real. O código-fonte está disponível para conferência.
>
> Se o Defender bloquear ou colocar o arquivo em quarentena: vá em **Segurança do Windows → Proteção contra vírus e ameaças → Histórico de proteção**, encontre o arquivo e clique em **Restaurar**. Para evitar o bloqueio novamente, adicione o arquivo (ou a pasta do projeto) em **Gerenciar configurações → Exclusões → Adicionar ou remover exclusões**.
---

Projeto desenvolvido como primeiro contato prático com programação aplicada, combinando visão computacional, automação de input, concorrência (threads) e interface gráfica.
