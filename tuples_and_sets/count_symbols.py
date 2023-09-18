# text = input()
#
# symbols = {}
#
# for symbol in text:
#     if symbol not in symbols:
#         symbols[symbol] = 1
#     else:
#         symbols[symbol] += 1
#
#
# sorted_symbols = dict(sorted(symbols.items()))
#
# for key, value in sorted_symbols.items():
#     print(f"{key}: {value} time/s")

text = input()

for symbol in sorted(set(text)):
    print(f"{symbol}: {text.count(symbol)} time/s")