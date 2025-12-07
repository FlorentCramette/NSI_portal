from django.core.management.base import BaseCommand
from courses.models import Course, Chapter, ContentBlock


class Command(BaseCommand):
    help = 'Populate NSI Reseaux course content'

    def handle(self, *args, **kwargs):
        self.stdout.write("Creating NSI Reseaux content...")
        
        course = Course.objects.get(slug='nsi-1-reseaux')
        course.chapters.all().delete()
        
        # Chapter 1: Le Modele OSI
        chapter1 = Chapter.objects.create(
            course=course,
            title="Le Modele OSI",
            description="Comprendre les 7 couches du modele OSI",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='TEXT',
            title="Le Modele OSI",
            content_markdown="""# Le Modele OSI

Le **modele OSI** (Open Systems Interconnection) est un modele de reference pour les communications reseau. Il decoupe la communication en **7 couches**.

## Les 7 couches

| N° | Couche | Role | Exemple |
|----|--------|------|---------|
| 7 | Application | Interface utilisateur | HTTP, FTP, SMTP |
| 6 | Presentation | Format des donnees | SSL, JPEG, ASCII |
| 5 | Session | Gestion des sessions | NetBIOS, RPC |
| 4 | Transport | Livraison fiable | TCP, UDP |
| 3 | Reseau | Routage | IP, ICMP |
| 2 | Liaison | Acces au media | Ethernet, WiFi |
| 1 | Physique | Transmission bits | Cables, ondes |

## Moyen mnemotechnique

**P**our **L**e **R**eseau **T**out **S**e **P**asse **A**utrement
(Physique, Liaison, Reseau, Transport, Session, Presentation, Application)

## Encapsulation

Chaque couche ajoute un **en-tete** aux donnees :

```
Application  : [Donnees]
Transport    : [En-tete TCP][Donnees]
Reseau       : [En-tete IP][En-tete TCP][Donnees]
Liaison      : [En-tete Eth][En-tete IP][En-tete TCP][Donnees][CRC]
```

## La couche Physique (1)

Transmission des bits bruts :
- Cables (cuivre, fibre optique)
- Ondes radio (WiFi, Bluetooth)
- Signaux electriques/lumineux

## La couche Liaison (2)

Transfert de donnees entre noeuds adjacents :
- Adresses MAC (48 bits)
- Detection d'erreurs (CRC)
- Protocoles : Ethernet, WiFi

## La couche Reseau (3)

Routage des paquets :
- Adresses IP
- Determination du chemin
- Protocoles : IP, ICMP

## La couche Transport (4)

Livraison bout-en-bout :
- **TCP** : fiable, ordonne, connecte
- **UDP** : rapide, non fiable
- Ports (0-65535)""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='CODE_SAMPLE',
            title="Simulation encapsulation",
            content_markdown="""# Simulation de l'encapsulation OSI

```python
class PaquetReseau:
    # Simulation de l'encapsulation/desencapsulation
    
    def __init__(self, donnees):
        self.donnees = donnees
        self.paquet = donnees
        self.historique = []
    
    def encapsuler(self, couche, entete):
        # Ajouter un en-tete
        self.paquet = f"[{entete}]{self.paquet}"
        self.historique.append(f"Couche {couche}: +{entete}")
        print(f"Encapsulation couche {couche}: {self.paquet}")
    
    def desencapsuler(self, couche, entete):
        # Retirer un en-tete
        prefixe = f"[{entete}]"
        if self.paquet.startswith(prefixe):
            self.paquet = self.paquet[len(prefixe):]
            print(f"Desencapsulation couche {couche}: {self.paquet}")


# Simulation d'envoi HTTP
print("=== EMISSION ===")
paquet = PaquetReseau("GET /index.html")

paquet.encapsuler(7, "HTTP")
paquet.encapsuler(4, "TCP:80")
paquet.encapsuler(3, "IP:192.168.1.1->10.0.0.1")
paquet.encapsuler(2, "MAC:AA:BB:CC->DD:EE:FF")

print("\\nPaquet final:", paquet.paquet)

print("\\n=== RECEPTION ===")
paquet.desencapsuler(2, "MAC:AA:BB:CC->DD:EE:FF")
paquet.desencapsuler(3, "IP:192.168.1.1->10.0.0.1")
paquet.desencapsuler(4, "TCP:80")
paquet.desencapsuler(7, "HTTP")

print("\\nDonnees recues:", paquet.paquet)
```""",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='QUIZ',
            title="Quiz modele OSI",
            content_markdown="""### Quiz : Le Modele OSI

**Question 1** : Combien de couches comporte le modele OSI ?

- [ ] 4
- [ ] 5
- [x] 7
- [ ] 8

**Question 2** : Quelle couche gere les adresses IP ?

- [ ] Couche Transport
- [x] Couche Reseau
- [ ] Couche Liaison
- [ ] Couche Application

**Question 3** : TCP et UDP appartiennent a quelle couche ?

- [ ] Couche Application
- [x] Couche Transport
- [ ] Couche Reseau
- [ ] Couche Session""",
            order=3
        )
        
        # Chapter 2: Protocole TCP/IP
        chapter2 = Chapter.objects.create(
            course=course,
            title="Le Protocole TCP/IP",
            description="Fonctionnement de TCP et IP",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='TEXT',
            title="TCP/IP",
            content_markdown="""# Le Protocole TCP/IP

**TCP/IP** est la suite de protocoles utilisee sur Internet. C'est un modele a **4 couches**.

## Comparaison OSI / TCP/IP

| OSI | TCP/IP |
|-----|--------|
| Application, Presentation, Session | Application |
| Transport | Transport |
| Reseau | Internet |
| Liaison, Physique | Acces reseau |

## Le protocole IP

**IP** (Internet Protocol) : acheminement des paquets.

### Adresse IPv4
- 32 bits (4 octets)
- Notation : 192.168.1.100
- Environ 4 milliards d'adresses

### Adresse IPv6
- 128 bits
- Notation : 2001:0db8:85a3::8a2e:0370:7334
- Pratiquement illimite

### Structure d'une adresse IP

Une adresse IP = **adresse reseau** + **adresse hote**

Le **masque de sous-reseau** separe les deux parties :
- 255.255.255.0 = /24 (256 adresses)
- 255.255.0.0 = /16 (65536 adresses)

## Le protocole TCP

**TCP** (Transmission Control Protocol) : transport fiable.

### Caracteristiques
- **Connexion** : etablissement avant envoi (3-way handshake)
- **Fiable** : detection et retransmission des erreurs
- **Ordonne** : les paquets arrivent dans l'ordre
- **Controle de flux** : adaptation au debit

### Le 3-way handshake

```
Client          Serveur
   |     SYN       |
   |-------------->|
   |   SYN + ACK   |
   |<--------------|
   |     ACK       |
   |-------------->|
   |   Connexion   |
```

## Le protocole UDP

**UDP** (User Datagram Protocol) : transport rapide.

- Pas de connexion
- Pas de garantie de livraison
- Pas d'ordre garanti
- Utilise pour : streaming, jeux, DNS""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='CODE_SAMPLE',
            title="Calculs reseau en Python",
            content_markdown="""# Calculs reseau avec Python

```python
import ipaddress

# Manipulation d'adresses IP
print("=== Adresses IPv4 ===")

ip = ipaddress.ip_address('192.168.1.100')
print(f"Adresse: {ip}")
print(f"Version: IPv{ip.version}")
print(f"Privee: {ip.is_private}")

# Reseau avec masque
print("\\n=== Reseau /24 ===")
reseau = ipaddress.ip_network('192.168.1.0/24')
print(f"Reseau: {reseau}")
print(f"Masque: {reseau.netmask}")
print(f"Premiere adresse: {reseau.network_address}")
print(f"Derniere adresse: {reseau.broadcast_address}")
print(f"Nombre d'hotes: {reseau.num_addresses - 2}")

# Verifier si une IP est dans le reseau
ip_test = ipaddress.ip_address('192.168.1.50')
print(f"{ip_test} dans {reseau}? {ip_test in reseau}")

# Sous-reseaux
print("\\n=== Sous-reseaux ===")
reseau_large = ipaddress.ip_network('10.0.0.0/8')
sous_reseaux = list(reseau_large.subnets(new_prefix=16))[:4]
for sr in sous_reseaux:
    print(f"  {sr}")

# Calcul d'adresse reseau
def calculer_adresse_reseau(ip, masque):
    ip_octets = [int(x) for x in ip.split('.')]
    masque_octets = [int(x) for x in masque.split('.')]
    reseau = [ip_octets[i] & masque_octets[i] for i in range(4)]
    return '.'.join(map(str, reseau))

print("\\n=== Calcul manuel ===")
ip = "192.168.1.100"
masque = "255.255.255.0"
print(f"IP: {ip}, Masque: {masque}")
print(f"Adresse reseau: {calculer_adresse_reseau(ip, masque)}")
```""",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='QUIZ',
            title="Quiz TCP/IP",
            content_markdown="""### Quiz : TCP/IP

**Question 1** : Combien de bits une adresse IPv4 ?

- [ ] 64 bits
- [x] 32 bits
- [ ] 128 bits
- [ ] 16 bits

**Question 2** : Quelle est la caracteristique principale de TCP ?

- [ ] Rapide mais non fiable
- [x] Fiable avec controle d'erreurs
- [ ] Sans connexion
- [ ] Reserve au streaming

**Question 3** : Que signifie le masque /24 ?

- [ ] 24 adresses disponibles
- [x] 24 bits pour le reseau, 8 pour l'hote
- [ ] 24 sous-reseaux
- [ ] 24 ports ouverts""",
            order=3
        )
        
        # Chapter 3: Routage
        chapter3 = Chapter.objects.create(
            course=course,
            title="Le Routage",
            description="Comment les paquets trouvent leur chemin",
            order=3
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='TEXT',
            title="Le Routage",
            content_markdown="""# Le Routage

Le **routage** permet aux paquets de trouver leur chemin a travers le reseau.

## Principe de base

Les **routeurs** interconnectent les reseaux et font suivre les paquets.

Chaque routeur maintient une **table de routage** :
- Destination : adresse reseau cible
- Passerelle : prochain routeur
- Interface : sortie a utiliser
- Metrique : cout du chemin

## Types de routage

### Routage statique
- Routes configurees manuellement
- Simple mais pas adaptable
- Pour petits reseaux stables

### Routage dynamique
- Routes apprises automatiquement
- Protocoles : RIP, OSPF, BGP
- S'adapte aux changements

## Algorithmes de routage

### Vecteur de distance (RIP)
- Chaque routeur partage sa table
- Choix par nombre de sauts
- Simple mais lent a converger

### Etat de liens (OSPF)
- Chaque routeur connait la topologie
- Calcul du plus court chemin (Dijkstra)
- Plus efficace, convergence rapide

## Table de routage exemple

```
Destination      Passerelle       Interface    Metrique
192.168.1.0/24   0.0.0.0          eth0         0
10.0.0.0/8       192.168.1.1      eth0         1
0.0.0.0/0        192.168.1.254    eth0         1
```

La derniere ligne (0.0.0.0/0) est la **route par defaut** (gateway).

## Processus de routage

1. Paquet arrive sur une interface
2. Lecture de l'adresse IP destination
3. Consultation de la table de routage
4. Selection de la meilleure route
5. Envoi sur l'interface correspondante
6. Decrementation du TTL""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='CODE_SAMPLE',
            title="Simulation de routage",
            content_markdown="""# Simulation de routage

```python
class Routeur:
    def __init__(self, nom):
        self.nom = nom
        self.table = []  # (reseau, masque, passerelle, interface, metrique)
    
    def ajouter_route(self, reseau, masque, passerelle, interface, metrique=1):
        self.table.append((reseau, masque, passerelle, interface, metrique))
    
    def ip_en_entier(self, ip):
        octets = [int(x) for x in ip.split('.')]
        return (octets[0] << 24) + (octets[1] << 16) + (octets[2] << 8) + octets[3]
    
    def correspond(self, ip, reseau, masque):
        ip_int = self.ip_en_entier(ip)
        reseau_int = self.ip_en_entier(reseau)
        masque_int = self.ip_en_entier(masque)
        return (ip_int & masque_int) == (reseau_int & masque_int)
    
    def router(self, ip_destination):
        print(f"[{self.nom}] Routage de {ip_destination}")
        
        meilleures = []
        for reseau, masque, passerelle, interface, metrique in self.table:
            if self.correspond(ip_destination, reseau, masque):
                prefixe = bin(self.ip_en_entier(masque)).count('1')
                meilleures.append((prefixe, metrique, passerelle, interface))
        
        if not meilleures:
            print("  -> Pas de route!")
            return None
        
        # Longest prefix match + plus petite metrique
        meilleures.sort(key=lambda x: (-x[0], x[1]))
        _, _, passerelle, interface = meilleures[0]
        
        print(f"  -> Interface: {interface}, Passerelle: {passerelle}")
        return (interface, passerelle)


# Creer un routeur
r1 = Routeur("R1")
r1.ajouter_route("192.168.1.0", "255.255.255.0", "0.0.0.0", "eth0", 0)
r1.ajouter_route("10.0.0.0", "255.0.0.0", "192.168.1.1", "eth0", 1)
r1.ajouter_route("172.16.0.0", "255.255.0.0", "192.168.1.2", "eth1", 2)
r1.ajouter_route("0.0.0.0", "0.0.0.0", "192.168.1.254", "eth0", 10)

# Tests
r1.router("192.168.1.50")  # Reseau local
r1.router("10.5.3.2")       # Via passerelle
r1.router("8.8.8.8")        # Route par defaut
```""",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='QUIZ',
            title="Quiz routage",
            content_markdown="""### Quiz : Le Routage

**Question 1** : Quel est le role d'un routeur ?

- [ ] Amplifier le signal
- [x] Interconnecter les reseaux et acheminer les paquets
- [ ] Filtrer les virus
- [ ] Stocker les donnees

**Question 2** : Qu'est-ce que la route par defaut (0.0.0.0/0) ?

- [ ] Une route interdite
- [ ] La route la plus rapide
- [x] La route utilisee quand aucune autre ne correspond
- [ ] Une route vers localhost

**Question 3** : Quel algorithme utilise OSPF pour calculer les routes ?

- [ ] Vecteur de distance
- [x] Dijkstra (plus court chemin)
- [ ] Round-robin
- [ ] Aleatoire""",
            order=3
        )
        
        self.stdout.write(self.style.SUCCESS('Created 3 chapters with 9 blocks for NSI Reseaux'))
