def cost(istart,iend):
    iconsume=(iend-istart)*0.85
    return iconsume
elecfeel= cost(1000,1200)
print("cost",elecfeel)
