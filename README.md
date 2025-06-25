# 🧊 Frosty-8: Handwritten Digit Recognition with Gradio + TensorFlow

Frosty-8 is a lightweight yet powerful web-based digit recognition app using a Convolutional Neural Network (CNN) trained on the MNIST dataset, and deployed with an interactive [Gradio](https://www.gradio.app/) interface.

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/2/27/MnistExamples.png" width="400" />
</p>

---

## 🚀 Features

- 🎨 Draw a digit (0–9) on a sketchpad
- 🤖 Predicts the top 3 most likely digits
- 🧠 Powered by a custom-trained CNN model
- 📊 Training and visualization via Jupyter Notebook
- 🌐 One-click web UI using Gradio

---

## 🗂️ Project Structure

```
frosty-8-mnist-gradio-project/
├── main.py                # Gradio web interface
├── train.ipynb            # Model training notebook
├── models/
│   └── mnist_trained_model.h5  # Trained CNN model
├── pyproject.toml         # Project dependencies (PEP 621)
├── .python-version        # Python version
└── README.md              # Project overview
```

---

## 🧑‍💻 Local Setup

### 1. Clone the repo

```bash
git clone https://github.com/your-username/frosty-8-mnist-gradio-project.git
cd frosty-8-mnist-gradio-project
```

### 2. Create virtual environment (recommended)

```bash
python3.12 -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
# or if using PEP 621 style:
uv pip install -r pyproject.toml
```

> Requires Python ≥ 3.12 and TensorFlow 2.19.0rc0

---

## 🚦 Run the Web App

```bash
python main.py
```

Open your browser and go to: [http://localhost:8080](http://localhost:8080)

---

## 🧠 Model Summary

The model is a CNN with:

- 2 convolutional + max pooling layers
- Flatten + Dense + Dropout
- Softmax output for 10 classes (digits 0–9)
- Trained on MNIST with 99%+ accuracy

You can retrain or modify the architecture via `train.ipynb`.

---

## 🛠 Deployment

This app can be deployed easily on:

### ▶ Render

1. Set Python version to 3.12
2. Set Start command: `python main.py`
3. Expose port `8080`
4. Optionally, use `requirements.txt` or `pyproject.toml`

### ▶ Railway

1. Add a new project and upload the repo
2. Set the environment variable: `PORT=8080`
3. Deploy with Python environment enabled

---

## 📦 Requirements

Major dependencies:

- `tensorflow==2.19.0rc0`
- `gradio>=5.34.2`
- `numpy`, `matplotlib`, `pandas`, `scikit-learn`
- Optional: `ipykernel` for notebook use

---

## 📊 Results & Visuals

<p align="center">
  <img src="https://miro.medium.com/v2/resize:fit:1000/format:webp/1*2wOTne5Y_euHFM7pMSJKRg.png" width="500" />
</p>

- 99%+ accuracy on validation
- Real-time inference in browser
- Robust on most drawn digits

---

## 🧠 Credits

- Trained using TensorFlow/Keras on the classic MNIST dataset
- Web UI powered by Gradio
- Built by [Frsoty-8](https://github.com/Frosty-8)

---

## 📜 License

MIT License — use freely, just give credit.
