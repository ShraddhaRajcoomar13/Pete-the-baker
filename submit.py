def cakes(recipe, available):
    j={}
    for k1,v1 in recipe.items():
        for k2,v2 in available.items():
            if k1==k2:
                p=int(v2/v1)
                j[k1]=p
    ams=[v3 for k3,v3 in j.items()]
    if len(j)==len(recipe):
        return min(ams)
    else:
        return 0
