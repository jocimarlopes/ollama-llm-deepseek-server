import logging

def configurar_logger(nome_arquivo="logs.log"):
    logging.basicConfig(
        filename=nome_arquivo,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

def salvar_log(mensagem, nivel=logging.INFO):
    logging.log(nivel, mensagem)
