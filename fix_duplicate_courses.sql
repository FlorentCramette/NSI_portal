-- Script pour supprimer les doublons de cours sur Railway
-- À exécuter via Railway CLI ou pgAdmin

-- Supprimer tous les anciens cours
DELETE FROM courses_course;

-- Les nouveaux cours seront créés automatiquement par start.py
-- qui exécute manage.py create_snt_content au démarrage
