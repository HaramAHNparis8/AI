

def affichage_tableau(tab):
    for ligne in tab:
        print(" | ".join(ligne))
        print("-" * 9)

def lejeuxfini(tab):
    for ligne in tab:
        if ligne.count('X') == 3 or ligne.count('O') == 3:
            return True
    for colonne in range(3):
        if tab[0][colonne] == tab[1][colonne] == tab[2][colonne] and tab[0][colonne] in ['X', 'O']:
            return True
    if tab[0][0] == tab[1][1] == tab[2][2] and tab[0][0] in ['X', 'O']:
        return True
    if tab[0][2] == tab[1][1] == tab[2][0] and tab[0][2] in ['X', 'O']:
        return True
    return False

def animation(tab):
    nbligne2_X = compter_ligne(tab, 'X', 2)
    nblign1_X = compter_ligne(tab, 'X', 1)
    nblign2_O = compter_ligne(tab, 'O', 2)
    nblign1_O = compter_ligne(tab, 'O', 1)
    return (3 * nbligne2_X + nblign1_X) - (3 * nblign2_O + nblign1_O)

def possibilité_bouge(tab):
    bouge = []
    for ligne in range(3):
        for colonne in range(3):
            if tab[ligne][colonne] == " ":
                bouge.append((ligne, colonne))
    return bouge

def compter_ligne(tab, symbol, num_symbols):
    count = 0
    for ligne in tab:
        if ligne.count(symbol) == num_symbols:
            count += 1
    for colonne in range(3):
        if [tab[ligne][colonne] for ligne in range(3)].count(symbol) == num_symbols:
            count += 1
    if [tab[i][i] for i in range(3)].count(symbol) == num_symbols:
        count += 1
    if [tab[i][2 - i] for i in range(3)].count(symbol) == num_symbols:
        count += 1
    return count

def contrôle_bouge(tab, bouge, symbol):
    ligne, colonne = bouge
    if tab[ligne][colonne] == " ":
        tab[ligne][colonne] = symbol
    return tab

def minimax(tab, profondeur, maxalisé_joeur):
    if profondeur == 0 or lejeuxfini(tab):
        return animation(tab)

    if maxalisé_joeur:
        max_évalu = float('-inf')
        for bouge in possibilité_bouge(tab):
            tab_nouveau = contrôle_bouge([ligne[:] for ligne in tab], bouge, 'X')
            eval = minimax(tab_nouveau, profondeur - 1, False)
            max_évalu = max(max_évalu, eval)
        return max_évalu
    else:
        min_eval = float('inf')
        for bouge in possibilité_bouge(tab):
            tab_nouveau = contrôle_bouge([ligne[:] for ligne in tab], bouge, 'O')
            eval = minimax(tab_nouveau, profondeur - 1, True)
            min_eval = min(min_eval, eval)
        return min_eval

# 게임 시작
def play_tic_tac_toe():
    tab = [[" " for _ in range(3)] for _ in range(3)]
    user_symbol = 'X'
    ai_symbol = 'O'
    
    while True:
        affichage_tableau(tab)
        
  
        while True:
            ligne = int(input("Entrez la ligne (0, 1, ou 2): "))
            colonne = int(input("Enterez la colonne (0, 1, ou 2): "))
            if 0 <= ligne < 3 and 0 <= colonne < 3 and tab[ligne][colonne] == " ":
                tab = contrôle_bouge(tab, (ligne, colonne), user_symbol)
                break
            else:
                print("c'est pas la bonne valeur, veuillez ré-essayer")
        
        if lejeuxfini(tab):
            affichage_tableau(tab)
            if animation(tab) == 1:
                print("vous avez perdu")
            else:
                
                print("vous avez gagné")
            break


        meilleur_bouge = None
        meillieur_valeur = float('-inf')
        for bouge in possibilité_bouge(tab):
            tab_nouveau = contrôle_bouge([ligne[:] for ligne in tab], bouge, ai_symbol)
            valeur = minimax(tab_nouveau, 3, False)
            if valeur > meillieur_valeur:
                meillieur_valeur = valeur
                meilleur_bouge = bouge

        print("IA Bouge:")
        tab = contrôle_bouge(tab, meilleur_bouge, ai_symbol)




play_tic_tac_toe()
n = int(input("vous voulez recommencer? si oui entrez 1 sinon 0 (0, 1)"))
if(n == 1):
    while(n == 1):
        play_tic_tac_toe()
        n = int(input("vous voulez recommencer? si oui entrez 1 sinon 0 (0, 1)"))

