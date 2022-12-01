# Import des prérequis ##########################
from datetime import datetime                   #
from selenium import webdriver                  #
from selenium.webdriver.common.by import By     #
import mysql.connector                          #
from mysql.connector import errorcode           #
#################################################

# Fonctions persos #############################################################
def getNow():                                                                  #
    try:                                                                       #
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")                    #
    except Exception as ex:                                                    #
        print("/!\\ Erreur, problème de récupération de l'heure actuelle...")  #
        print(ex)                                                              #
                                                                               #
def log(msg):                                                                  #
    try:                                                                       #
        print(getNow(), msg)                                                   #
    except Exception as ex:                                                    #
        print("/!\\ Erreur, problème avec la fonction log()...")               #
        print(ex)                                                              #
                                                                               #
def setValeurInput(cssSel, valeur):                                            #
    try:                                                                       #
        driver.find_element(By.CSS_SELECTOR, cssSel).clear()                   #
        driver.find_element(By.CSS_SELECTOR, cssSel).send_keys(valeur)         #
    except Exception as ex:                                                    #
        log("- Erreur, problème avec la mise à jour de valeur...")             #
        print(ex)                                                              #
################################################################################

# Paramètres ##########################
                                      #
# URL de l'application                #http://gsb-b3/
urlAppli = "http://projetgsb-tibo/"   #
                                      #
# Informations de connexion à la BDD  #
configBdd = {                         #
  'user': 'userGsb',                  #
  'password': 'secret',               #
  'host': 'localhost',                #
  'database': 'gsb_frais',            #
  'raise_on_warnings': True           #
}                                     #
                                      #
# Identifiants visiteur               #
login = 'lvillachane'                 #
mdp = 'jux7g'                         #
#######################################

# Création du navigateur
try:
    driver = webdriver.Chrome()
    print(getNow(), "- Ouverture du navigateur : OK")
except Exception as ex:
    print(getNow(), "- Erreur, problème au lancement du navigateur...")
    print(ex)

# Ouverture de la page de connexion
try:
    driver.get(urlAppli)
    log("- Ouverture de la page de connexion : OK")
except Exception as ex:
    log("- Erreur, problème d'accès à la page de connexion...")
    print(ex)

# Connexion du visiteur
try:
    setValeurInput('input[name="login"]', login)
    setValeurInput('input[name="mdp"]', mdp)
    driver.find_element(By.TAG_NAME, 'form').submit()
    log("- Envoi du formulaire de connexion : OK")
except Exception as ex:
    log("- Erreur, la page de connexion est incorrecte...")
    print(ex)

# Connexion à la BDD
try:
    cnx = mysql.connector.connect(**configBdd)
    log("- Connexion à la BDD : OK")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    log("- Erreur, le login ou de mot de passe de la BDD est incorrect...")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    log("- Erreur, la BDD n'existe pas...")
  else:
    log("- Erreur : ", err)
except Exception as ex:
    print(ex)

# Création d'un curseur pour récupérer le résultat d'une requête SQL
try:
    cursor = cnx.cursor()
    log("- Création du curseur : OK")
except Exception as ex:
    log("- Erreur, problème à la création du curseur...")
    print(ex)

# Exécution de la requête SQL de récupération du code A2F
try:
    sql = """SELECT visiteur.codea2f FROM visiteur WHERE visiteur.login = %s"""
    cursor.execute(sql, (login,))
    log("- Lancement de la requête SQL de récupération du code A2F : OK")
except Exception as ex:
    log("- Erreur, problème à l'exécution de la requête SQL...")
    print(ex)

# Récupération du code A2F
try:
    code = cursor.fetchone()[0]
    log("- Récupération du code A2F : OK")
except Exception as ex:
    log("- Erreur, problème à la récupération du code A2F...")
    print(ex)

# Saisie du code A2F
try:
    setValeurInput('input[name="code"]', code)
    driver.find_element(By.TAG_NAME, 'form').submit()
    log("- Saisie du code A2F : OK")
except Exception as ex:
    log("- Erreur, la saisie du code A2F est incorrecte...")
    print(ex)

# Est-ce que ça a fonctionné ?
try:
    driver.find_element(By.CLASS_NAME, 'active')
    log("- Connexion à la page d'accueil : OK")
except Exception as ex:
    log("- Erreur, problème de connexion à la page d'accueil...")
    print(ex)