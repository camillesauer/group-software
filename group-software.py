import random as rd
participants=[]

def add_participants(x):
    return participants.append(x)

def question_participant():
    print("Another one more participant?") 
    return input()

def add_more_participants():
    while question_participant() == 'yes': 
        print("Who are the participants?") 
        new_participant = input()
        add_participants(new_participant)
        print(participants)

def person_number(participants):
    """ Fonction qui demande un nombre et le renvoie en vérifiant que c'est un chiffre et que le chiffre est conforme pour que les groupes soient valides """
    print("Entrez le nombre de personnes par groupe :")
    num_to_select_input=input() #Demande un chiffre
    while not num_to_select_input.isdigit() or int(num_to_select_input) > len(participants)//2 or int(num_to_select_input) <= 1:  #Vérifie que l'utilisateur a bien rentré un chiffre valide
        if not num_to_select_input.isdigit(): #Cas où l'entrée n'est pas un chiffre
            print("Entrez le nombre de personnes par groupe EN CHIFFRE :")
            num_to_select_input=input() #Demande un nouveau chiffre
        elif int(num_to_select_input) > len(participants)//2: #Cas où le chiffre est trop grand (génèrerait qu'un seul groupe)
            print("Nombre invalide : Trop grand")
            print("Entrez le nombre de personnes par groupe :")
            num_to_select_input=input() #Demande un nouveau chiffre
        elif int(num_to_select_input) <= 0 : #Cas où le nombre est négatif ou égal à 1 
            print("Nombre invalide : Trop petit")
            print("Entrez le nombre de personnes par groupe :")
            num_to_select_input=input() #Demande un nouveau chiffre
        else:
            break
    return (int(num_to_select_input)) #Renvoie le nombre entré

def p_aleatoire(participants):
    num_to_select=person_number(participants)
    num_of_group = len(participants)//num_to_select
    group=[]
    for i in range(num_of_group): #On itere autant de fois qu'on veut de groupes
        if len(participants)>=num_to_select: #Permet de vérifier qu'il y a assez de personnes pour un groupe complet
            group.append(rd.sample(participants, num_to_select)) #On ajoute un groupe de personnes tirées aléatoirement à une liste
            for j in range(num_to_select): #On itere autant de fois qu'il y a de personnes qui viennent d'être assignées à un groupe
                participants.remove(group[i][j]) #On enleve les personnes qu'on vient de grouper de la liste de départ
        else:
            break #Arrête d'essayer de créer des groupes si il ne reste plus assez de personnes

    for k in range (len(participants)): #On regarde s'il reste des personnes dans le groupe participants
        group[k%len(group)].append(participants[k]) #On les répartit 1 par 1 dans les groupes déjà existants (k%len pour par exemple groupes de 4 avec 11 personnes : on veut que répartir dans les 2 groupes déjà existants)
    print(group)
    return group

def add_competence():
    skill= input() 
    if skill == 'yes': 
        return question_niveau()
    else:
        p_aleatoire(participants)
        return p_aleatoire(participants)
        
def a_competence(participants):
    dico={}
    for participant in participants:
        print("Quelle est la note de {}(1 à 5)".format(participant))
        dico[participant]=input()
    return dico

def question_niveau():
    print("Do you want to share by equal levels?")
    resp=input()
    if resp == 'yes':
         return p_meme_niveau(participants)
    else:
        return p_aleatoire(participants)
    
def p_meme_niveau(participants):
    num_to_select=person_number(participants)
    num_of_group = len(participants)//num_to_select
    group_p=[]
    p_2=sorted(a_competence(participants).items(), key=lambda t: t[1]) #Trie la liste des apprenants en fonction des notes
    for i in range(num_of_group): #On itere autant de fois qu'on veut de groupes
        if len(p_2)-len(group_p)*num_to_select>=num_to_select: #Permet de vérifier qu'il y a assez de personnes pour un groupe complet
            group_p.append([])
            for j in range(num_to_select): #On itere autant de fois qu'il y a de personnes qui viennent d'être assignées à un groupe
                group_p[i].append(p_2[i*num_to_select+j][0])
        else:
            break #Arrête d'essayer de créer des groupes si il ne reste plus assez de personnes

    for k in range (len(participants)-len(group_p)*num_to_select): #On regarde s'il reste des personnes dans le groupe participants
        group_p[-1-k%len(group_p)].append(p_2[-1-k][0]) #On les répartit 1 par 1 dans les groupes déjà existants en commençant par les plus proches en niveau (k%len pour par exemple groupes de 4 avec 11 personnes : on veut que répartir dans les 2 groupes déjà existants)
    return group_p    
    
print("Who are the participants?")    
participant1= input()

add_participants(participant1)

print(participants)

add_more_participants()

print(participants)

print("Do you want to add a skill?") 

print(add_competence())  