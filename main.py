from config import apikey, secretkey, password
from apps.functions import get_okx_tokens, get_binance_tokens, get_balance


def main():
    print(f'Торговые пары OKX: {get_okx_tokens()}')
    print('-'*50)
    print(f'Торговые пары Binance: {get_binance_tokens()}')
    print(get_balance(apikey, secretkey, password))


if __name__ == '__main__':
    main()