# Coisas que aprendi 

## 1. Módulo ```__future__```

  - É um módulo embutido no **Python** que é usado para herdar novos recursos que estarão disponíveis nas novas versões.
  - Este módulo inclui todas as funções mais recentes que não estavam presentes na versão anterior do Python.

## 1.1 Uso
- Usei para expecificar _type hints_ [PEP 526](https://peps.python.org/pep-0526/) no código [buscaBinaria](code/buscaBinaria.py)

```Python
    from __future__ import annotations
```
- **annotations** expecificado em [PEP 563](https://peps.python.org/pep-0563/)

## 1.2 Fonte
-  [Docs Python](https://docs.python.org/pt-br/3/library/__future__.html)
-  [Geeks forgeeks](https://www.geeksforgeeks.org/__future__-module-in-python/)