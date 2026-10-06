# %%
nume=input("numele tau este: ")
varsta = input("varsta este: ")

print("buna", nume, "!")
print(nume,"are", varsta, "ani.")

# %%
a=int(input(" a = "))
b=int(input(" b= "))
suma=a+b
print(a)
print (b)
print("suma este:", suma)

# %%
a=input("a=")
b=input("b=" )
print (a+b)

# %%
a=int(input(" a = "))
b=int(input(" b= "))
suma=a+b
diferenta=a-b
produsul=a*b
media=(a+b)/2;
catul=a//b
restul=a%b
patrat_a=a**2
patrat_b=b**2

print(suma)
print(diferenta)
print(produsul)
print(media)
print(catul)
print(restul)
print(patrat_a)
print(patrat_b)


# %%
pret_initial= int(input ("pret_initial= "))

pret_final=pret_initial+(pret_initial*19)/100
print (pret_final)

# %%
m=int(input("m= "))

ore=m//60
minute=m%60
print(ore,minute)

# %%
numar=int(input("numar="))
u=numar%10
z=numar//10

suma=u+z

print(suma)

# %%
varsta = int(input())
raspuns = input("Are card? da/nu: ").lower()
are_card = raspuns == "da"
print(varsta)
print(are_card)
reducere = varsta < 18 or varsta > 60 or are_card == True
print(reducere)

# %%
nota_ex = int(input())
nota_seminar=int(input())

nota_fin= (40 * nota_seminar)/100 + (60 * nota_ex)/100

promoveaza = nota_ex >= 5 and nota_fin >= 5
print(promoveaza)

