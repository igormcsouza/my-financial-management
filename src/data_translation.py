from dataclasses import dataclass


@dataclass
class Headers:
    STAMP = 'Carimbo de data/hora'
    DESCRIPTION = 'Descrição da Transação'
    DATE = 'Data da Transação '
    AMOUNT = 'Valor da Transação'
    RESPONSABLE = 'Responsável pela Transação'
    TYPE = 'Tipo de Transação'
    METHOD = 'Método de pagamento'
    CATEGORY = 'Categoria da Transação'
    RECEIPT = 'Upload do Comprovante'


@dataclass
class TransactionType:
    INCOMING = 'Entrada'
    OUTGOING = 'Saída'


@dataclass
class Categories:
    FOOD = 'Alimentação'
    HEALTH = 'Saúde'
    SALARY = 'Salário'
    CLOTHING = 'Vestuário'
    PLAY = 'Lazer'
    TRANSPORTATION = 'Transporte'
    BILLS = 'Contas Fixas'
    THITHING = 'Dízimos e Ofertas'
    ANIMALS = 'Animais de Estimação'
    OTHERS = 'Outros'


@dataclass
class Methods:
    CREDIT = 'Crédito/Financiamento/Empréstimo'
    DEBIT = 'Débito/Pix/Dinheiro' 


def get_language(language: str) -> object:
    if language == 'por':
        return PortugueseLabels
    else:
        raise ValueError('This language was not implemented yet.')


@dataclass
class PortugueseLabels:
    TITLE = "Gerenciamento Financeiro"
    CONFIGURATION_TITLE = "Configurações"
    SHOW_DATA = "Mostrar Planilha"
    SEE_ENTIRE_TABLE = "Veja a tabela todos os dados"
    DATE_RANGE = dict(initial="Início do Ciclo:", final="Final do Cíclo:")
    DATA_SUMMURY = "Resumo dos Gastos no Período"
    RESERVED_4_FOOD = "$ Reservado para essas Alimentação/Outros:"
    BUTTON_DEFAULT_LABEL = "Calcular"
    WAITING_2_START = "Aguardando os parametros."
