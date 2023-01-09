

vam=eval(input("meghdare vam : "))
bahre=eval(input("darsade bahre : "))
sal=int(input("tedade sal : "))

def mounthly(p,r,d):
    if r==0:
        mo=p/d
        
    else:
        mo=(p*(r*(1+r)**d))/(((1+r)**d)-1)
    return mo


        
print (mounthly(vam,bahre,sal))
    
