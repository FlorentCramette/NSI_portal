from django.core.management.base import BaseCommand
from courses.models import Course, Chapter, ContentBlock


class Command(BaseCommand):
    help = 'Populate NSI Architecture Materielle course content'

    def handle(self, *args, **kwargs):
        self.stdout.write("Creating NSI Architecture Materielle content...")
        
        course = Course.objects.get(slug='nsi-1-architecture')
        course.chapters.all().delete()
        
        # Chapter 1: Le Processeur (CPU)
        chapter1 = Chapter.objects.create(
            course=course,
            title="Le Processeur (CPU)",
            description="Composants et fonctionnement du processeur",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='TEXT',
            title="Le Processeur",
            content_markdown="""# Le Processeur (CPU)

Le **processeur** (CPU - Central Processing Unit) est le "cerveau" de l'ordinateur. Il execute les instructions des programmes.

## Composants principaux

### 1. L'Unite Arithmetique et Logique (UAL)
L'UAL effectue les operations :
- **Arithmetiques** : addition, soustraction, multiplication, division
- **Logiques** : ET, OU, NON, comparaisons

### 2. L'Unite de Controle (UC)
L'UC coordonne les operations :
- Lit les instructions en memoire
- Decode les instructions
- Pilote l'execution

### 3. Les Registres
Memoires ultra-rapides integrees au processeur :
- **Compteur de programme (PC)** : adresse de la prochaine instruction
- **Registre d'instruction (RI)** : instruction en cours
- **Accumulateur** : resultats des calculs
- **Registres generaux** : donnees temporaires

## Le cycle d'execution

Le processeur fonctionne en cycles repetitifs :

1. **FETCH** (Lecture) : Recuperer l'instruction en memoire
2. **DECODE** (Decodage) : Analyser l'instruction
3. **EXECUTE** (Execution) : Effectuer l'operation
4. **WRITEBACK** : Stocker le resultat

## Frequence et performances

- **Frequence** : nombre de cycles par seconde (en Hz)
- Un processeur a 3 GHz fait 3 milliards de cycles par seconde
- Plus la frequence est elevee, plus le processeur est rapide

## Architecture multi-coeurs

Les processeurs modernes ont plusieurs **coeurs** :
- Chaque coeur peut executer des instructions
- 4 coeurs = 4 taches en parallele
- Ameliore les performances pour les applications paralleles""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='CODE_SAMPLE',
            title="Simulation d'un processeur",
            content_markdown="""# Simulation d'un processeur simple en Python

```python
class ProcesseurSimple:
    # Simulation pedagogique d'un CPU
    
    def __init__(self):
        # Registres
        self.PC = 0  # Compteur de programme
        self.ACC = 0  # Accumulateur
        self.registres = [0] * 4  # 4 registres generaux
        
        # Memoire (256 mots)
        self.memoire = [0] * 256
        
        # Etat
        self.running = True
    
    def charger_programme(self, programme):
        # Charge un programme en memoire
        for i, instruction in enumerate(programme):
            self.memoire[i] = instruction
        self.PC = 0
    
    def fetch(self):
        # Lecture de l'instruction
        instruction = self.memoire[self.PC]
        self.PC += 1
        return instruction
    
    def decode_execute(self, instruction):
        # Decodage et execution
        opcode = instruction.split()[0]
        args = instruction.split()[1:] if len(instruction.split()) > 1 else []
        
        if opcode == "LOAD":
            self.ACC = int(args[0])
            print(f"LOAD {args[0]} -> ACC = {self.ACC}")
            
        elif opcode == "ADD":
            self.ACC += int(args[0])
            print(f"ADD {args[0]} -> ACC = {self.ACC}")
            
        elif opcode == "SUB":
            self.ACC -= int(args[0])
            print(f"SUB {args[0]} -> ACC = {self.ACC}")
            
        elif opcode == "HALT":
            self.running = False
            print("HALT - Programme termine")
    
    def run(self):
        print("=== Debut de l'execution ===")
        while self.running and self.PC < 256:
            instruction = self.fetch()
            if instruction == 0:
                break
            self.decode_execute(instruction)
        print(f"Resultat: ACC = {self.ACC}")


# Exemple : calculer 10 + 25 - 5
cpu = ProcesseurSimple()
programme = ["LOAD 10", "ADD 25", "SUB 5", "HALT"]
cpu.charger_programme(programme)
cpu.run()
```""",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='QUIZ',
            title="Quiz sur le processeur",
            content_markdown="""### Quiz : Le Processeur

**Question 1** : Que signifie CPU ?

- [ ] Computer Power Unit
- [x] Central Processing Unit
- [ ] Core Performance Utility
- [ ] Central Program Unit

**Question 2** : Quel composant effectue les operations arithmetiques ?

- [x] L'UAL (Unite Arithmetique et Logique)
- [ ] L'Unite de Controle
- [ ] Le compteur de programme
- [ ] La memoire cache

**Question 3** : Dans le cycle d'execution, que fait l'etape FETCH ?

- [ ] Decoder l'instruction
- [x] Recuperer l'instruction en memoire
- [ ] Executer l'instruction
- [ ] Stocker le resultat""",
            order=3
        )
        
        # Chapter 2: La Memoire
        chapter2 = Chapter.objects.create(
            course=course,
            title="La Memoire",
            description="Types de memoire et hierarchie",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='TEXT',
            title="Les types de memoire",
            content_markdown="""# La Memoire

La memoire stocke les donnees et les programmes. Il existe differents types de memoire, organises en **hierarchie**.

## Hierarchie de la memoire

Du plus rapide au plus lent :

| Niveau | Type | Taille | Vitesse | Persistance |
|--------|------|--------|---------|-------------|
| 1 | Registres | ~100 octets | ~1 ns | Non |
| 2 | Cache L1 | ~64 Ko | ~2 ns | Non |
| 3 | Cache L2/L3 | ~8 Mo | ~10 ns | Non |
| 4 | RAM | ~16 Go | ~100 ns | Non |
| 5 | SSD | ~500 Go | ~100 us | Oui |
| 6 | HDD | ~2 To | ~10 ms | Oui |

## La memoire vive (RAM)

**RAM** = Random Access Memory

### Caracteristiques
- Acces direct a n'importe quelle adresse
- **Volatile** : donnees perdues a l'extinction
- Stocke programmes et donnees en cours d'utilisation

### Types de RAM
- **DRAM** : memoire principale, doit etre rafraichie
- **SRAM** : plus rapide, utilisee pour le cache

## La memoire cache

Memoire tres rapide entre le CPU et la RAM :

- **Cache L1** : integre au coeur, tres petit mais ultra-rapide
- **Cache L2** : plus grand, legerement plus lent
- **Cache L3** : partage entre les coeurs

### Principe de localite
Le cache exploite deux principes :
- **Localite temporelle** : donnees recemment utilisees seront reutilisees
- **Localite spatiale** : donnees proches seront utilisees ensemble

## Adressage memoire

Chaque octet en memoire a une **adresse** unique :
- Adresse sur 32 bits : 2^32 = 4 Go maximum
- Adresse sur 64 bits : 2^64 = 16 Eo (exaoctets)""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='CODE_SAMPLE',
            title="Exploration memoire en Python",
            content_markdown="""# Exploration de la memoire en Python

```python
import sys

# Taille des objets en memoire
print("=== Taille des objets Python ===")

entier = 42
flottant = 3.14
chaine = "Hello World"
liste = [1, 2, 3, 4, 5]

print(f"int (42): {sys.getsizeof(entier)} octets")
print(f"float (3.14): {sys.getsizeof(flottant)} octets")
print(f"str: {sys.getsizeof(chaine)} octets")
print(f"list: {sys.getsizeof(liste)} octets")

# Adresses memoire avec id()
print("\\n=== Adresses memoire ===")
a = 100
b = 100
print(f"a = 100, adresse: {id(a)}")
print(f"b = 100, adresse: {id(b)}")
print(f"Meme adresse? {id(a) == id(b)}")  # Vrai pour petits entiers

# Simulation de cache LRU
class CacheSimple:
    def __init__(self, taille_max):
        self.taille_max = taille_max
        self.cache = {}
        self.ordre = []
        self.hits = 0
        self.misses = 0
    
    def get(self, cle):
        if cle in self.cache:
            self.hits += 1
            self.ordre.remove(cle)
            self.ordre.append(cle)
            return self.cache[cle]
        else:
            self.misses += 1
            return None
    
    def set(self, cle, valeur):
        if len(self.cache) >= self.taille_max and cle not in self.cache:
            oldest = self.ordre.pop(0)
            del self.cache[oldest]
        self.cache[cle] = valeur
        if cle in self.ordre:
            self.ordre.remove(cle)
        self.ordre.append(cle)

cache = CacheSimple(3)
for cle in ['A', 'B', 'C', 'A', 'D', 'B', 'A']:
    if cache.get(cle) is None:
        cache.set(cle, f"data_{cle}")
print(f"\\nHits: {cache.hits}, Misses: {cache.misses}")
```""",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='QUIZ',
            title="Quiz sur la memoire",
            content_markdown="""### Quiz : La Memoire

**Question 1** : Quelle memoire est la plus rapide ?

- [x] Les registres du processeur
- [ ] La RAM
- [ ] Le cache L3
- [ ] Le SSD

**Question 2** : La RAM est une memoire volatile, cela signifie :

- [ ] Elle est tres rapide
- [x] Les donnees sont perdues a l'extinction
- [ ] Elle est tres grande
- [ ] Elle consomme peu d'energie

**Question 3** : Quel est le role de la memoire cache ?

- [ ] Stocker les fichiers definitivement
- [x] Accelerer l'acces aux donnees frequemment utilisees
- [ ] Remplacer la RAM
- [ ] Executer les programmes""",
            order=3
        )
        
        # Chapter 3: Architecture Von Neumann
        chapter3 = Chapter.objects.create(
            course=course,
            title="Architecture de Von Neumann",
            description="Le modele fondamental des ordinateurs modernes",
            order=3
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='TEXT',
            title="L'architecture Von Neumann",
            content_markdown="""# Architecture de Von Neumann

L'**architecture de Von Neumann** est le modele fondamental des ordinateurs modernes, propose par John von Neumann en 1945.

## Principe fondamental

**Programme stocke** : les instructions et les donnees sont stockees dans la meme memoire.

Avant Von Neumann, les "calculateurs" devaient etre recables pour chaque nouveau programme !

## Les 4 composants principaux

### 1. L'Unite Centrale de Traitement (CPU)
- Execute les instructions
- Contient l'UAL et l'Unite de Controle

### 2. La Memoire
- Stocke instructions ET donnees
- Acces par adresse

### 3. Les Entrees/Sorties
- Communication avec l'exterieur
- Peripheriques divers

### 4. Le Bus
- Connexions entre les composants
- Bus de donnees, d'adresses et de controle

## Schema simplifie

```
    +---------+
    |   CPU   |
    +---------+
         |
    +----+----+
    |   BUS   |
    +----+----+
         |
    +---------+     +---------+
    | MEMOIRE | --- |  E/S    |
    +---------+     +---------+
```

## Le goulot d'etranglement

Le **goulot de Von Neumann** : le bus unique entre CPU et memoire limite les performances.

Solutions modernes :
- Memoire cache
- Bus separes pour instructions et donnees (Harvard modifie)
- Prefetching (prelecture)

## Architecture Harvard

Alternative a Von Neumann :
- Memoires separees pour instructions et donnees
- Deux bus distincts
- Plus rapide mais moins flexible
- Utilisee dans les microcontroleurs""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='CODE_SAMPLE',
            title="Simulation Von Neumann",
            content_markdown="""# Simulation d'un ordinateur Von Neumann

```python
class OrdinateurVonNeumann:
    # Jeu d'instructions
    OPCODES = {
        0x01: "LOAD_IMM",  # Charger valeur immediate
        0x02: "LOAD_MEM",  # Charger depuis memoire
        0x03: "STORE",     # Stocker en memoire
        0x04: "ADD",       # Addition
        0x05: "SUB",       # Soustraction
        0x0C: "PRINT",     # Afficher
        0xFF: "HALT"       # Arreter
    }
    
    def __init__(self, taille_memoire=256):
        # Memoire unifiee (Von Neumann)
        self.memoire = [0] * taille_memoire
        self.PC = 0      # Program Counter
        self.ACC = 0     # Accumulateur
        self.running = False
    
    def charger(self, programme, adresse=0):
        for i, val in enumerate(programme):
            self.memoire[adresse + i] = val
    
    def fetch(self):
        instruction = self.memoire[self.PC]
        self.PC += 1
        return instruction
    
    def execute(self, opcode):
        if opcode == 0x01:  # LOAD_IMM
            self.ACC = self.fetch()
            print(f"LOAD {self.ACC}")
        elif opcode == 0x02:  # LOAD_MEM
            addr = self.fetch()
            self.ACC = self.memoire[addr]
            print(f"LOAD [{addr}] = {self.ACC}")
        elif opcode == 0x03:  # STORE
            addr = self.fetch()
            self.memoire[addr] = self.ACC
            print(f"STORE [{addr}] = {self.ACC}")
        elif opcode == 0x04:  # ADD
            addr = self.fetch()
            self.ACC += self.memoire[addr]
            print(f"ADD -> {self.ACC}")
        elif opcode == 0x0C:  # PRINT
            print(f"OUTPUT: {self.ACC}")
        elif opcode == 0xFF:  # HALT
            self.running = False
            print("HALT")
    
    def run(self, debut=0):
        self.PC = debut
        self.running = True
        while self.running:
            self.execute(self.fetch())

# Demo : additionner 25 + 17
ordi = OrdinateurVonNeumann()
# Programme a l'adresse 0, donnees a 100
ordi.charger([0x02, 100, 0x04, 101, 0x0C, 0xFF])
ordi.charger([25, 17], 100)
ordi.run()  # Output: 42
```""",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='QUIZ',
            title="Quiz Von Neumann",
            content_markdown="""### Quiz : Architecture de Von Neumann

**Question 1** : Quel est le principe fondamental de l'architecture Von Neumann ?

- [ ] Utiliser plusieurs processeurs
- [x] Stocker programmes et donnees dans la meme memoire
- [ ] Separer memoire d'instructions et de donnees
- [ ] Utiliser uniquement de la memoire cache

**Question 2** : Qu'est-ce que le "goulot de Von Neumann" ?

- [ ] Un probleme de refroidissement
- [ ] Un manque de memoire
- [x] La limitation du bus unique entre CPU et memoire
- [ ] Un bug dans les programmes

**Question 3** : Quelle est la difference avec l'architecture Harvard ?

- [ ] Harvard n'a pas de memoire
- [x] Harvard separe memoire d'instructions et de donnees
- [ ] Harvard n'a pas de CPU
- [ ] Harvard est plus lente""",
            order=3
        )
        
        self.stdout.write(self.style.SUCCESS('Created 3 chapters with 9 blocks for NSI Architecture Materielle'))
