# Erros com os quais me deparei e suas resoluções 

  >
  
#### 1. Erro:

 > standard_init_linux.go:228: exec user process caused: exec format error

-  Adicionar o shebang no aquivo [medidor.py](medidor.py) (#!) 
-  Refere-se a um conjunto de caracteres exclusivos incluídos no início de um arquivo de script. Um shebang define o tipo e o caminho do programa que deve executar o script.
  
#### 2.1 Solução 
  - Adicionar 
    ```python
     #!/usr/bin/env python3 
     ```
  
#### 2.2 Outras possíveis causas

   - [Aqui 🤔](https://bugfreesoft.com/standard-init-linux-go-228/)