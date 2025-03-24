import argparse
import torch
import cv2
from ultralytics import YOLO


def detect(source, weights, conf_thres=0.5):
    model = YOLO(weights)
    
    if source.endswith(('.mp4', '.avi', '.mov')):
        cap = cv2.VideoCapture(source)
        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        
        out = cv2.VideoWriter('results/detected_video.mp4',
                              cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            results = model(frame, conf=conf_thres)
            for r in results:
                frame = r.plot()
            
            out.write(frame)
            cv2.imshow('YOLOv8 Detection', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cap.release()
        out.release()
        cv2.destroyAllWindows()
    
    else:
        img = cv2.imread(source)
        results = model(img, conf=conf_thres)
        for r in results:
            img = r.plot()
        cv2.imwrite('results/detected_image.jpg', img)
        cv2.imshow('YOLOv8 Detection', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, required=True, help='Chemin de l'image ou de la vidéo')
    parser.add_argument('--weights', type=str, required=True, help='Chemin du modèle YOLOv8')
    parser.add_argument('--conf-thres', type=float, default=0.5, help='Seuil de confiance pour la détection')
    args = parser.parse_args()
    
    detect(args.source, args.weights, args.conf_thres)
