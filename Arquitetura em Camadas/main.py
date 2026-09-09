from notificadores import NotificadorEmail, NotificadorSMS
from repositorios import VendaArquivoRepository, VendaMemoriaRepository
from servico import VendaService


def main() -> None:
    # Exemplo 1: Persistência em memória e notificação via SMS
    repositorio_memoria = VendaMemoriaRepository()
    notificador_sms = NotificadorSMS()

    servico_sms = VendaService(
        repositorio=repositorio_memoria,
        notificador=notificador_sms,
    )
    servico_sms.processar(cliente="Carlos Lima", valor=200.0, contato="+5511999998888")

    print("-" * 50)

    # Exemplo 2: Persistência em arquivo e notificação via e-mail
    repositorio_arquivo = VendaArquivoRepository()
    notificador_email = NotificadorEmail()

    servico_email = VendaService(
        repositorio=repositorio_arquivo,
        notificador=notificador_email,
    )
    servico_email.processar(cliente="Marina Dias", valor=80.0, contato="marina@email.com")


if __name__ == "__main__":
    main()