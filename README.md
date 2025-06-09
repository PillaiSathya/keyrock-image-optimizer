# 🌟 Keyrock Challenge – Image Optimizer on Kubernetes✨✨

This project simulates a production-ready deployment of a lightweight Python-based image optimizer that can **resize** and **compress** images via Docker and Kubernetes.

---

## 🚀 Features.

- 🐍 Python app with Pillow library
- 🐳 Dockerized and pushed to Docker Hub
- ☸️ Kubernetes manifests for:
  - Deployment
  - Service (LoadBalancer)
  - Secret management
  - Resource limits
  - Prometheus metrics annotation
- 🤖 GitHub Actions (CI/CD pipeline simulated)

---

## 🛠 Tech Stack

| Tool        | Purpose                       |
|-------------|-------------------------------|
| Python + Pillow | Image processing          |
| Docker      | Containerization              |
| Kubernetes  | Container orchestration       |
| GitHub Actions | CI/CD automation (simulated) |
| Prometheus  | Metrics support (via annotation) |

---

## 🔐 Secrets Used

| Key      | Description                      |
|----------|----------------------------------|
| `API_KEY` | Stored in Kubernetes Secret, simulated for production use |

> ⚠️ API key usage is mocked — not used in actual image processing logic.

---

## 📦 Docker

To build and run the image locally:

```bash
# Build image
docker build -t image-optimizer .

# Resize image
docker run --rm -v "${PWD}:/app" -w /app --entrypoint python image-optimizer main.py input.jpg output.jpg --resize 300 300

# Compress image
docker run --rm -v "${PWD}:/app" -w /app --entrypoint python image-optimizer main.py input.jpg output_compress.jpg --compress 70

## 🎯 Demo – Before vs After

| Before | After |
|--------|-------|
| ![Input](demo/input.jpg) | ![Output](demo/output.jpg) |


☸️ Kubernetes Deployment
Apply all manifests:

bash
Copy
Edit
kubectl apply -f k8s/
Check pod and service status:

bash
Copy
Edit
kubectl get pods
kubectl get svc
🌐 Access the service via external LoadBalancer IP (minikube or cloud platform).

📁 Project Structure
css
Copy
Edit
keyrock-challenge/
├── app/
│   └── main.py
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── secret.yaml
├── Dockerfile
├── README.md
└── input.jpg (optional)
🔄 GitHub Actions (Simulated)
A .github/workflows/docker-build.yml exists to simulate CI/CD behavior (not triggered automatically in this local setup).

🧠 Author
👩‍💻 Sathya Pillai – DevOps Engineer in training

💬 Connect: GitHub

📌 Notes
This is a learning project designed for DevOps practice.

Real-world secret management and authentication can be added using Vault or cloud IAM.
