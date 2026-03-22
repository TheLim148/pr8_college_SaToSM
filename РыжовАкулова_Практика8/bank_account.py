class BankAccount:
    """
    Модель банковского счёта клиента.

    Attributes:
        owner (str): Имя владельца счёта.
        balance (float): Текущий баланс счёта в рублях.

    Example:
        >>> acc = BankAccount("Иванов И.И.", 5000)
        >>> acc.deposit(2000)
        >>> acc.balance
        7000
    """

    def __init__(self, owner: str, balance: float = 0) -> None:
        """
        Создаёт банковский счёт с указанным владельцем и начальным балансом.

        Args:
            owner (str): Имя владельца счёта.
            balance (float, optional): Начальный баланс счёта. По умолчанию 0.

        Example:
            >>> acc = BankAccount("Петров П.П.", 1500)
            >>> acc.owner
            'Петров П.П.'
            >>> acc.balance
            1500
        """
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """
        Пополняет счёт на указанную сумму.

        Args:
            amount (float): Сумма пополнения. Должна быть > 0.

        Raises:
            ValueError: Если сумма <= 0.
        """
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть больше 0.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Снимает деньги со счёта.

        Args:
            amount (float): Сумма снятия. Должна быть > 0 и <= balance.

        Raises:
            ValueError: Если сумма <= 0 или превышает баланс.
        """
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть больше 0.")
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счёте.")
        self.balance -= amount

    def get_info(self) -> str:
        """
        Возвращает строку с информацией о счёте.

        Returns:
            str: Строка вида "Владелец: Иванов И.И. | Баланс: 5000 руб.".
        """
        return f"Владелец: {self.owner} | Баланс: {self.balance:g} руб."
