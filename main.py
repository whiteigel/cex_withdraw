from config import apikey, secretkey
from apps.functions import get_okx_tokens, get_binance_tokens


def main():
    print(f'Торговые пары OKX: {get_okx_tokens()}')
    print('-'*50)
    print(f'Торговые пары Binance: {get_binance_tokens()}')


if __name__ == '__main__':
    main()