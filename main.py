import ccxt
from pprint import pprint
from config import okx_apikey, okx_secretkey, okx_password, bybit_apikey, bybit_secretkey
from apps.functions import get_okx_tokens, get_binance_tokens, get_balance, get_balance_okx

okx = ccxt.okx({
    'apiKey': okx_apikey,
    'secret': okx_secretkey,
    'password': okx_password
})

bybit = ccxt.bybit({
        'apiKey': bybit_apikey,
        'secret': bybit_secretkey,
    })


def main():
    # print(f'Торговые пары OKX: {get_okx_tokens()}')
    # print('-'*50)
    # print(f'Торговые пары Binance: {get_binance_tokens()}')

    get_balance_okx(okx, 'all')

    print('-' * 50)

    balance = get_balance(okx)
    pprint(f'OKX balance: {balance}')

    print('-'*50)

    balance = get_balance(bybit)
    pprint(f'Bybit balance: {balance}')


if __name__ == '__main__':
    main()