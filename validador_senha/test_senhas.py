from verificador_senhas_auto import verifica_senha

def test_senha_valida():
    assert verifica_senha("Senha123!") == []

def test_senha_curta():
    assert "Senha muito curta" in verifica_senha("S1!")

def test_falta_maiuscula():
    assert "Falta letra maiúscula" in verifica_senha("senha123!")

def test_falta_minuscula():
    assert "Falta letra minúscula" in verifica_senha("SENHA123!")

def test_falta_numero():
    assert "Falta número" in verifica_senha("SenhaTest!")

def test_falta_caractere_especial():
    assert "Falta caractere especial" in verifica_senha("Senha123")

def test_tem_espaco():
    assert "Contém espaços" in verifica_senha("Senha 123!")
