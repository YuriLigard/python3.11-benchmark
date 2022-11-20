# Erros com os quais me deparei e suas resoluções 

  >
  
  #### 1. Erro:
  > ModuleNotFoundError: No module named ...
  
  - Ocorreu por motivo do python não conseguir resolver o nome do modulo em **sys.path**, uma lista de strings que especifica o caminho de pesquisa para módulos. Inicializado a partir da variável de ambiente **PYTHONPATH**.
  >

  #### 1.1 Solução
  
  - Adicionar o caminho raiz do projeto a variável de ambiente **PYTHONPATH** com o seguinte comando:

    - Linux 
        > export PYTHONPATH="${PYTHONPATH}:/path/to/your project/"

    - Windowns 
        > set PYTHONPATH=%PYTHONPATH%;C:\path\to\your\project\
        
   #### 1.2 Fonte:
   - [towardsdatascience.com](https://towardsdatascience.com/how-to-fix-modulenotfounderror-and-importerror-248ce5b69b1c)
  
   - [docs.python](https://docs.python.org/3/library/sys.html)
  >

---
#### 2. Erro:

 > standard_init_linux.go:228: exec user process caused: exec format error

- Esqueci de adicionar o shebang no aquivo [medidor.py](medidor.py) (#!) 
-  Refere-se a um conjunto de caracteres exclusivos incluídos no início de um arquivo de script. Um shebang define o tipo e o caminho do programa que deve executar o script.
  
#### 2.1 Solução 
  - Adicionar 
    ```python
     #!/usr/bin/env python3 
     ```
  
#### 2.2 Outras possíveis causas

   - [Aqui 🤔](https://bugfreesoft.com/standard-init-linux-go-228/)