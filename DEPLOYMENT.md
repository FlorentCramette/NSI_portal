# 🚀 Guide de Déploiement en Production

Ce guide explique comment déployer le Portail NSI sur un serveur de production.

---

## 📋 Prérequis

- Serveur Linux (Ubuntu 22.04 LTS recommandé)
- Python 3.10+
- PostgreSQL 14+
- Nginx
- Supervisor (pour gérer les processus)
- Nom de domaine configuré (optionnel mais recommandé)

---

## 🔧 Configuration du serveur

### 1. Mise à jour du système

```bash
sudo apt update
sudo apt upgrade -y
```

### 2. Installation des dépendances

```bash
# Python et pip
sudo apt install python3 python3-pip python3-venv -y

# PostgreSQL
sudo apt install postgresql postgresql-contrib -y

# Nginx
sudo apt install nginx -y

# Supervisor
sudo apt install supervisor -y

# Dépendances système pour psycopg2
sudo apt install libpq-dev python3-dev -y
```

---

## 🗄️ Configuration PostgreSQL

### 1. Créer la base de données et l'utilisateur

```bash
sudo -u postgres psql
```

```sql
CREATE DATABASE nsi_platform_prod;
CREATE USER nsi_prod_user WITH PASSWORD 'VoTrE_MoT_dE_pAsSe_SeCuRiSe';
ALTER ROLE nsi_prod_user SET client_encoding TO 'utf8';
ALTER ROLE nsi_prod_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE nsi_prod_user SET timezone TO 'Europe/Paris';
GRANT ALL PRIVILEGES ON DATABASE nsi_platform_prod TO nsi_prod_user;
\q
```

### 2. Sécuriser PostgreSQL

Éditez `/etc/postgresql/14/main/pg_hba.conf` :
```
# Autoriser uniquement les connexions locales
local   all             all                                     peer
host    all             all             127.0.0.1/32            md5
```

Redémarrez PostgreSQL :
```bash
sudo systemctl restart postgresql
```

---

## 📦 Déploiement de l'application

### 1. Créer un utilisateur dédié

```bash
sudo useradd -m -s /bin/bash nsi
sudo su - nsi
```

### 2. Cloner le projet

```bash
cd /home/nsi
git clone https://github.com/votre-repo/NSI_portal.git
cd NSI_portal
```

Ou transférez les fichiers avec `scp` ou `rsync` depuis votre machine locale :
```bash
# Depuis votre machine locale
rsync -avz C:/dev/NSI_portal/ user@serveur:/home/nsi/NSI_portal/
```

### 3. Créer l'environnement virtuel

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
pip install gunicorn  # Serveur WSGI pour production
```

### 4. Configuration des variables d'environnement

Créez `/home/nsi/NSI_portal/.env` :
```ini
SECRET_KEY=votre-clé-secrète-très-longue-générée-aléatoirement-128-caractères
DEBUG=False
ALLOWED_HOSTS=votre-domaine.fr,www.votre-domaine.fr,adresse-ip-serveur

# PostgreSQL
DB_NAME=nsi_platform_prod
DB_USER=nsi_prod_user
DB_PASSWORD=VoTrE_MoT_dE_pAsSe_SeCuRiSe
DB_HOST=localhost
DB_PORT=5432

# Email (optionnel, pour réinitialisation de mot de passe)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=votre-email@gmail.com
EMAIL_HOST_PASSWORD=votre-mot-de-passe-application
```

**Générer une SECRET_KEY sécurisée :**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 5. Configuration Django pour la production

Modifiez `nsi_project/settings.py` pour ajouter :

```python
# À la fin du fichier
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
```

### 6. Initialiser la base de données

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

### 7. Tester avec Gunicorn

```bash
gunicorn --bind 0.0.0.0:8000 nsi_project.wsgi:application
```

Testez dans un navigateur : `http://adresse-ip-serveur:8000`

---

## 🔄 Configuration Supervisor

Supervisor gère le démarrage automatique de Gunicorn.

### Créer le fichier de configuration

`/etc/supervisor/conf.d/nsi_portal.conf` :
```ini
[program:nsi_portal]
command=/home/nsi/NSI_portal/venv/bin/gunicorn --workers 3 --bind unix:/home/nsi/NSI_portal/nsi_portal.sock nsi_project.wsgi:application
directory=/home/nsi/NSI_portal
user=nsi
autostart=true
autorestart=true
redirect_stderr=true
stdout_logfile=/home/nsi/NSI_portal/logs/gunicorn.log
stderr_logfile=/home/nsi/NSI_portal/logs/gunicorn_error.log
```

### Créer le répertoire des logs

```bash
sudo mkdir -p /home/nsi/NSI_portal/logs
sudo chown nsi:nsi /home/nsi/NSI_portal/logs
```

### Activer la configuration

```bash
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start nsi_portal
sudo supervisorctl status
```

---

## 🌐 Configuration Nginx

### Créer la configuration

`/etc/nginx/sites-available/nsi_portal` :
```nginx
server {
    listen 80;
    server_name votre-domaine.fr www.votre-domaine.fr;

    client_max_body_size 10M;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        alias /home/nsi/NSI_portal/staticfiles/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    location /media/ {
        alias /home/nsi/NSI_portal/media/;
        expires 30d;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/nsi/NSI_portal/nsi_portal.sock;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### Activer le site

```bash
sudo ln -s /etc/nginx/sites-available/nsi_portal /etc/nginx/sites-enabled/
sudo nginx -t  # Tester la configuration
sudo systemctl restart nginx
```

### Tester

Visitez `http://votre-domaine.fr` ou `http://adresse-ip-serveur`

---

## 🔐 Configuration SSL avec Let's Encrypt (HTTPS)

### 1. Installer Certbot

```bash
sudo apt install certbot python3-certbot-nginx -y
```

### 2. Obtenir un certificat SSL

```bash
sudo certbot --nginx -d votre-domaine.fr -d www.votre-domaine.fr
```

Suivez les instructions. Certbot modifiera automatiquement la configuration Nginx.

### 3. Renouvellement automatique

Le renouvellement est automatique. Testez avec :
```bash
sudo certbot renew --dry-run
```

---

## 🔥 Firewall (UFW)

```bash
sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'
sudo ufw enable
sudo ufw status
```

---

## 📊 Monitoring et logs

### Voir les logs Gunicorn

```bash
tail -f /home/nsi/NSI_portal/logs/gunicorn.log
tail -f /home/nsi/NSI_portal/logs/gunicorn_error.log
```

### Voir les logs Nginx

```bash
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log
```

### Voir les logs PostgreSQL

```bash
sudo tail -f /var/log/postgresql/postgresql-14-main.log
```

### Redémarrer les services

```bash
# Redémarrer Gunicorn
sudo supervisorctl restart nsi_portal

# Redémarrer Nginx
sudo systemctl restart nginx

# Redémarrer PostgreSQL
sudo systemctl restart postgresql
```

---

## 🔄 Mise à jour de l'application

### Script de déploiement automatique

Créez `/home/nsi/NSI_portal/deploy.sh` :
```bash
#!/bin/bash
set -e

echo "📦 Pulling latest changes..."
git pull origin main

echo "📥 Installing dependencies..."
source venv/bin/activate
pip install -r requirements.txt

echo "🗃️ Running migrations..."
python manage.py migrate

echo "📂 Collecting static files..."
python manage.py collectstatic --noinput

echo "🔄 Restarting Gunicorn..."
sudo supervisorctl restart nsi_portal

echo "✅ Deployment complete!"
```

Rendez-le exécutable :
```bash
chmod +x /home/nsi/NSI_portal/deploy.sh
```

Pour déployer une nouvelle version :
```bash
cd /home/nsi/NSI_portal
./deploy.sh
```

---

## 💾 Sauvegardes

### Sauvegarde de la base de données

Créez un script `/home/nsi/backup_db.sh` :
```bash
#!/bin/bash
BACKUP_DIR="/home/nsi/backups"
DATE=$(date +%Y-%m-%d_%H-%M-%S)
FILENAME="nsi_platform_$DATE.sql"

mkdir -p $BACKUP_DIR

pg_dump -U nsi_prod_user -h localhost nsi_platform_prod > $BACKUP_DIR/$FILENAME

# Garder seulement les 30 derniers backups
find $BACKUP_DIR -name "nsi_platform_*.sql" -mtime +30 -delete

echo "Backup créé : $FILENAME"
```

### Automatiser avec cron

```bash
crontab -e
```

Ajoutez :
```
# Backup quotidien à 2h du matin
0 2 * * * /home/nsi/backup_db.sh
```

### Restaurer une sauvegarde

```bash
psql -U nsi_prod_user -h localhost nsi_platform_prod < /home/nsi/backups/nsi_platform_YYYY-MM-DD.sql
```

---

## 🔒 Sécurité supplémentaire

### 1. Fail2ban (protection contre brute force)

```bash
sudo apt install fail2ban -y
```

Créez `/etc/fail2ban/jail.local` :
```ini
[DEFAULT]
bantime = 3600
findtime = 600
maxretry = 5

[sshd]
enabled = true

[nginx-limit-req]
enabled = true
filter = nginx-limit-req
logpath = /var/log/nginx/error.log
```

```bash
sudo systemctl restart fail2ban
```

### 2. Désactiver le login root SSH

Éditez `/etc/ssh/sshd_config` :
```
PermitRootLogin no
PasswordAuthentication no  # Si vous utilisez des clés SSH
```

```bash
sudo systemctl restart sshd
```

### 3. Mises à jour automatiques

```bash
sudo apt install unattended-upgrades -y
sudo dpkg-reconfigure --priority=low unattended-upgrades
```

---

## 📈 Optimisations

### 1. Redis pour le cache

```bash
sudo apt install redis-server -y
pip install django-redis
```

Dans `settings.py` :
```python
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'
```

### 2. Compression Gzip dans Nginx

Dans `/etc/nginx/nginx.conf` :
```nginx
gzip on;
gzip_vary on;
gzip_proxied any;
gzip_comp_level 6;
gzip_types text/plain text/css text/xml text/javascript application/json application/javascript application/xml+rss;
```

---

## ✅ Checklist de déploiement

- [ ] PostgreSQL configuré et sécurisé
- [ ] Variables d'environnement configurées (`.env`)
- [ ] `DEBUG=False` en production
- [ ] `ALLOWED_HOSTS` configuré
- [ ] Migrations appliquées
- [ ] Fichiers statiques collectés
- [ ] Superuser créé
- [ ] Gunicorn testé
- [ ] Supervisor configuré et actif
- [ ] Nginx configuré et actif
- [ ] SSL/HTTPS configuré (Let's Encrypt)
- [ ] Firewall activé (UFW)
- [ ] Fail2ban installé
- [ ] Sauvegardes automatiques configurées
- [ ] Monitoring mis en place
- [ ] Tests de charge effectués

---

## 🆘 Dépannage

### Erreur 502 Bad Gateway
```bash
# Vérifier le statut de Gunicorn
sudo supervisorctl status nsi_portal

# Vérifier les logs
tail -f /home/nsi/NSI_portal/logs/gunicorn_error.log
```

### Permission denied sur le socket
```bash
sudo chown nsi:www-data /home/nsi/NSI_portal/nsi_portal.sock
sudo chmod 660 /home/nsi/NSI_portal/nsi_portal.sock
```

### Fichiers statiques non chargés
```bash
python manage.py collectstatic --noinput
sudo systemctl restart nginx
```

---

**Bon déploiement ! 🚀**
