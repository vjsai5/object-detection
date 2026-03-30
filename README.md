# 🧠 YOLOv8 Live Object Counter

A real-time object detection and tracking system built using YOLOv8 and OpenCV. This project counts unique objects from a live webcam feed using tracking IDs.

---

## 🚀 Features

* 🎥 Real-time webcam detection
* 🧠 YOLOv8 object detection
* 🔁 Object tracking with persistent IDs
* 🔢 Unique object counting (no duplicates)
* 🔄 Reset counter functionality
* ❌ Quit anytime

---

## 🛠️ Tech Stack

* Python
* Ultralytics YOLOv8
* OpenCV
* PyTorch
* NumPy

## 🎮 Controls

| Key | Action               |
| --- | -------------------- |
| Q   | Quit application     |
| R   | Reset object counter |

---

## 🧠 How It Works

1. Webcam captures live frames
2. YOLOv8 detects objects in each frame
3. Tracker assigns a unique ID to each object
4. IDs are stored in a set (`seen_ids`)
5. Only new IDs increase the count
---

## ⚠️ Requirements

* Python 3.8 or higher
* Webcam (built-in or external)
* Internet (first run downloads YOLO model)

---

## ⚡ Performance Tips

* Use smaller resolution for faster processing
* Use GPU (CUDA) if available
* Close other heavy applications

---

## 🧩 Common Issues & Fixes

### ❌ Webcam not opening

Try:

```python
cv2.VideoCapture(1)
---

## 📜 License

This project is open-source and available under the MIT License.

---

## 🙌 Acknowledgements

* Ultralytics YOLOv8
* OpenCV community
* PyTorch team

---

## ⭐ Support

If you like this project:

* ⭐ Star the repository
* 🍴 Fork it
* 🧠 Share ideas

---

