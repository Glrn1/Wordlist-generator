list=[]
Nomes=[]
temp_Nomes=[]
Telefone=''
Simbolos=''
dob=input("Data de nascimento(DDMMYYYY): ")
if(len(dob)==8):
    Dia=dob[:2]
    Mes=dob[2:4]
    Ano=dob[4:]
else:
    print("Formato errado para data de nascimento, tente igual a esse formato > DDMMYYYY")
    exit()

Telefone=input("Numero de Telefone: ")
Simbolos=input("Caracter Especial: ")
def ListOfImportantWords():
    Nomes.append(input("Primeiro Nome: "))
    Nomes.append(input("Sobrenome: "))
    Nomes.append(input("Nickname: "))
    Nomes.append(input("Apelido: "))
    Nomes.append(input("Nome de um parente: "))
    Nomes.append(input("Nome do animal de estimação: "))
    Nomes.append(input("Nome da namorada(o): "))
    Nomes.append(input("Nome do filho(a): "))
    Nomes.append(input("Apelido do filho(a): "))
    Nomes.append(input("Cidade: "))
    Nomes.append(input("Pais: "))
    Nomes.append(input("Cor favorita: "))
    print("Tecle Enter: ")

    while True:
        inp = input()
        if inp == '':
            break
        Nomes.append(inp)
    while('' in Nomes) : 
        Nomes.remove('') 

def permute(inp): 
    n = len(inp) 
   
    mx = 1 << n 
   
    inp = inp.lower() 
      
    for i in range(mx): 
        combination = [k for k in inp] 
        for j in range(n): 
            if (((i >> j) & 1) == 1): 
                combination[j] = inp[j].upper() 
   
        temp = "" 
        for i in combination: 
            temp += i 
        temp_Nomes.append(temp) 



def WordListCreator(list):
    for word in Nomes:
        for i in range(0,len(word)+1):
            list.append(word[:i]+Dia+Simbolos+word[i:])
            list.append(word[:i]+Mes+Simbolos+word[i:])
            list.append(word[:i]+Dia+Mes+Simbolos+word[i:])
            list.append(word[:i]+Ano+Simbolos+word[i:])
            list.append(word[:i]+Dia+Mes+Ano+Simbolos+word[i:])
            list.append(word[:i]+word+Simbolos+Dia+Mes[i:])
            if len(Ano)==4:
                list.append(word[:i]+Ano[2:]+word[i:])
            list.append(word[:i]+Telefone+word[i:])
    if not Telefone=='':
        list.append(Telefone)

def WriteToFile(list):
    with open('wordlist.txt', 'w') as f:
        for item in list:
            f.write("%s\n" % item)



ListOfImportantWords()
for i in Nomes:
    permute(i)       
Nomes=Nomes+temp_Nomes
WordListCreator(list)
WriteToFile(list)
