# Interconnect
Interconnect è un piccolo social network creato con il framework di Django.

Su Interconnect puoi:
* Seguire/Non seguire altri utenti
* Postare dei post
* Commentare post altrui e mettergli un 'mi piace'
* Vedere il tuo 'feed'
* Modificare il tuo profilo utente
* Creare dei gruppi con altri utenti (in questi ci sono 2 categorie: membro e moderatore)
* I moderatori dei gruppi possono rimuovere gli utenti del gruppo
* E possono eliminare anche i post di altri utenti

# Struttura del progetto
Per la creazione del progetto è stato utilizzato:
* django, per la creazione di tutta la parte di backend (directory django_prog_socialnetwork)
* nginx/HTTP, per avere un server web/proxy del sito (directory nginx)
* postgresql, per la gestione (e piccola popolazione) dei dati riguardanti il sito

# Come modificare il progetto
Il progetto è 'auto-contenuto' in docker (il file docker-compose.yml infatti contiene tutti i container necessari per lo sviluppo). 
I container dell'ambiente sono:
* web ---> contentitore dell'app effettiva
* db ---> contenitore di postgres
(NB per poter fare tutto ricorda di avere sulla macchina docker desktop)

Prima di tutto devi clonare la repo ---> git clone https://github.com/StefanoUnifi/Interconnect/

Poi devi impostare i file dell'ambiente (env):
* env
* env.dev
* env.db

env deve stare nella root del progetto (ovvero in django_prog_social_network/django_prog_socialnetwork)

Mentre env.dev e env.db fuori dalla root.
Questi 2 devi crearli per rispettivamente:
* per definire le variabili env che utilizza django
* per definire le variabili di postgres

Successivamente esegui docker e poi su shell:
  docker compose -f docker-compose.yml up -d --build 
  docker compose exec web python manage.py makemigrations
  docker compose exec web python manage.py makemigrations accounts posts groups 
  docker compose exec web python manage.py migrate

Questi comandi rispettivamente:
* avvia il container e ri-crea le immagini del progetto
* crea i file di migrazione per i modelli di django
* crea solo le migrazioni delle app necessarie
* applica le migrazioni sul database di postgres
  
