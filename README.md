# valo_vision

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