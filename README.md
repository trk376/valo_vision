# valo_vision
Ce projet est un projet de computer vision implémenté avec YOLOv8 permettant de detecter les agents de valorant sur la minimap pouvant servir par la suite à creer étudier les deplacements de joueurs/équipes.
Le projet est à ses débuts et les models ont encore besoin d'entrainements. les agents qu'il peut actuellement detecter sont  : omen , jett, sova, neon, cypher, breach.
## Installation
### Cloner le projet 
```
git clone https://github.com/trk376/valo_vision.git
```
### Installer les dépendances
```
pip install -r requirements.txt
```
## Utilisation
### Detection sur une image 
```
python scripts/detect.py --weights models/best.pt --source image.jpg
```

### Detection sur une video
```
python scripts/detect.py --weights models/best.pt --source video.mp4
```