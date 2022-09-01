BDD = {}

def ajouter_nouvel_étudiant(dico,id,family_name,name,gender):
    for key in dico.keys():
        if id == key:
            return -1
    dico[id] = {"prénom":name,"nom":family_name,"est_fille":gender,"notes":[]}
    return 0


def ajouter_note_étudiant(dico,id,note,coef):
    for key in dico.keys():
        if key == id:
            dico[key]["notes"].append((note,coef))
            return 0
    return -1


def avoir_moyenne_pondérée_étudiant(dico,id):
    total_div = 0
    notes_total = 0
    for key in dico.keys():
        if id == key:
            for element in dico[key]["notes"]:
                notes_total += element[0] * element[1]
                total_div += element[1]
            res = notes_total/total_div
            return res
    return -1


def avoir_moyenne_pondérée_générale(dico):
    """Version en utilisant avoir_moyenne_pondérée_étudiant()"""
    if len(dico) == 0:
        return 0
    else:
        notes_total = 0
        for key in dico.keys():
            notes_total += avoir_moyenne_pondérée_étudiant(dico,key)
        res = notes_total/len(dico)
        return res


def avoir_moyenne_pondérée_généralev2(dico):
    """Version sans utiliser avoir_moyenne_pondérée_étudiant()"""
    if len(dico) == 0:
        return 0
    else:
        notes_total = 0
        total_div = 0
        for key in dico.keys():
            for element in dico[key]["notes"]:
                notes_total += element[0] * element[1]
                total_div += element[1]
        res = notes_total/total_div
        return res


       



print(BDD)
print(ajouter_nouvel_étudiant(BDD,1,"famille","prenom",True))
print(ajouter_note_étudiant(BDD,1,1,1))
print(ajouter_note_étudiant(BDD,1,15,2))
print(ajouter_nouvel_étudiant(BDD,2,"famille","prenom",True))
print(ajouter_note_étudiant(BDD,2,1,1))
print(ajouter_note_étudiant(BDD,2,15,2))
print(avoir_moyenne_pondérée_étudiant(BDD,1))
print(avoir_moyenne_pondérée_étudiant(BDD,2))
print(avoir_moyenne_pondérée_générale(BDD))
print(BDD)
