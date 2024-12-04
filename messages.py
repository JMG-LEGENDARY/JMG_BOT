import random

def message_bienvenue(joueur):
    messages = [
        f"Bienvenue, {joueur} ! Prépare-toi pour une aventure épique !",
        f"Salut {joueur} ! Le serveur t'attendait pour commencer la fête !",
        f"Attention tout le monde ! {joueur} vient de se connecter !",
        f"Hey {joueur} ! C’est parti pour une nouvelle aventure !",
        f"{joueur} a rejoint le serveur ! Que la quête commence !",
        f"Un nouvel aventurier, {joueur}, est parmi nous ! Préparez-vous !",
        f"Bienvenue sur le serveur, {joueur} ! Ton aventure commence maintenant.",
        f"Tout le monde, dites bonjour à {joueur} !",
        f"{joueur} vient de débarquer ! Le serveur est prêt pour toi !",
        f"Un grand salut à {joueur} qui vient de nous rejoindre !",
        f"Le héros de la légende, {joueur}, est enfin arrivé ! ",
        f"Attention ! {joueur} vient de pop comme un creeper derrière toi ! ",
        f"Qui a laissé la porte ouverte ? Ah non, c’est juste {joueur} ! ",
        f"{joueur} est ici ! Que les blocs tremblent ! ",
        f"Et voici {joueur}, prêt à miner tout ce qui bouge ! ",
        f"{joueur} a spawné ! Est-ce que le serveur survivra ? ",
        f"Alerte ! Un nouveau joueur sauvage, {joueur}, est apparu ! ",
        f"Pas de panique, {joueur} est là pour sauver le serveur ! ",
        f"Les zombies ont peur... {joueur} est en ligne ! ",
        f"Si vous voyez {joueur}, restez à l'écart on ne sait jamais ! "
    ]
    message_selectionne = random.choice(messages)
    return message_selectionne

def message_au_revoir(joueur):
    messages_au_revoir = [
        f"Au revoir {joueur} ! Reviens vite avant que le serveur ne s’ennuie !",
        f"{joueur} a quitté le serveur ! Les mobs peuvent respirer... pour l’instant.",
        f"{joueur} s’est déconnecté. Le serveur est un peu plus vide maintenant.",
        f"Bye {joueur} ! N'oublie pas de revenir miner quelques blocs !",
        f"{joueur} a disparu... Mais où est-il parti ?",
        f"Déconnexion de {joueur} : C'est ciaw !",
        f"C’est tout pour aujourd’hui pour {joueur} ! À la prochaine !",
        f"Le monde de Minecraft dit au revoir à {joueur} !",
        f"Ne partez pas tous ! Ah non, c’est juste {joueur} qui s’en va.",
        f"Et voilà, {joueur} a quitté le serveur. Fin de la fête...",
        f"{joueur} est parti, mais le creeper reste... Attention !",
        f"Le serveur perd un aventurier... À bientôt, {joueur} !",
        f"Déconnexion de {joueur}... Une autre aventure l’attend !",
        f"{joueur} s’en va. On parie qu’il revient avec du café ?",
        f"{joueur} a quitté le serveur ! Les moutons peuvent enfin se reposer.",
        f"Bye {joueur} ! N’oublie pas de fermer le portail du Nether en sortant !",
        f"{joueur} s’est déco ! Qui va s’occuper des creepers maintenant ?",
        f"Déconnexion de {joueur}. Le calme revient... pour combien de temps ?",
        f"{joueur} s'en va, mais ses constructions restent !",
        f"À la prochaine, {joueur} ! Le serveur attendra ton retour !"
    ]
    msg = random.choice(messages_au_revoir)
    return msg


