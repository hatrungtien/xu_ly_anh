import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import urllib.request
import cv2
import numpy as np
import os
from scipy.stats import entropy
from skimage import filters
from PIL import Image, ImageTk

class TrafficImageProcessor:
    def __init__(self, master):
        self.master = master
        master.title("Traffic Image Processing")
        master.geometry("800x600")
        master.configure(bg="#f0f0f0")

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TButton", padding=10, font=("Arial", 10))
        self.style.configure("TFrame", background="#f0f0f0")

        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self.master, padding="20 20 20 20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        # File operations frame
        file_frame = ttk.LabelFrame(main_frame, text="File Operations", padding="20 20 20 20")
        file_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)

        ttk.Button(file_frame, text="Download YOLO Files", command=self.download_yolo_files).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(file_frame, text="Load Image", command=self.load_image).grid(row=0, column=1, padx=5, pady=5)

        # Image processing frame
        process_frame = ttk.LabelFrame(main_frame, text="Image Processing", padding="10 10 10 10")
        process_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)

        ttk.Button(process_frame, text="Process Image", command=self.process_image).grid(row=0, column=0, padx=5, pady=5)
        ttk.Button(process_frame, text="Detect Vehicles", command=self.detect_vehicles).grid(row=1, column=0, padx=5, pady=5)
        ttk.Button(process_frame, text="Analyze Image", command=self.analyze_image).grid(row=2, column=0, padx=5, pady=5)
        ttk.Button(process_frame, text="Sharpen Image", command=self.sharpen_image).grid(row=3, column=0, padx=5, pady=5)

        # Status frame
        status_frame = ttk.LabelFrame(main_frame, text="Status", padding="10 10 10 10")
        status_frame.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)

        self.status_text = tk.Text(status_frame, wrap=tk.WORD, width=30, height=10)
        self.status_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.status_text.config(state=tk.DISABLED)

        # Image display frame
        image_frame = ttk.LabelFrame(main_frame, text="Image Display", padding="10 10 10 10")
        image_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)

        self.original_image_label = ttk.Label(image_frame, text="Original Image")
        self.original_image_label.grid(row=0, column=0, padx=5, pady=5)

        self.enhanced_image_label = ttk.Label(image_frame, text="Enhanced Image")
        self.enhanced_image_label.grid(row=0, column=1, padx=5, pady=5)

        self.original_image_canvas = tk.Canvas(image_frame, width=300, height=200)
        self.original_image_canvas.grid(row=1, column=0, padx=5, pady=5)

        self.enhanced_image_canvas = tk.Canvas(image_frame, width=300, height=200)
        self.enhanced_image_canvas.grid(row=1, column=1, padx=5, pady=5)

        # Configure grid weights
        for frame in (main_frame, file_frame, process_frame, status_frame, image_frame):
            for i in range(4):
                frame.columnconfigure(i, weight=1)
                frame.rowconfigure(i, weight=1)

    def update_status(self, message):
        self.status_text.config(state=tk.NORMAL)
        self.status_text.insert(tk.END, message + "\n")
        self.status_text.see(tk.END)
        self.status_text.config(state=tk.DISABLED)

    def download_yolo_files(self):
        # Kiểm tra sự tồn tại của các tệp
        if os.path.isfile("coco.names") and os.path.isfile("yolov3.weights") and os.path.isfile("yolov3.cfg"):
            self.update_status("YOLOv3 files already exist.")
        else:
            try:
                # Nếu tệp không tồn tại, tải xuống
                if not os.path.isfile("coco.names"):
                    self.update_status("Downloading coco.names...")
                    urllib.request.urlretrieve("https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names", "coco.names")
                    self.update_status("Downloaded coco.names successfully.")
                if not os.path.isfile("yolov3.weights"):
                    self.update_status("Downloading yolov3.weights...")
                    urllib.request.urlretrieve("https://pjreddie.com/media/files/yolov3.weights", "yolov3.weights")
                    self.update_status("Downloaded yolov3.weights successfully.")
                if not os.path.isfile("yolov3.cfg"):
                    self.update_status("Downloading yolov3.cfg...")
                    urllib.request.urlretrieve("https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg", "yolov3.cfg")
                    self.update_status("Downloaded yolov3.cfg successfully.")

                self.update_status("YOLOv3 files downloaded successfully.")
            except Exception as e:
                self.update_status(f"Error during download: {str(e)}")

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
        if file_path:
            self.image = cv2.imread(file_path)
            if self.image is None:
                self.update_status("Error: Unable to read the image.")
            else:
                self.update_status("Image loaded successfully.")
                self.display_image(self.original_image_canvas, self.image)
        else:
            self.update_status("No image selected.")

    def process_image(self):
        if hasattr(self, 'image'):
            gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            self.processed_image = cv2.equalizeHist(gray_image)
            cv2.imwrite('processed_image.jpg', self.processed_image)
            self.update_status("Image processed and saved as 'processed_image.jpg'.")
            self.display_image(self.original_image_canvas, self.processed_image)
        else:
            self.update_status("Error: No image loaded. Please load an image first.")

    def detect_vehicles(self):
        if hasattr(self, 'processed_image'):
            net = cv2.dnn.readNet("D:/DowloadSoft/Retouch-CPU-V40/xu_ly_anh/data/yolov3.cfg", "D:/DowloadSoft/Retouch-CPU-V40/xu_ly_anh/data/yolov3.weights")
            with open("coco.names", "r") as f:
                classes = [line.strip() for line in f.readlines()]

            layer_names = net.getLayerNames()
            output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

            height, width, channels = self.processed_image.shape
            blob = cv2.dnn.blobFromImage(self.processed_image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
            net.setInput(blob)
            outs = net.forward(output_layers)

            class_ids = []
            confidences = []
            boxes = []

            for out in outs:
                for detection in out:
                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]
                    if confidence > 0.5:
                        center_x = int(detection[0] * width)
                        center_y = int(detection[1] * height)
                        w = int(detection[2] * width)
                        h = int(detection[3] * height)
                        x = int(center_x - w / 2)
                        y = int(center_y - h / 2)
                        boxes.append([x, y, w, h])
                        confidences.append(float(confidence))
                        class_ids.append(class_id)

            indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

            for i in range(len(boxes)):
                if i in indexes:
                    x, y, w, h = boxes[i]
                    label = str(classes[class_ids[i]])
                    if label in ["car", "bus", "truck", "motorbike"]:
                        cv2.rectangle(self.processed_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        cv2.putText(self.processed_image, label, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

            cv2.imwrite('detected_vehicles.jpg', self.processed_image)
            self.update_status("Vehicles detected and saved as 'detected_vehicles.jpg'.")
            self.display_image(self.original_image_canvas, self.processed_image)
        else:
            self.update_status("Error: No processed image found. Please process an image first.")

    def analyze_image(self):
        if hasattr(self, 'processed_image'):
            brightness = np.mean(self.processed_image)
            contrast = np.var(self.processed_image)
            hist = cv2.calcHist([self.processed_image], [0], None, [256], [0, 256])
            hist_normalized = hist.ravel() / hist.sum()
            img_entropy = entropy(hist_normalized)
            edges = filters.sobel(self.processed_image)
            sharpness = np.mean(np.abs(edges))

            self.update_status(f'Brightness: {brightness:.2f}\n'
                               f'Contrast: {contrast:.2f}\n'
                               f'Information Content: {img_entropy:.2f}\n'
                               f'Sharpness: {sharpness:.2f}')

        else:
            self.update_status("Error: No processed image found. Please process an image first.")

    def sharpen_image(self):
        if hasattr(self, 'processed_image'):
            kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
            sharpened_image = cv2.filter2D(self.processed_image, -1, kernel)
            cv2.imwrite('sharpened_image.jpg', sharpened_image)
            self.update_status("Sharpened image saved as 'sharpened_image.jpg'.")
            self.display_image(self.enhanced_image_canvas, sharpened_image)

            # Phân tích ảnh sau khi tăng cường
            brightness = np.mean(sharpened_image)
            contrast = np.var(sharpened_image)
            hist = cv2.calcHist([sharpened_image], [0], None, [256], [0, 256])
            hist_normalized = hist.ravel() / hist.sum()
            img_entropy = entropy(hist_normalized)
            edges = filters.sobel(sharpened_image)
            sharpness = np.mean(np.abs(edges))

            self.update_status(f'Enhanced Image - Brightness: {brightness:.2f}\n'
                               f'Enhanced Image - Contrast: {contrast:.2f}\n'
                               f'Enhanced Image - Information Content: {img_entropy:.2f}\n'
                               f'Enhanced Image - Sharpness: {sharpness:.2f}')

        else:
            self.update_status("Error: No processed image found. Please process an image first.")

    def display_image(self, canvas, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(image)
        pil_image = pil_image.resize((300, 200), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(pil_image)
        canvas.create_image(0, 0, anchor=tk.NW, image=img)
        canvas.image = img  # Keep a reference to avoid garbage collection

if __name__ == "__main__":
    root = tk.Tk()
    app = TrafficImageProcessor(root)
    root.mainloop()
