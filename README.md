# HematoVision

Advanced Blood Cell Classification using Transfer Learning

Short instructions to get this project running locally.

Prerequisites
- Git
- Python 3.8+ (virtual environment recommended)
- SSH key or GitHub credentials configured for pushing

Quick setup
1. Open a terminal and navigate to the project root:

   cd "e:\Nagendra\projects\HematoVision-Advanced-Blood-Cell-Classification-Using-Transfer-Learning-by-LTVIP2025TMID44712-main\HematoVision-Advanced-Blood-Cell-Classification-Using-Transfer-Learning"

2. Create & activate a virtual environment (Windows PowerShell):

   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

3. Install dependencies:

   pip install -r "project requriments\requirements.txt"

   If `requirements.txt` is missing or incomplete, install manually:

   pip install flask tensorflow opencv-python numpy matplotlib

4. Place the trained model file (if not included) at:

   project requriments/Blood Cell.h5

5. Run the application:

   python app.py

6. Open the app in your browser:

   http://localhost:5000

Notes
- The repository intentionally ignores large model files (e.g. *.h5). Add the trained model manually or store it in an external storage service and update the path in `app.py`.
- The server runs in development mode. Use a WSGI server for production (e.g., Gunicorn on Linux).

Push to your GitHub repository
1. Initialize git, add files, and push (replace remote URL if different):

   git init
   git add .
   git commit -m "Initial import of HematoVision project"
   git branch -M main
   git remote add origin git@github.com:Nagendrasomisetti/HematoVision.git
   git push -u origin main

If you prefer HTTPS for remote:

   git remote add origin https://github.com/Nagendrasomisetti/HematoVision.git
   git push -u origin main
## 🧠 Team ID : LTVIP2026TMIDS38361

### Team Size : 5
---
### 👨‍💻 Team Members
Team Leader : Mattaparthi Sai Santhosh Vamsi

Team member : Mullamgi Vidya Sri

Team member : Munganda Koushik

Team member : Nagendra Somisetti

Team member : Dune Sankar Narayan Sathvik
---
# 🧬 HematoVision: Advanced Blood Cell Classification Using Transfer Learning

**HematoVision** is a deep learning-powered web application designed to classify microscopic images of blood cells into one of four categories:

* 🔴 **Eosinophil**
* 🟢 **Lymphocyte**
* 🟡 **Monocyte**
* 🔵 **Neutrophil**

This intelligent diagnostic tool leverages **Transfer Learning** with **MobileNetV2** to deliver high-accuracy predictions in real-time, wrapped in a clean and intuitive **Flask**-based web interface.

---

## 🚀 How It Works

1. **📤 Upload** a microscopic image of a blood cell.
2. **🔍 The model** processes the image using deep learning.
3. **📈 You get** the predicted class along with a preview of the uploaded image.

This makes HematoVision an ideal assistant for biomedical learners, educators, and early-stage researchers.

---

## ⚙️ Features

* ✅ Real-time image classification
* ✅ Built-in preprocessing pipeline with OpenCV
* ✅ Lightweight model (MobileNetV2) for quick inference
* ✅ Web interface with smooth UX and visual feedback
* ✅ Base64 image embedding for fast, secure previews

---

## 🛠️ Tech Stack

| Layer         | Technologies Used                          |
| ------------- | ------------------------------------------ |
| **Model**     | TensorFlow / Keras with MobileNetV2        |
| **Backend**   | Python, Flask                              |
| **Image Ops** | OpenCV for image preprocessing             |
| **Frontend**  | HTML5, CSS3 (light theme with stunning UI) |

---

## 📁 Project Structure

```bash
HematoVision/
├── app.py               # Main Flask application
├── Blood Cell.h5        # Pretrained MobileNetV2 model (~60MB)
├── requirements.txt     # Project dependencies
├── static/              # Uploaded image storage
└── templates/           # HTML templates
    ├── home.html        # File upload and landing page
    └── result.html      # Prediction result display page
```

---

## 💻 Run Locally

You can run this project easily on your local system. Just follow these steps:

### 1️⃣ Clone the Repository

```bash
git
cd HematoVision-Advanced-Blood-Cell-Classification-Using-Transfer-Learning-by-LTVIP2026TMIDS38361
```

### 2️⃣ Create a Virtual Environment (Optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate       # On Windows
# source venv/bin/activate  # On macOS/Linux
```

### 3️⃣ Install the Required Packages

```bash
pip install -r requirements.txt
```

### 4️⃣ Start the Flask App

```bash
python app.py
```

Then open your browser and go to:
🔗 [http://localhost:5000]

---

## 📸 Sample Output

> 🧠 The application shows the predicted blood cell type alongside the uploaded image, providing instant visual confirmation.

---

## 👨‍🔬 Future Enhancements

* Integration with mobile camera input
* Batch image classification
* Confidence score visualization
* CSV download for prediction logs

---

## 🙌 Acknowledgements

Thanks to the open-source community for datasets, MobileNetV2 pretrained weights, and Flask ecosystem.

---

