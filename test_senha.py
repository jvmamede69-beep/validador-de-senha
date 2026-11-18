from senha import senha_forte, validar_senha


def test_senha_forte_e_aceita():
    assert senha_forte("Manaus@2026")
    assert validar_senha("Manaus@2026") == []


def test_senha_curta_e_rejeitada():
    assert not senha_forte("Ab1@")


def test_sem_maiuscula():
    problemas = validar_senha("manaus@2026")
    assert "Deve ter pelo menos uma letra maiúscula." in problemas


def test_sem_minuscula():
    problemas = validar_senha("MANAUS@2026")
    assert "Deve ter pelo menos uma letra minúscula." in problemas


def test_sem_numero():
    problemas = validar_senha("Manaus@Amazonas")
    assert "Deve ter pelo menos um número." in problemas


def test_sem_especial():
    problemas = validar_senha("Manaus2026")
    assert "Deve ter pelo menos um caractere especial." in problemas


def test_com_espaco():
    problemas = validar_senha("Manaus @2026")
    assert "Não pode conter espaços." in problemas


def test_senha_vazia_tem_varios_problemas():
    assert len(validar_senha("")) >= 4
