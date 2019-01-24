stock_portfolio = {
    'ibm':100,
    'msft':50,
    'snap':120,
    'brk.a':50,
    'brk.b':80
}

print (stock_portfolio.items())
for k,v in stock_portfolio.items():
    print('the key is',k)
    print('the associated value is',v)

print(stock_portfolio['brk.b'])

'''
print(stock_portfolio)
print(stock_portfolio.keys())
keys = list(stock_portfolio.keys())
for k in keys:
    v = stock_portfolio[k]
    print('For stock',k,'I have shares equal to',v)

print(stock_portfolio['brk.a'])
'''