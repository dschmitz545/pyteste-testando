from sys import platform
import pytest
from src.funcoesMatematicas import animals, multiplos


@pytest.mark.rabbit
def test_when_number_recive_1_then_must_return_rabbit():
    ent = 1
    espe = "rabbit"
    res = animals(ent)

    assert res == espe


@pytest.mark.rabbit
def test_when_number_recive_2_then_must_return_rabbit():
    ent = 2
    espe = "rabbit"
    res = animals(ent)

    assert res == espe


@pytest.mark.rabbit
def test_when_number_recive_3_then_must_return_rabbit():
    ent = 3
    espe = "rabbit"
    res = animals(ent)

    assert res == espe


@pytest.mark.dog
def test_when_number_recive_4_then_must_return_dog():
    ent = 4
    espe = "dog"
    res = animals(ent)

    assert res == espe


@pytest.mark.skip(reason="wip()work in progress")
def test_when_number_recive_5_then_must_return_dog():

    assert animals(54) == "dog"


@pytest.mark.parametrize(
    "entrada, esperado",
    [
        (3, "Only Three"),
        (6, "Only Three"),
        (9, "Only Three"),
        (12, "Only Three"),
        (15, "Three and Five"),
    ],
)
def test_return_multiples_3(entrada, esperado):
    assert multiplos(entrada) == esperado


@pytest.mark.parametrize(
    "entrada, esperado",
    [
        (5, "Only Five"),
        (10, "Only Five"),
        (15, "Three and Five"),
        (20, "Only Five"),
        (25, "Only Five"),
    ],
)
def test_return_multiples_5(entrada, esperado):
    assert multiplos(entrada) == esperado


# exemplo de xfail
# é esperado que esse teste falhe, se rodar no windows
@pytest.mark.xfail(platform == "win32", reason="Roda apenas se for windows")
def test_xfail_windows():
    pass


# exemplo de skipif
# se a plataforma for windows, pula esse teste
@pytest.mark.skipif(platform == "win32", reason="pula se não for windows")
def test_skipif_windows():
    pass
