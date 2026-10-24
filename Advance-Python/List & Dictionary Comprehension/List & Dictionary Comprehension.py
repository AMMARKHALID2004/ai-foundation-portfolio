L1=[item for item in range(10)]
print(L1)

L2=[item**2 for item in L1]
print(L2)


D={
    'Name':"Ammar Khalid",
    'Gender':'Male',
    'Age':21
}

D1={key+' hehe':value for key,value in D.items()}
print(D1)