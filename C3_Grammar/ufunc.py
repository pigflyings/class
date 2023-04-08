#电费计算：(期末读数 - 期初读数)*单价
def costCompute(iStart, iEnd):
    iConsume = iEnd - iStart
    return iConsume*0.85

f=0
fElecFee1 = costCompute(1201,1786)
fElecFee2 = costCompute(1322,1423)
print("Electronic Power Cost of Mr Zhang：",fElecFee1)
c=5/9*(f-32)
if f==60:
    print("c=",c)