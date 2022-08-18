# Aprendendo um pouco do PyTest

## Considerações para rodar o pytest

- o projeto precisa ter uma pasta tests
- os arquivos de teste precisam iniciar com test_quaquer_coisa
- no diretório tests, precisa ter o arquivo **init**.py

### Rodando

```python
pytest
pytest .
```

### com modo verboso

```bash
pytest -v
```

### rodar sem criar o **init**.py na pasta test

```bash
python -m pytest
```

### para quando um teste falhar - Saída rápida

```bash
pytest -x
```

### Mostra as saídas no console - mostrar conteudo dos prints()

```bash
pytest -s
```

### Filtra resultado, por qualquer parte do nome da função de teste

```bash
pytest -k "nome_do_teste"
```

### para para debugar quando der erro

```bash
> pytest --pdb
```

### gerar report em modo junit

```bash
> pytest --junitxml report.xml
```

### Mark (Marcações)

- ajuda a montar grupos para testes especificos

#### na raiz do projeto criar arquivo

> pytest.ini

- dentro do arquivo pytest.ini

```ini
[pytest]
markers =
     rabbit: mark test with rabbit
```

### no arquivo de test

```python
import pytest

@pytest.mark.rabbit
```

### para rodar

```bash
pytest -m suatag
```

### com modo verboso junto

```bash
pytest -m suatag -v
```

### invertendo

```bash
pytest -m "not rabbit" -v
```

### Tags Especiais

```python
@pytest.mark.skip(reason="not implemented") # skipa um teste
```

```bash
pytest -rs  # mostra razaão e o teste skipado
```

```python

@pytest.mark.parametrize("entrada, esperado", [(5, "Only Five"), (10,"Only Five"), (15, "Three and Five"), (20,"Only Five"), (25,"Only Five")])
def test_return_multiples_5(entrada, esperado):
     assert multiplos(entrada) == esperado
```

### exemplo de xfail

- é esperado que esse teste falhe, se rodar no windows

```python
@pytest.mark.xfail(sys.platform == 'win32', reason="Roda apenas se for windows")
def test_xfail_windows():
    pass
```

### exemplo de skipif

- se a plataforma for windows, pula esse teste

```python
@pytest.mark.skipif(sys.platform == 'win32', reason="pula se não for windows")
def test_skipif_windows():
    pass

```

### Executando

```bash
pytest -m "meu_marcador"
pytest -m "meu_marcador" -v     # com modo verboso junto
```
