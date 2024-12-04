from python_aternos import Client
atclient = Client()
try:
    atclient.login('BryanNinja007', 'NinjA#2020')  # Utilise tes identifiants Aternos
    print("Connexion à Aternos réussie.")
    aternos_client = True
except Exception as e:
    print(f"Erreur lors de la connexion à Aternos : {e}")
    aternos_client = False

aternos = atclient.account



if aternos_client:
    try:
        servs = aternos.list_servers()
        print("Serveurs Aternos trouvés :", [server for server in servs])
    except Exception as e:
        print(f"Erreur lors de la récupération des serveurs Aternos : {e}")
else:
    print("Connexion à Aternos échouée. Impossible de récupérer les serveurs.")