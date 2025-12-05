# NSI Portal - Script de démarrage automatique
# Ce script vérifie et démarre automatiquement le portail NSI

Write-Host "=====================================" -ForegroundColor Cyan
Write-Host "   Portail NSI - Démarrage           " -ForegroundColor Cyan
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host ""

# Se placer dans le répertoire du projet
Set-Location -Path $PSScriptRoot

# Vérifier si l'environnement virtuel existe
if (-not (Test-Path "venv")) {
    Write-Host "[!] Environnement virtuel non trouvé. Création..." -ForegroundColor Yellow
    python -m venv venv
    Write-Host "[✓] Environnement virtuel créé" -ForegroundColor Green
}

# Activer l'environnement virtuel
Write-Host "[*] Activation de l'environnement virtuel..." -ForegroundColor Blue
& ".\venv\Scripts\Activate.ps1"

# Vérifier si les dépendances sont installées
Write-Host "[*] Vérification des dépendances..." -ForegroundColor Blue
$pipList = pip list
if ($pipList -notmatch "Django") {
    Write-Host "[!] Installation des dépendances..." -ForegroundColor Yellow
    pip install -r requirements.txt
    Write-Host "[✓] Dépendances installées" -ForegroundColor Green
} else {
    Write-Host "[✓] Dépendances déjà installées" -ForegroundColor Green
}

# Vérifier si le fichier .env existe
if (-not (Test-Path ".env")) {
    Write-Host "[!] Fichier .env non trouvé" -ForegroundColor Red
    Write-Host "[*] Créez un fichier .env à partir de .env.example" -ForegroundColor Yellow
    Write-Host "[*] Exemple de contenu :" -ForegroundColor Yellow
    Write-Host ""
    Get-Content ".env.example"
    Write-Host ""
    $continue = Read-Host "Voulez-vous continuer sans .env ? (O/N)"
    if ($continue -ne "O" -and $continue -ne "o") {
        Write-Host "[X] Arrêt du script" -ForegroundColor Red
        exit 1
    }
}

# Vérifier si la base de données est configurée
Write-Host "[*] Vérification de la base de données..." -ForegroundColor Blue
$migrationsExist = python manage.py showmigrations 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "[!] Base de données non configurée" -ForegroundColor Yellow
    Write-Host "[*] Création des migrations..." -ForegroundColor Blue
    python manage.py makemigrations
    Write-Host "[*] Application des migrations..." -ForegroundColor Blue
    python manage.py migrate
    Write-Host "[✓] Base de données configurée" -ForegroundColor Green
    
    # Proposer de créer des données de test
    Write-Host ""
    $createData = Read-Host "Voulez-vous créer des données de test ? (O/N)"
    if ($createData -eq "O" -or $createData -eq "o") {
        python manage.py create_sample_data
        Write-Host "[✓] Données de test créées" -ForegroundColor Green
    }
} else {
    Write-Host "[✓] Base de données configurée" -ForegroundColor Green
}

# Collecter les fichiers statiques (si nécessaire)
if (-not $env:DEBUG -or $env:DEBUG -eq "False") {
    Write-Host "[*] Collecte des fichiers statiques..." -ForegroundColor Blue
    python manage.py collectstatic --noinput
    Write-Host "[✓] Fichiers statiques collectés" -ForegroundColor Green
}

Write-Host ""
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host "   Démarrage du serveur Django       " -ForegroundColor Cyan
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "[*] Le serveur démarre sur : http://127.0.0.1:8000" -ForegroundColor Green
Write-Host "[*] Interface admin : http://127.0.0.1:8000/admin" -ForegroundColor Green
Write-Host ""
Write-Host "[*] Comptes de test (si créés) :" -ForegroundColor Yellow
Write-Host "    - Admin     : admin / admin123" -ForegroundColor White
Write-Host "    - Professeur: prof_martin / prof123" -ForegroundColor White
Write-Host "    - Élève     : eleve_alice / eleve123" -ForegroundColor White
Write-Host ""
Write-Host "[*] Appuyez sur Ctrl+C pour arrêter le serveur" -ForegroundColor Cyan
Write-Host ""

# Démarrer le serveur Django
python manage.py runserver
