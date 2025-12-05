# NSI Portal - Script de test
# Ce script lance les tests du projet

Write-Host "=====================================" -ForegroundColor Cyan
Write-Host "   Portail NSI - Tests                " -ForegroundColor Cyan
Write-Host "=====================================" -ForegroundColor Cyan
Write-Host ""

# Activer l'environnement virtuel
if (Test-Path "venv") {
    & ".\venv\Scripts\Activate.ps1"
} else {
    Write-Host "[!] Environnement virtuel non trouvé" -ForegroundColor Red
    Write-Host "[*] Exécutez d'abord start.ps1" -ForegroundColor Yellow
    exit 1
}

Write-Host "[*] Lancement des tests..." -ForegroundColor Blue
Write-Host ""

# Lancer les tests
python manage.py test

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "[✓] Tous les tests sont passés !" -ForegroundColor Green
} else {
    Write-Host ""
    Write-Host "[X] Certains tests ont échoué" -ForegroundColor Red
    exit 1
}
