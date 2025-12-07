from django.core.management.base import BaseCommand
from courses.models import Course, Chapter, ContentBlock


class Command(BaseCommand):
    help = 'Populate NSI 1ère Représentation des Données course'

    def handle(self, *args, **options):
        self.stdout.write('Creating NSI Représentation des Données content...')
        
        try:
            course = Course.objects.get(slug='nsi-1-representation-donnees')
        except Course.DoesNotExist:
            self.stdout.write(self.style.ERROR('Course not found'))
            return
        
        course.chapters.all().delete()
        
        # Chapter 1: Binaire et hexadécimal
        chapter1 = Chapter.objects.create(
            course=course,
            title="Systèmes de numération",
            description="Binaire, décimal, hexadécimal",
            order=1,
            is_published=True
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='TEXT',
            title="Les systèmes de numération",
            content_markdown="""## Pourquoi différents systèmes?

Les ordinateurs utilisent l'**électricité** : courant ou pas courant, 1 ou 0.
- **Binaire (base 2)**: Le langage des machines
- **Décimal (base 10)**: Notre système quotidien
- **Hexadécimal (base 16)**: Notation compacte pour les humains

## Le système binaire

### Principe
Seulement **2 chiffres**: 0 et 1 (appelés **bits**)

### Compter en binaire

| Décimal | Binaire | Explication |
|---------|---------|-------------|
| 0 | 0000 | Zéro |
| 1 | 0001 | Un |
| 2 | 0010 | Deux |
| 3 | 0011 | Trois |
| 4 | 0100 | Quatre |
| 5 | 0101 | Cinq |
| 10 | 1010 | Dix |
| 15 | 1111 | Quinze |
| 255 | 11111111 | Maximum sur 8 bits |

### Conversion binaire → décimal

Chaque position représente une puissance de 2:

```
1011₂ = ?₁₀

Position:  3    2    1    0
Bit:       1    0    1    1
Poids:     2³   2²   2¹   2⁰
Valeur:    8    0    2    1

Total: 8 + 0 + 2 + 1 = 11₁₀
```

### Conversion décimal → binaire

**Méthode des divisions successives:**

```
Convertir 25₁₀ en binaire:

25 ÷ 2 = 12 reste 1  ← bit de poids faible
12 ÷ 2 = 6  reste 0
6  ÷ 2 = 3  reste 0
3  ÷ 2 = 1  reste 1
1  ÷ 2 = 0  reste 1  ← bit de poids fort

Lire de bas en haut: 11001₂
```

## Le système hexadécimal

### Principe
**16 chiffres**: 0-9 puis A-F

| Hex | Décimal | Binaire |
|-----|---------|---------|
| 0 | 0 | 0000 |
| 1 | 1 | 0001 |
| ... | ... | ... |
| 9 | 9 | 1001 |
| A | 10 | 1010 |
| B | 11 | 1011 |
| C | 12 | 1100 |
| D | 13 | 1101 |
| E | 14 | 1110 |
| F | 15 | 1111 |

### Pourquoi l'hexadécimal?

Un chiffre hex = **4 bits** → Plus compact!

**Exemple:**
- Binaire: `11111111`
- Hexadécimal: `FF`

### Conversion hex ↔ binaire

**Hex → Binaire:** Remplacer chaque chiffre par 4 bits

```
2A3₁₆ = ?₂

2    A    3
0010 1010 0011

Résultat: 001010100011₂
```

**Binaire → Hex:** Grouper par 4 bits

```
10110111₂ = ?₁₆

1011 0111
B    7

Résultat: B7₁₆
```

## Notation

- Binaire: `0b1010` ou `1010₂`
- Hexadécimal: `0x2A` ou `2A₁₆`
- Décimal: `42` ou `42₁₀`

## Unités de mesure

| Unité | Valeur | Utilisation |
|-------|--------|-------------|
| bit (b) | 0 ou 1 | Plus petite unité |
| octet (byte, B) | 8 bits | Caractère, pixel |
| kilo-octet (Ko) | 1024 octets | Petit fichier texte |
| méga-octet (Mo) | 1024 Ko | Photo, chanson |
| giga-octet (Go) | 1024 Mo | Film, jeu |
| téra-octet (To) | 1024 Go | Disque dur |

⚠️ **Attention:** 1 Ko = 1024 octets (pas 1000!)""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='CODE_SAMPLE',
            title="Pratique: Conversions",
            content_markdown="""# Conversions entre bases

# Décimal vers binaire
def decimal_vers_binaire(n):
    if n == 0:
        return "0"
    binaire = ""
    while n > 0:
        binaire = str(n % 2) + binaire
        n = n // 2
    return binaire

# Binaire vers décimal
def binaire_vers_decimal(binaire):
    decimal = 0
    puissance = 0
    for bit in reversed(binaire):
        if bit == '1':
            decimal += 2 ** puissance
        puissance += 1
    return decimal

# Décimal vers hexadécimal
def decimal_vers_hex(n):
    if n == 0:
        return "0"
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    while n > 0:
        hexadecimal = hex_chars[n % 16] + hexadecimal
        n = n // 16
    return hexadecimal

# Hexadécimal vers décimal
def hex_vers_decimal(hexa):
    return int(hexa, 16)

# Tests
print("=== CONVERSIONS ===\n")

# Exemples décimal → binaire
for n in [5, 42, 255]:
    bin_manuel = decimal_vers_binaire(n)
    bin_python = bin(n)[2:]  # Enlever le préfixe '0b'
    print(f"{n:3}₁₀ = {bin_manuel:8} (manuel) = {bin_python:8} (Python)")

print()

# Exemples binaire → décimal
binaires = ["1010", "11111111", "10101010"]
for b in binaires:
    dec_manuel = binaire_vers_decimal(b)
    dec_python = int(b, 2)
    print(f"{b:8}₂ = {dec_manuel:3}₁₀ (manuel) = {dec_python:3}₁₀ (Python)")

print()

# Exemples décimal → hexadécimal
for n in [16, 255, 4095]:
    hex_manuel = decimal_vers_hex(n)
    hex_python = hex(n)[2:].upper()
    print(f"{n:4}₁₀ = {hex_manuel:4}₁₆ (manuel) = {hex_python:4}₁₆ (Python)")

print()

# Conversions avec Python
nombre = 42
print(f"=== CONVERSIONS DE {nombre} ===")
print(f"Décimal:      {nombre}")
print(f"Binaire:      {bin(nombre)}")
print(f"Hexadécimal:  {hex(nombre)}")
print(f"Octal:        {oct(nombre)}")

print("\n=== OPÉRATIONS BINAIRES ===")
a = 0b1010  # 10 en décimal
b = 0b1100  # 12 en décimal

print(f"a = {a} = {bin(a)}")
print(f"b = {b} = {bin(b)}")
print(f"a AND b = {a & b} = {bin(a & b)}")
print(f"a OR  b = {a | b} = {bin(a | b)}")
print(f"a XOR b = {a ^ b} = {bin(a ^ b)}")
print(f"NOT a   = {~a}")
print(f"a << 2  = {a << 2} = {bin(a << 2)} (décalage gauche)")
print(f"a >> 1  = {a >> 1} = {bin(a >> 1)} (décalage droite)")

# Table de multiplication binaire
print("\n=== TABLE BINAIRE (0-15) ===")
print("Déc | Bin    | Hex")
print("----|--------|----")
for i in range(16):
    print(f"{i:3} | {bin(i)[2:]:>6} | {hex(i)[2:].upper():>2}")

# Unités de stockage
print("\n=== UNITÉS DE STOCKAGE ===")
octets = 1
for unite in ["octet", "Ko", "Mo", "Go", "To"]:
    bits = octets * 8
    print(f"1 {unite:6} = {octets:20,} octets = {bits:20,} bits")
    octets *= 1024""",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='EXERCISE',
            title="Exercice: Convertisseur multi-bases",
            content_markdown="""Crée un **convertisseur universel** entre binaire, décimal et hexadécimal.

**Fonctionnalités:**
1. Détecte automatiquement la base d'entrée
2. Convertit vers les deux autres bases
3. Affiche en format lisible

**Structure:**
```python
def detecter_base(nombre_str):
    # Retourne 2 (binaire), 10 (decimal), ou 16 (hex)
    if nombre_str.startswith('0b'):
        return 2
    elif nombre_str.startswith('0x'):
        return 16
    elif all(c in '01' for c in nombre_str):
        return 2
    elif all(c in '0123456789ABCDEF' for c in nombre_str.upper()):
        return 16
    else:
        return 10

def convertir_multi_bases(nombre_str):
    base = detecter_base(nombre_str)
    
    # Convertir en décimal d'abord
    if base == 2:
        decimal = int(nombre_str.replace('0b', ''), 2)
    elif base == 16:
        decimal = int(nombre_str.replace('0x', ''), 16)
    else:
        decimal = int(nombre_str)
    
    # Afficher toutes les bases
    print(f"Nombre saisi: {nombre_str} (base {base})")
    print(f"  Décimal:      {decimal}")
    print(f"  Binaire:      {bin(decimal)}")
    print(f"  Hexadécimal:  {hex(decimal)}")
    print(f"  Octets:       {decimal // 8} octets + {decimal % 8} bits")

# Tests
convertir_multi_bases("0b1010")
convertir_multi_bases("42")
convertir_multi_bases("0xFF")
```

**Bonus:** Ajoute la conversion en base 64 et en octal (base 8)!""",
            order=3
        )
        
        ContentBlock.objects.create(
            chapter=chapter1,
            type='QUIZ',
            title="Quiz: Systèmes de numération",
            content_markdown="""**Question 1:** Combien vaut 1011₂ en décimal?
- a) 9
- b) 11 ✓
- c) 13
- d) 15

**Question 2:** Combien de bits dans un octet?
- a) 4
- b) 8 ✓
- c) 16
- d) 32

**Question 3:** Que vaut F en hexadécimal?
- a) 10
- b) 12
- c) 14
- d) 15 ✓

**Question 4:** Combien d'octets dans 1 Ko?
- a) 1000
- b) 1024 ✓
- c) 10000
- d) 8192""",
            order=4
        )
        
        # Chapter 2: Encodage des caractères
        chapter2 = Chapter.objects.create(
            course=course,
            title="Encodage des caractères",
            description="ASCII, Unicode, UTF-8",
            order=2,
            is_published=True
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='TEXT',
            title="Comment encoder du texte?",
            content_markdown="""## Le problème

Les ordinateurs ne comprennent que les **nombres binaires**.
Comment représenter du texte?

**Solution:** Une **table de correspondance** entre caractères et nombres.

## ASCII (American Standard Code for Information Interchange)

### Historique
- Créé en 1963
- **7 bits** = 128 caractères possibles
- Conçu pour l'anglais

### Table ASCII (extrait)

| Décimal | Hex | Binaire | Caractère |
|---------|-----|---------|-----------|
| 32 | 20 | 0100000 | (espace) |
| 48 | 30 | 0110000 | 0 |
| 49 | 31 | 0110001 | 1 |
| 65 | 41 | 1000001 | A |
| 66 | 42 | 1000010 | B |
| 97 | 61 | 1100001 | a |
| 98 | 62 | 1100010 | b |

### Catégories
- **0-31**: Caractères de contrôle (retour ligne, tab, etc.)
- **32-47**: Symboles et espace
- **48-57**: Chiffres 0-9
- **65-90**: Lettres majuscules A-Z
- **97-122**: Lettres minuscules a-z
- **123-127**: Symboles

### Limites d'ASCII
❌ Pas d'accents: é, à, ç
❌ Pas d'autres alphabets: 中, العربية, Русский
❌ Pas d'emojis: 😀, 🚀

## Unicode

### Principe
**Un code unique** pour **chaque caractère** dans toutes les langues du monde!

### Caractéristiques
- **1,1 million** de codes possibles
- Notation: `U+0041` pour 'A'
- Couvre toutes les langues vivantes et mortes
- Inclut les emojis, symboles mathématiques, etc.

### Exemples

| Caractère | Code Unicode | Description |
|-----------|--------------|-------------|
| A | U+0041 | Lettre A |
| é | U+00E9 | e accent aigu |
| € | U+20AC | Symbole euro |
| 中 | U+4E2D | Caractère chinois |
| 😀 | U+1F600 | Emoji sourire |
| 🚀 | U+1F680 | Fusée |

## UTF-8 (Unicode Transformation Format - 8 bits)

### Le problème
Unicode définit les codes, mais comment les **stocker** en binaire?

### Principe UTF-8
Encodage **variable**: 1 à 4 octets selon le caractère

### Règles d'encodage

| Plage Unicode | Octets | Format |
|---------------|--------|--------|
| U+0000 à U+007F | 1 | 0xxxxxxx |
| U+0080 à U+07FF | 2 | 110xxxxx 10xxxxxx |
| U+0800 à U+FFFF | 3 | 1110xxxx 10xxxxxx 10xxxxxx |
| U+10000 à U+10FFFF | 4 | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx |

### Exemples d'encodage

**Lettre 'A' (U+0041):**
- 1 octet: `01000001` (65 en décimal)
- Compatible ASCII! ✅

**Lettre 'é' (U+00E9 = 233):**
- 2 octets: `11000011 10101001` (C3 A9 en hex)

**Emoji '😀' (U+1F600):**
- 4 octets: `11110000 10011111 10011000 10000000` (F0 9F 98 80)

### Avantages UTF-8
✅ Compatible ASCII (1 octet pour caractères courants)
✅ Économique pour textes latins
✅ Support universel
✅ Standard du web (90% des sites)

## Comparaison

| Encodage | Octets/car | Langues | Utilisation |
|----------|------------|---------|-------------|
| ASCII | 1 | Anglais | Obsolète |
| Latin-1 | 1 | Européennes | Rare |
| UTF-8 | 1-4 | Toutes | Web, Linux ✓ |
| UTF-16 | 2-4 | Toutes | Windows, Java |
| UTF-32 | 4 | Toutes | Rare |""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='CODE_SAMPLE',
            title="Pratique: Encodage de caractères",
            content_markdown="""# Encodage et décodage en Python

# ASCII
print("=== ASCII ===")
lettre = 'A'
code_ascii = ord(lettre)  # Caractère → code
print(f"'{lettre}' a le code ASCII {code_ascii}")
print(f"En binaire: {bin(code_ascii)}")
print(f"En hexadécimal: {hex(code_ascii)}")

# Inverse: code → caractère
print(f"Le code 65 donne: '{chr(65)}'")

# Table ASCII partielle
print("\n=== TABLE ASCII (A-Z) ===")
print("Car | Déc | Hex | Bin")
print("----|-----|-----|--------")
for i in range(65, 91):  # A à Z
    car = chr(i)
    print(f" {car}  | {i:3} | {hex(i):>4} | {bin(i):>10}")

# Unicode
print("\n=== UNICODE ===")
caracteres = ['A', 'é', '€', '中', '😀', '🚀']
for car in caracteres:
    code = ord(car)
    print(f"'{car}' → U+{code:04X} → {code}")

# UTF-8 encoding
print("\n=== ENCODAGE UTF-8 ===")
texte = "Café €20 😀"
print(f"Texte: {texte}")

# Encoder en UTF-8
utf8_bytes = texte.encode('utf-8')
print(f"UTF-8: {utf8_bytes}")
print(f"Nombre d'octets: {len(utf8_bytes)}")

# Afficher octet par octet
print("\nDétail octet par octet:")
for car in texte:
    utf8 = car.encode('utf-8')
    hex_str = ' '.join(f'{b:02X}' for b in utf8)
    print(f"'{car}' → {len(utf8)} octet(s): {hex_str}")

# Comparaison ASCII vs UTF-8
print("\n=== COMPARAISON TAILLE ===")
textes = [
    "Hello",           # Anglais
    "Bonjour",         # Français
    "Привет",          # Russe
    "こんにちは",       # Japonais
    "Hello 😀"         # Avec emoji
]

for texte in textes:
    ascii_ok = all(ord(c) < 128 for c in texte)
    utf8_bytes = len(texte.encode('utf-8'))
    utf16_bytes = len(texte.encode('utf-16-le'))
    
    print(f"{texte:15} | UTF-8: {utf8_bytes:2} octets | "
          f"UTF-16: {utf16_bytes:2} octets | "
          f"ASCII: {'✓' if ascii_ok else '✗'}")

# Problèmes d'encodage
print("\n=== PROBLÈMES D'ENCODAGE ===")

# Texte avec accents
texte_fr = "L'été en forêt, c'est génial! 🌲"

# Bon encodage
print("Bon encodage (UTF-8):")
print(texte_fr)

# Mauvais décodage (simulé)
try:
    utf8_bytes = texte_fr.encode('utf-8')
    mauvais = utf8_bytes.decode('latin-1')  # Mauvais décodage
    print(f"\nMauvais décodage (latin-1): {mauvais}")
except:
    print("Erreur de décodage!")

# Échappement Unicode
print("\n=== ÉCHAPPEMENT UNICODE ===")
print("Python supporte \\u et \\U:")
print("\u0041 = A")
print("\u00E9 = é")
print("\u20AC = €")
print("\U0001F600 = 😀")

# Longueur de chaîne
print("\n=== LONGUEUR ===")
texte = "Café 😀"
print(f"Texte: '{texte}'")
print(f"Nombre de caractères: {len(texte)}")
print(f"Nombre d'octets UTF-8: {len(texte.encode('utf-8'))}")
print(f"Nombre d'octets UTF-16: {len(texte.encode('utf-16-le'))}")""",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='EXERCISE',
            title="Exercice: Analyseur de texte",
            content_markdown="""Crée un **analyseur de texte** qui donne des statistiques sur l'encodage.

**Fonctionnalités:**
1. Compte les caractères de chaque type (ASCII, Latin-1, Unicode)
2. Calcule la taille en différents encodages
3. Détecte les emojis
4. Recommande le meilleur encodage

**Structure:**
```python
def analyser_texte(texte):
    stats = {
        'ascii': 0,
        'latin1': 0,
        'unicode': 0,
        'emojis': 0
    }
    
    for car in texte:
        code = ord(car)
        if code < 128:
            stats['ascii'] += 1
        elif code < 256:
            stats['latin1'] += 1
        elif code >= 0x1F600 and code <= 0x1F6FF:
            stats['emojis'] += 1
            stats['unicode'] += 1
        else:
            stats['unicode'] += 1
    
    # Calculer tailles
    utf8_size = len(texte.encode('utf-8'))
    utf16_size = len(texte.encode('utf-16-le'))
    
    # Afficher résultats
    print(f"=== ANALYSE DE: {texte} ===")
    print(f"Caractères ASCII: {stats['ascii']}")
    print(f"Caractères Latin-1: {stats['latin1']}")
    print(f"Caractères Unicode: {stats['unicode']}")
    print(f"Emojis: {stats['emojis']}")
    print(f"Taille UTF-8: {utf8_size} octets")
    print(f"Taille UTF-16: {utf16_size} octets")
    
    # Recommandation
    if stats['unicode'] == 0 and stats['latin1'] == 0:
        print("Recommandation: ASCII suffit")
    elif stats['unicode'] == 0:
        print("Recommandation: Latin-1 ou UTF-8")
    else:
        print("Recommandation: UTF-8 obligatoire")

# Tests
analyser_texte("Hello World")
analyser_texte("Café €20")
analyser_texte("Hello 世界 😀")
```

**Bonus:** Ajoute la détection des différents scripts (latin, cyrillique, chinois, arabe...)!""",
            order=3
        )
        
        ContentBlock.objects.create(
            chapter=chapter2,
            type='QUIZ',
            title="Quiz: Encodage",
            content_markdown="""**Question 1:** Combien de caractères peut encoder ASCII?
- a) 64
- b) 128 ✓
- c) 256
- d) 65536

**Question 2:** Quel encodage est standard sur le web?
- a) ASCII
- b) Latin-1
- c) UTF-8 ✓
- d) UTF-16

**Question 3:** Combien d'octets pour encoder 'A' en UTF-8?
- a) 1 ✓
- b) 2
- c) 3
- d) 4

**Question 4:** Que fait la fonction ord('A')?
- a) Retourne 'A'
- b) Retourne 65 ✓
- c) Retourne 0x41
- d) Erreur""",
            order=4
        )
        
        # Chapter 3: Nombres à virgule
        chapter3 = Chapter.objects.create(
            course=course,
            title="Représentation des nombres réels",
            description="Virgule fixe et virgule flottante",
            order=3,
            is_published=True
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='TEXT',
            title="Les nombres à virgule",
            content_markdown="""## Le problème

Comment représenter des nombres comme `3.14`, `0.5`, `-2.718` en binaire?

## Virgule fixe

### Principe
Réserver un nombre fixe de bits pour la **partie entière** et pour la **partie décimale**.

### Exemple: 8 bits (4.4)
4 bits pour l'entier, 4 bits pour la décimale

```
Nombre: 5.75

Partie entière: 5 = 0101
Partie décimale: 0.75 = 0.5 + 0.25 = 1/2 + 1/4
                      = 2⁻¹ + 2⁻²
                      = 1100 (en binaire)

Résultat: 0101.1100
```

### Limites
✅ Simple et prévisible
❌ Plage limitée
❌ Précision fixe
❌ Gaspillage si beaucoup de zéros

## Virgule flottante (IEEE 754)

### Principe
Écrire le nombre en **notation scientifique** :

```
Nombre = (-1)^signe × mantisse × 2^exposant
```

### Format 32 bits (float)

| Partie | Bits | Rôle |
|--------|------|------|
| Signe | 1 | 0 = positif, 1 = négatif |
| Exposant | 8 | Décalage du point |
| Mantisse | 23 | Chiffres significatifs |

### Format 64 bits (double)

| Partie | Bits | Rôle |
|--------|------|------|
| Signe | 1 | 0 = positif, 1 = négatif |
| Exposant | 11 | Plus grande plage |
| Mantisse | 52 | Plus de précision |

### Exemple de codage

**Nombre: 12.375**

1. **Convertir en binaire:**
   - 12 = 1100
   - 0.375 = 0.011 (3/8 = 1/4 + 1/8 = 2⁻² + 2⁻³)
   - Total: 1100.011

2. **Normaliser (mantisse commence par 1):**
   - 1100.011 = 1.100011 × 2³
   - Exposant: 3
   - Mantisse: 100011 (on omet le 1 implicite)

3. **Encoder:**
   - Signe: 0 (positif)
   - Exposant: 3 + 127 = 130 = 10000010
   - Mantisse: 10001100000000000000000

### Valeurs spéciales

| Valeur | Exposant | Mantisse | Signification |
|--------|----------|----------|---------------|
| 0 | 0 | 0 | Zéro |
| ±∞ | 255 | 0 | Infini |
| NaN | 255 | ≠0 | Not a Number |

### Plages de valeurs

**Float (32 bits):**
- Plus petit: ~1.4 × 10⁻⁴⁵
- Plus grand: ~3.4 × 10³⁸
- Précision: ~7 chiffres décimaux

**Double (64 bits):**
- Plus petit: ~4.9 × 10⁻³²⁴
- Plus grand: ~1.8 × 10³⁰⁸
- Précision: ~15-16 chiffres décimaux

## Problèmes de précision

### Nombres non représentables

Certains nombres décimaux simples sont **impossibles** à représenter exactement en binaire!

**Exemple: 0.1**
```python
0.1 en binaire = 0.00011001100110011... (infini!)
```

### Conséquences

```python
>>> 0.1 + 0.2
0.30000000000000004  # ≠ 0.3 !

>>> 0.1 + 0.1 + 0.1 == 0.3
False  # Surprise!
```

### Erreurs d'arrondi

Plus on fait d'opérations, plus les erreurs s'accumulent:

```python
>>> sum = 0.0
>>> for i in range(10):
...     sum += 0.1
>>> sum
0.9999999999999999  # ≠ 1.0
```

## Bonnes pratiques

### ❌ À éviter
```python
if x == 0.3:  # Comparaison exacte dangereuse!
    ...
```

### ✅ À faire
```python
epsilon = 1e-9
if abs(x - 0.3) < epsilon:  # Comparaison avec tolérance
    ...
```

### Utiliser Decimal pour l'argent
```python
from decimal import Decimal

prix = Decimal('0.10')
total = prix + prix + prix
# Résultat exact: 0.30
```""",
            order=1
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='CODE_SAMPLE',
            title="Pratique: Nombres flottants",
            content_markdown="""import struct
import sys
from decimal import Decimal

# Problèmes classiques avec les flottants
print("=== PROBLÈMES DE PRÉCISION ===\n")

# Addition
resultat = 0.1 + 0.2
print(f"0.1 + 0.2 = {resultat}")
print(f"Est-ce égal à 0.3? {resultat == 0.3}")
print(f"Différence: {abs(resultat - 0.3)}")

print()

# Accumulation d'erreurs
somme = 0.0
for i in range(10):
    somme += 0.1
print(f"0.1 ajouté 10 fois: {somme}")
print(f"Est-ce égal à 1.0? {somme == 1.0}")

print()

# Soustraction problématique
a = 1.0
b = 0.9999999999999999
print(f"1.0 - 0.9999999999999999 = {a - b}")

# Représentation interne
print("\n=== REPRÉSENTATION IEEE 754 ===\n")

def afficher_float_binaire(nombre):
    # Convertir en bytes
    bytes_float = struct.pack('f', nombre)
    # Convertir en int 32 bits
    bits = struct.unpack('I', bytes_float)[0]
    # Extraire les parties
    signe = (bits >> 31) & 1
    exposant = (bits >> 23) & 0xFF
    mantisse = bits & 0x7FFFFF
    
    print(f"Nombre: {nombre}")
    print(f"Signe: {signe} ({'négatif' if signe else 'positif'})")
    print(f"Exposant: {exposant} (réel: {exposant - 127})")
    print(f"Mantisse: {mantisse:023b}")
    print(f"Binaire complet: {bits:032b}")
    print()

afficher_float_binaire(12.375)
afficher_float_binaire(-5.5)
afficher_float_binaire(0.1)

# Valeurs spéciales
print("=== VALEURS SPÉCIALES ===\n")
inf_pos = float('inf')
inf_neg = float('-inf')
nan = float('nan')

print(f"Infini positif: {inf_pos}")
print(f"Infini négatif: {inf_neg}")
print(f"NaN (Not a Number): {nan}")
print(f"1.0 / 0.0 = {1.0 / 0.0}")  # Attention en Python!
print(f"0.0 / 0.0 = ?")  # Erreur en Python

# Limites
print("\n=== LIMITES DES FLOTTANTS ===\n")
print(f"Float max: {sys.float_info.max}")
print(f"Float min (positif): {sys.float_info.min}")
print(f"Précision (epsilon): {sys.float_info.epsilon}")
print(f"Chiffres de précision: {sys.float_info.dig}")

# Comparaisons correctes
print("\n=== COMPARAISONS CORRECTES ===\n")

def comparer_flottants(a, b, epsilon=1e-9):
    return abs(a - b) < epsilon

x = 0.1 + 0.2
print(f"0.1 + 0.2 == 0.3 ? {x == 0.3} (mauvais)")
print(f"0.1 + 0.2 ≈ 0.3 ? {comparer_flottants(x, 0.3)} (bon)")

# Solution: Decimal pour l'exactitude
print("\n=== UTILISATION DE DECIMAL ===\n")

# Avec float (problème)
prix_float = 0.1
total_float = prix_float + prix_float + prix_float
print(f"Avec float: 0.1 + 0.1 + 0.1 = {total_float}")

# Avec Decimal (exact)
prix_decimal = Decimal('0.1')
total_decimal = prix_decimal + prix_decimal + prix_decimal
print(f"Avec Decimal: 0.1 + 0.1 + 0.1 = {total_decimal}")

# Calculs monétaires
print("\n=== CALCULS MONÉTAIRES ===")
prix_ht = Decimal('19.99')
tva = Decimal('0.20')
prix_ttc = prix_ht * (1 + tva)
print(f"Prix HT: {prix_ht} €")
print(f"TVA: {tva * 100}%")
print(f"Prix TTC: {prix_ttc} €")

# Performance
import time

print("\n=== PERFORMANCE ===")
n = 1000000

# Float
start = time.time()
somme_float = 0.0
for i in range(n):
    somme_float += 0.1
temps_float = time.time() - start

# Decimal
start = time.time()
somme_decimal = Decimal('0')
for i in range(n):
    somme_decimal += Decimal('0.1')
temps_decimal = time.time() - start

print(f"Float: {temps_float:.4f}s")
print(f"Decimal: {temps_decimal:.4f}s")
print(f"Ratio: {temps_decimal / temps_float:.1f}x plus lent")""",
            order=2
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='EXERCISE',
            title="Exercice: Calculatrice de précision",
            content_markdown="""Crée une **calculatrice** qui compare float et Decimal pour des calculs financiers.

**Fonctionnalités:**
1. Calcul de prix TTC avec TVA
2. Somme de prix multiples
3. Comparaison float vs Decimal
4. Détection des erreurs d'arrondi

**Structure:**
```python
from decimal import Decimal, getcontext

# Augmenter la précision
getcontext().prec = 28

def calculer_panier_float(prix_unitaires, quantites):
    total = 0.0
    for prix, qte in zip(prix_unitaires, quantites):
        total += prix * qte
    return total

def calculer_panier_decimal(prix_unitaires, quantites):
    total = Decimal('0')
    for prix, qte in zip(prix_unitaires, quantites):
        prix_dec = Decimal(str(prix))
        total += prix_dec * qte
    return total

# Test avec un panier d'achats
prix = [0.1, 0.2, 0.15, 0.25]  # Prix en euros
quantites = [10, 20, 15, 30]

total_float = calculer_panier_float(prix, quantites)
total_decimal = calculer_panier_decimal(prix, quantites)

print(f"Total avec float: {total_float:.20f} €")
print(f"Total avec Decimal: {total_decimal} €")
print(f"Différence: {abs(float(total_decimal) - total_float):.20f} €")

# Calcul de TVA
def appliquer_tva(prix_ht, taux_tva=20):
    # Avec Decimal pour la précision
    prix = Decimal(str(prix_ht))
    tva = Decimal(str(taux_tva)) / 100
    prix_ttc = prix * (1 + tva)
    montant_tva = prix_ttc - prix
    return float(prix_ttc), float(montant_tva)

prix_ht = 19.99
ttc, tva = appliquer_tva(prix_ht)
print(f"\n{prix_ht} € HT → {ttc:.2f} € TTC (TVA: {tva:.2f} €)")
```

**Bonus:** Ajoute la gestion des arrondis selon les règles bancaires (arrondi au centime le plus proche)!""",
            order=3
        )
        
        ContentBlock.objects.create(
            chapter=chapter3,
            type='QUIZ',
            title="Quiz: Nombres flottants",
            content_markdown="""**Question 1:** Pourquoi 0.1 + 0.2 ≠ 0.3 en Python?
- a) Bug de Python
- b) Erreur de représentation binaire ✓
- c) Problème de mémoire
- d) C'est égal en réalité

**Question 2:** Combien de bits pour un float (simple précision)?
- a) 16
- b) 32 ✓
- c) 64
- d) 128

**Question 3:** Comment comparer correctement deux flottants?
- a) if a == b
- b) if abs(a - b) < epsilon ✓
- c) if a >= b and a <= b
- d) Impossible

**Question 4:** Quel type utiliser pour des calculs monétaires précis?
- a) float
- b) int
- c) Decimal ✓
- d) double""",
            order=4
        )
        
        self.stdout.write(self.style.SUCCESS(
            f'✓ Created {course.chapters.count()} chapters with '
            f'{ContentBlock.objects.filter(chapter__course=course).count()} blocks'
        ))
