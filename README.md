# 🌸 FastAPI Iris Classifier — Deploying ML Models with FastAPI 🚀

Build, containerize and ship a **decision-tree Iris flower classifier** in minutes.  
The project trains a model on the classic *Iris* dataset and serves real-time predictions through a fast, documented REST API.

&nbsp;

| &nbsp; | **Tech Stack** |
|-------|----------------|
| 📦 Model | scikit-learn Decision Tree |
| 🖧 API & Docs | FastAPI · Swagger · ReDoc |
| 🐳 Deployment | Docker-ready |
| 💻 Optional UI | Streamlit |

***

## 📂 Project Layout

```
fastapi-iris-app/
├─ main.py            # FastAPI application
├─ train_model.py     # Model training script
├─ iris_model.pkl     # Saved model
├─ requirements.txt   # Python dependencies
├─ Dockerfile         # Container recipe
├─ streamlit_app.py   # (Optional) Streamlit demo
├─ test_requests.http # REST examples
└─ decision_tree.png  # Model visualization
```

***

## ⚡ Key Features

- ✅ **One-command training** of an Iris classifier  
- ✅ **/predict** endpoint for real-time inference  
- ✅ **Auto-generated docs** at `/docs` (Swagger) & `/redoc`  
- ✅ **Container-first** workflow with Docker  
- ✅ *(Optional)* **Streamlit dashboard** for quick experiments  

***

## 🛠️ Installation

### 1. Clone the repo
```bash
git clone https://github.com/Nikhilnsd/fastapi-iris-app.git
cd fastapi-iris-app
```

### 2. Create a virtual environment
```bash
python -m venv venv
# Mac / Linux
source venv/bin/activate
# Windows
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the API server
```bash
uvicorn main:app --reload
```
Open your browser:

* Swagger UI →   
* ReDoc → 

***

## 📡 How to Use the API

`POST /predict`

```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

Response:

```json
{
  "species": "setosa"
}
```

***

## 🐳 Run with Docker

```bash
docker build -t iris-fastapi .
docker run -p 8000:80 iris-fastapi
```
Then visit → 

***

## 📈 Model Details

* **Algorithm:** Decision Tree Classifier 🌳  
* **Dataset:** UCI Iris  
* **Classes:** *setosa*, *versicolor*, *virginica*  

***

## 🚀 Roadmap

- 🔒 Add authentication & rate-limiting  
- ☁️ Deploy to AWS / Azure / Heroku  
- 🔄 Integrate CI/CD (GitHub Actions)  
- 📝 Centralized logging & monitoring  

***

## 👨💻 Author

**Nikhil S Doshikar**  
✉️ *nikhilnsd01@gmail.com*  
🔗 [LinkedIn](https://www.linkedin.com/in/nikhil-doshikar-4b12b21a0/)

If this project helps you, **please give it a ⭐ on GitHub**!

***
