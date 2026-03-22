import pytest

from bank_account import BankAccount


# ══ Тесты инициализации ══════════════════════════════════════════════
def test_create_account_with_balance():
    """Счёт создаётся с правильным владельцем и балансом."""
    acc = BankAccount("Петров П.П.", 10000)
    assert acc.owner == "Петров П.П."
    assert acc.balance == 10000


def test_create_account_default_balance():
    """При создании без баланса — баланс равен 0."""
    acc = BankAccount("Сидоров С.С.")
    assert acc.balance == 0


# ══ Тесты пополнения ═════════════════════════════════════════════════
def test_deposit_increases_balance():
    """Пополнение увеличивает баланс на правильную сумму."""
    acc = BankAccount("Тест", 1000)
    acc.deposit(500)
    assert acc.balance == 1500


def test_deposit_zero_raises_error():
    """Пополнение на 0 вызывает ValueError."""
    acc = BankAccount("Тест", 1000)
    with pytest.raises(ValueError):
        acc.deposit(0)



def test_deposit_negative_raises_error():
    """Пополнение на отрицательную сумму вызывает ValueError."""
    acc = BankAccount("Тест", 1000)
    with pytest.raises(ValueError):
        acc.deposit(-100)


# ══ Тесты снятия ═════════════════════════════════════════════════════
def test_withdraw_decreases_balance():
    """Снятие уменьшает баланс на правильную сумму."""
    acc = BankAccount("Тест", 2000)
    acc.withdraw(800)
    assert acc.balance == 1200



def test_withdraw_full_balance():
    """Можно снять весь баланс."""
    acc = BankAccount("Тест", 500)
    acc.withdraw(500)
    assert acc.balance == 0



def test_withdraw_more_than_balance_raises_error():
    """Снятие суммы больше баланса вызывает ValueError."""
    acc = BankAccount("Тест", 300)
    with pytest.raises(ValueError):
        acc.withdraw(500)



def test_withdraw_zero_raises_error():
    """Снятие 0 вызывает ValueError."""
    acc = BankAccount("Тест", 1000)
    with pytest.raises(ValueError):
        acc.withdraw(0)


# ══ Тест метода get_info ═════════════════════════════════════════════
def test_get_info_format():
    """get_info возвращает строку в правильном формате."""
    acc = BankAccount("Козлов К.К.", 7500)
    info = acc.get_info()
    assert "Козлов К.К." in info
    assert "7500" in info
