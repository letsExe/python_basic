class Main:
    pass

from Cliente import Cliente
from Conta import Conta

cliente1 = Cliente("Leticia", "1234-5678")

conta1 = Conta(cliente1.get_nome(), "009a",650)

conta1.depositar(1000)
conta1.saque(50)
conta1.extrato();