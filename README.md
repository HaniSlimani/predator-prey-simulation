# Simulation Prédateurs / Proies

Simulation interactive d'un écosystème prédateurs-proies basée sur un automate cellulaire, inspirée du **Jeu de la Vie** de Conway et du modèle mathématique de **Lotka-Volterra**.

Étude de l'impact de différents paramètres biologiques (taux de reproduction, période de jeûne, densité d'obstacles, proportion initiale entre espèces) sur la dynamique des populations sur le long terme.

## Aperçu

Le monde est représenté par une grille où évoluent trois entités :

- 🟦 **Moutons (proies)** — se déplacent aléatoirement et se reproduisent périodiquement
- 🟥 **Loups (prédateurs)** — chassent les moutons, se reproduisent, meurent de faim s'ils ne mangent pas
- ⬛ **Obstacles** — terrain infranchissable (modélise un environnement non homogène)

À chaque itération, le simulateur affiche l'état du monde et trace en parallèle la courbe d'évolution des deux populations dans le temps.

## Fonctionnalités

- Simulation visuelle en temps réel via **Pygame**
- Génération aléatoire de l'état initial (proportions paramétrables)
- Tracé automatique des courbes de population avec **Matplotlib**
- Détection du pic de prédateurs (référence visuelle sur le graphe)
- Étude de stabilité : recherche des conditions qui mènent à un équilibre, à l'extinction d'une espèce, ou à des oscillations cycliques

## Paramètres explorés

Le projet a fait l'objet d'une **étude expérimentale systématique**. Les paramètres testés :

| Paramètre | Description | Valeurs testées |
|-----------|-------------|-----------------|
| `SHEEP_BREED` | Cycle de reproduction des moutons | 1 à 5 |
| `WOLF_BREED` | Cycle de reproduction des loups | 2 à 12 |
| `WOLF_STARVE` | Nombre d'itérations sans manger avant mort | 1 à 8 |
| `OBSTACLE` | Densité d'obstacles | 100 à 1000 |
| Proportion loups/moutons | Rapport initial entre les deux populations | 10 % à 100 % |

Chaque configuration a été simulée et les résultats sont disponibles dans `Predateur_Proie_Modelisation/Graph/` et `Video_Modele/`.

## Structure

```
Predateur_Proie_Modelisation/
├── Code/
│   └── Pred_Prey.py              # Simulation principale (Pygame + Matplotlib)
├── Graph/                         # ~40 graphes d'expérimentation
├── Video_Modele/                  # Captures vidéo des simulations marquantes
├── Presentation/
│   └── Pred vs Prey Model Dynamic.pdf
└── Rapport final pour l'Are Proies VS Prédateurs.pdf

Lien_ressources.md                 # Sources scientifiques utilisées
README.md
```

## Utilisation

### Prérequis
```bash
pip install pygame numpy matplotlib
```

### Lancer la simulation
```bash
python Predateur_Proie_Modelisation/Code/Pred_Prey.py
```

### Contrôles
- **Clic gauche** — initialiser le monde (place aléatoirement moutons, loups et obstacles)
- **Espace** — démarrer / arrêter la simulation
- À l'arrêt, le graphe d'évolution des populations s'affiche automatiquement

## Contexte

Projet réalisé dans le cadre du module **ARE (Atelier de Recherche Encadrée)** en L1 Informatique à Sorbonne Université. L'objectif pédagogique était de mener un projet de recherche complet : formulation d'une problématique, recherche bibliographique, modélisation, expérimentation et restitution.

## Auteurs

- Hani Slimani
- Fernando Li
- Phuong Hoang
- Yasmine Ayed
