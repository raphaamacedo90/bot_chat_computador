
# Automação com PyAutoGUI: Simulação de Tela de Login no Excel

Este projeto demonstra como usar Python com a biblioteca `pyautogui` para automatizar interações com uma planilha `.xlsx` que simula uma tela de login, útil para:

- Treinamento de automações
- Simulação de processos com interface visual
- Demonstrações educativas

---

## 📂 Estrutura do Projeto

```
📁 bot_chat_computador
├── Login.xlsx              # Planilha simulando a tela de login
├── position.py           # Script para achar a posição
├── main.py               # Script principal de automação com PyAutoGUI
└── README.md              
```

---

## ⚙️ Requisitos

- Python 3.9+
- Biblioteca `pyautogui`
- OnlyOffice Desktop Editors (ou outro app para abrir .xlsx localmente)

```bash
pip install pyautogui
```

---

## 🧠 Como Funciona

1. O script abre automaticamente a planilha `.xlsx`.
2. Aguarda o carregamento da janela.
3. Posiciona o cursor nas células de login e senha e preenche com dados fictícios.
4. Clica no botão "Fazer Login".

---

## 🖱️ Como Obter as Posições

Execute o script abaixo para identificar as posições do mouse na tela:

```python
import pyautogui
import time

print("Coloque o mouse na célula de LOGIN (B2)...")
time.sleep(5)
print("Login B2:", pyautogui.position())

print("Coloque o mouse na célula de SENHA (B3)...")
time.sleep(5)
print("Senha B3:", pyautogui.position())

print("Coloque o mouse sobre o botão 'Fazer Login'...")
time.sleep(5)
print("Botão Login:", pyautogui.position())
```

---

## 🎯 Objetivo

Esse projeto é ideal para quem quer **aprender automações visuais com Python** de forma prática, sem depender de ambientes web ou APIs. Ele serve como base para ideias maiores, como:

- Automatizar ERPs antigos
- Preencher planilhas recorrentes
- Executar tarefas repetitivas

---

## 💡 Autor

Raphael Macedo  
[LinkedIn](https://www.linkedin.com/in/raphael-macedo10/) | [GitHub](https://github.com/raphaamacedo90)
