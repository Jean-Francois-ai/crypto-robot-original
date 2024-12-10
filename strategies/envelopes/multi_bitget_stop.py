import datetime
import sys

sys.path.append("./Live-Tools-V2")

import asyncio
from utilities.bitget_perp import PerpBitget
from secret import ACCOUNTS
import ta

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


async def main():
    account = ACCOUNTS["bitget1"]

    margin_mode = "isolated"  # isolated or crossed
    leverage = 8
    hedge_mode = True

    tf = "1h"
    sl = 0.3
    params = {
        params = {
        "BTC/USDT": {
            "src": "close",
            "ma_base_window": 7,
            "envelopes": [0.07, 0.1, 0.15],
            "size": 0.1,
            "sides": ["long", "short"],
        },
        "ETH/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15],
            "size": 0.1,
            "sides": ["long", "short"],
        },
        "ADA/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.09, 0.12, 0.15],
            "size": 0.1,
            "sides": ["long", "short"],
        },
        "AVAX/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.09, 0.12, 0.15],
            "size": 0.1,
            "sides": ["long", "short"],
        },
        "AAVE/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.09, 0.12],
            "size": 0.1,
            "sides": ["long", "short"],
        },
        "APE/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.09, 0.12],
            "size": 0.1,
            "sides": ["long", "short"],
        },
        "AXS/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.09, 0.12],
            "size": 0.1,
            "sides": ["long", "short"],
        },
        "BNB/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15],
            "size": 0.1,
            "sides": ["long", "short"],
        },
        "CRV/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15],
            "size": 0.1,
            "sides": ["long", "short"],
        },
        "DOGE/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15],
            "size": 0.1,
            "sides": ["long", "short"],
        },
        "DOT/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15],
            "size": 0.1,
            "sides": ["long", "short"],
        },
        "DYDX/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15],
            "size": 0.1,
            "sides": ["long", "short"],
        },
        "FIL/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15],
            "size": 0.1,
            "sides": ["long", "short"],
        },
        "FTM/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15],
            "size": 0.1,
            "sides": ["long", "short"],
        },
        "GALA/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15],
            "size": 0.1,
            "sides": ["long", "short"],
        },
        "GMT/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15],
            "size": 0.1,
            "sides": ["long", "short"],
        },
        "GRT/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15],
            "size": 0.1,
            "sides": ["long", "short"],
        },
        "KNC/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15],
            "size": 0.1,
            "sides": ["long", "short"],
        },
        "KSM/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15],
            "size": 0.1,
            "sides": ["long", "short"],
        },
        "LRC/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15],
            "size": 0.1,
            "sides": ["long", "short"],
        },
        "MANA/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15],
            "size": 0.1,
            "sides": ["long", "short"],
        },
        "MASK/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15],
            "size": 0.1,
            "sides": ["long", "short"],
        },
        "NEAR/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15],
            "size": 0.1,
            "sides": ["long", "short"],
        },
        "ONE/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15],
            "size": 0.1,
            "sides": ["long", "short"],
        },
        "OP/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15],
            "size": 0.1,
            "sides": ["long", "short"],
        },
        "SAND/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15],
            "size": 0.1,
            "sides": ["long", "short"],
        },
        "SHIB/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15],
            "size": 0.1,
            "sides": ["long", "short"],
        },
        "SOL/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15],
            "size": 0.1,
            "sides": ["long", "short"],
        },
        "STG/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15],
            "size": 0.1,
            "sides": ["long", "short"],
        },
        "WOO/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15],
            "size": 0.1,
            "sides": ["long", "short"],
        },
        "EGLD/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15],
            "size": 0.1,
            "sides": ["long", "short"],
        },
        "LTC/USDT": {
            "src": "close",
            "ma_base_window": 5,
            "envelopes": [0.07, 0.1, 0.15],
            "size": 0.1,
            "sides": ["long", "short"],
        },
    }
    }

    exchange = PerpBitget(
        public_api=account["public_api"],
        secret_api=account["secret_api"],
        password=account["password"],
    )

    invert_side = {"long": "sell", "short": "buy"}
    print(
        f"--- Execution started at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---"
    )

    try:
        await exchange.load_markets()

        for pair in params.copy():
            info = exchange.get_pair_info(pair)
            if info is None:
                print(f"Pair {pair} not found, removing from params...")
                del params[pair]

        pairs = list(params.keys())

        print(f"Setting {margin_mode} x{leverage} on {len(pairs)} pairs...")
        tasks = [
            exchange.set_margin_mode_and_leverage(pair, margin_mode, leverage)
            for pair in pairs
        ]
        await asyncio.gather(*tasks)

        print(f"Getting data and indicators on {len(pairs)} pairs...")
        tasks = [exchange.get_last_ohlcv(pair, tf, 50) for pair in pairs]
        dfs = await asyncio.gather(*tasks)
        df_list = dict(zip(pairs, dfs))

        for pair in df_list:
            current_params = params[pair]
            df = df_list[pair]
            src = df["close"] if current_params["src"] == "close" else (
                df["close"] + df["high"] + df["low"] + df["open"]) / 4

            df["ma_base"] = ta.trend.sma_indicator(
                close=src, window=current_params["ma_base_window"]
            )
            high_envelopes = [
                round(1 / (1 - e) - 1, 3) for e in current_params["envelopes"]
            ]
            for i in range(1, len(current_params["envelopes"]) + 1):
                df[f"ma_high_{i}"] = df["ma_base"] * (1 + high_envelopes[i - 1])
                df[f"ma_low_{i}"] = df["ma_base"] * (
                    1 - current_params["envelopes"][i - 1]
                )

            df_list[pair] = df

        usdt_balance = await exchange.get_balance()
        usdt_balance = usdt_balance.total
        print(f"Balance: {round(usdt_balance, 2)} USDT")

        tasks = [exchange.get_open_trigger_orders(pair) for pair in pairs]
        print(f"Getting open trigger orders...")
        trigger_orders = await asyncio.gather(*tasks)
        trigger_order_list = dict(zip(pairs, trigger_orders))

        tasks = []
        for pair in df_list:
            params[pair]["canceled_orders_buy"] = len(
                [
                    order
                    for order in trigger_order_list[pair]
                    if order.side == "buy" and not order.reduce
                ]
            )
            params[pair]["canceled_orders_sell"] = len(
                [
                    order
                    for order in trigger_order_list[pair]
                    if order.side == "sell" and not order.reduce
                ]
            )
            tasks.append(
                exchange.cancel_trigger_orders(
                    pair, [order.id for order in trigger_order_list[pair]]
                )
            )
        print(f"Canceling trigger orders...")
        await asyncio.gather(*tasks)

        tasks = [exchange.get_open_orders(pair) for pair in pairs]
        print(f"Getting open orders...")
        orders = await asyncio.gather(*tasks)
        order_list = dict(zip(pairs, orders))

        tasks = []
        for pair in df_list:
            params[pair]["canceled_orders_buy"] += len(
                [
                    order
                    for order in order_list[pair]
                    if order.side == "buy" and not order.reduce
                ]
            )
            params[pair]["canceled_orders_sell"] += len(
                [
                    order
                    for order in order_list[pair]
                    if order.side == "sell" and not order.reduce
                ]
            )
            tasks.append(
                exchange.cancel_orders(pair, [order.id for order in order_list[pair]])
            )
        print(f"Canceling limit orders...")
        await asyncio.gather(*tasks)

        print(f"Getting live positions...")
        positions = await exchange.get_open_positions(pairs)
        tasks_close = []
        tasks_open = []

        for position in positions:
            print(
                f"Current position on {position.pair} {position.side} - {position.size} ~ {position.usd_size} $"
            )
            row = df_list[position.pair].iloc[-2]
            tasks_close.append(
                exchange.place_order(
                    pair=position.pair,
                    side=invert_side[position.side],
                    price=row["ma_base"],
                    size=exchange.amount_to_precision(position.pair, position.size),
                    type="limit",
                    reduce=True,
                    margin_mode=margin_mode,
                    error=False,
                )
            )
            if position.side == "long":
                sl_side = "sell"
                sl_price = exchange.price_to_precision(
                    position.pair, position.entry_price * (1 - sl)
                )
            else:  # short
                sl_side = "buy"
                sl_price = exchange.price_to_precision(
                    position.pair, position.entry_price * (1 + sl)
                )
            tasks_close.append(
                exchange.place_trigger_order(
                    pair=position.pair,
                    side=sl_side,
                    trigger_price=sl_price,
                    price=None,
                    size=exchange.amount_to_precision(position.pair, position.size),
                    type="market",
                    reduce=True,
                    margin_mode=margin_mode,
                    error=False,
                )
            )

        print(f"Placing {len(tasks_close)} close SL / limit order...")
        await asyncio.gather(*tasks_close)

        await exchange.close()
        print(
            f"--- Execution finished at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---"
        )
    except Exception as e:
        await exchange.close()
        raise e


if __name__ == "__main__":
    asyncio.run(main())
