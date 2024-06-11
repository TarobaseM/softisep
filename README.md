# SoftIsep

SoftIsep est une application Django conçue pour lister les cours et les logiciels associés à une plateforme d'enseignement.

## Fonctionnalités

- Affichage de la liste des cours disponibles.
- Affichage des logiciels associés à chaque cours.
- Recherche de cours par nom.

## Utilisation

### Prérequis

- Python installé sur votre système. Téléchargez-le depuis [python.org](https://www.python.org/).
- Docker installé sur votre système. Téléchargez-le depuis [docker.com](https://www.docker.com/).

### Installation

1. Clonez ce dépôt sur votre machine :

    ```bash
    git clone https://github.com/TarobaseM/SoftIsep.git
    ```

2. Accédez au répertoire du projet :

    ```bash
    cd SoftIsep
    ```

3. Créez un environnement virtuel :

    ```bash
    python3 -m venv venv
    ```

4. Activez l'environnement virtuel :

    - Sur Windows :

        ```bash
        venv\Scripts\activate
        ```

    - Sur macOS et Linux :

        ```bash
        source venv/bin/activate
        ```

5. Installez les dépendances requises :

    ```bash
    pip install -r requirements.txt
    ```

### Exécution en local

1. Appliquez les migrations de la base de données :

    ```bash
    python manage.py migrate
    ```

2. Lancez le serveur de développement :

    ```bash
    python manage.py runserver
    ```

3. Accédez à l'application dans votre navigateur à l'adresse `http://127.0.0.1:8000/`.

### Déploiement avec Docker

1. Depuis le répertoire racine du projet, construisez l'image Docker :

    ```bash
    docker build -t softisep .
    ```

2. Lancez un conteneur Docker à partir de l'image construite :

    ```bash
    docker run -d -p 8000:8000 softisep
    ```

3. Accédez à l'application dans votre navigateur à l'adresse `http://localhost:8000/`.

## Contributeurs

- Tom Amar
