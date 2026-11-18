"""Validador de senha forte.

Uma senha é considerada forte quando atende a todas as regras abaixo.
"""

TAMANHO_MINIMO = 8
ESPECIAIS = "!@#$%&*()-_=+[]{};:,.<>?/|"


def validar_senha(senha: str) -> list[str]:
    """Retorna a lista de problemas encontrados. Lista vazia = senha forte."""
    problemas = []

    if len(senha) < TAMANHO_MINIMO:
        problemas.append(f"Deve ter pelo menos {TAMANHO_MINIMO} caracteres.")
    if not any(c.islower() for c in senha):
        problemas.append("Deve ter pelo menos uma letra minúscula.")
    if not any(c.isupper() for c in senha):
        problemas.append("Deve ter pelo menos uma letra maiúscula.")
    if not any(c.isdigit() for c in senha):
        problemas.append("Deve ter pelo menos um número.")
    if not any(c in ESPECIAIS for c in senha):
        problemas.append("Deve ter pelo menos um caractere especial.")
    if " " in senha:
        problemas.append("Não pode conter espaços.")

    return problemas


def senha_forte(senha: str) -> bool:
    """True se a senha atende a todas as regras."""
    return not validar_senha(senha)


if __name__ == "__main__":
    entrada = input("Digite uma senha para testar: ")
    erros = validar_senha(entrada)
    if erros:
        print("Senha fraca:")
        for erro in erros:
            print(f" - {erro}")
    else:
        print("Senha forte!")
