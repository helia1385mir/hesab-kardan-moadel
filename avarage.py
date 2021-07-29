name=input('esmetan ra vared konid')
family=input('familetan ra vared konid')
avarage1=int(input('nomre1:'))
avarage2=int(input('nomre2:'))
avarage3=int(input('nomre3:'))
moadel=(avarage1+avarage2+avarage3)/3
if moadel>=17:
    print('great')
elif moadel<17 and moadel==12 and moadel>12 :
    print('normal')
elif  moadel<12 :
    print('fail')

print(name,family,'moadel shoma',moadel)