# IMS

Inventory Management System (IMS)

📌 Project Overview

The Inventory Management System (IMS) is a desktop-based application designed to efficiently manage inventory records. It allows users to add, update, delete, and track products using a user-friendly interface built with Tkinter. The backend API is developed using Flask, and the data is stored in an SQLite database.

🛠 Tech Stack

Frontend: Python (Tkinter)

Backend: Flask (REST API)

Database: SQLite (ims.db)

Development Environment: VS Code

Containerization: Docker (Planned)

Deployment: Cloud (Planned)


📂 Project Structure

IMS/
│── _pycache_/       # Compiled Python files  
│── bill/            # Billing-related files  
│── images/          # UI-related images  
│── ims.db           # SQLite database  
│── main.py          # Entry point of the application  
│── api/             # Flask API code  
│── config.py        # Configuration settings  
│── Dockerfile       # Docker container setup  
│── requirements.txt # Dependencies  
│── README.md        # Documentation

🚀 Features

✔ Add, update, delete products
✔ Search inventory items
✔ Generate invoices
✔ REST API for inventory operations
✔ Dockerized deployment (Coming Soon)

🏗 Setup & Installation

1. Clone the repository:

git clone https://github.com/your-repo-url.git
cd IMS


2. Create a virtual environment and install dependencies:

python -m venv venv  
source venv/bin/activate  # On Windows: venv\Scripts\activate  
pip install -r requirements.txt


3. Run the Flask backend:

python api/app.py


4. Run the Tkinter GUI:

python main.py



🐳 Docker Setup (Coming Soon)

Once Docker is implemented, you can build and run the application using:

docker build -t ims-app .  
docker run -p 5000:5000 ims-app

🎯 Future Enhancements

Implement role-based authentication

Deploy on a cloud platform

Improve UI/UX


🤝 Contributing

Feel free to contribute by submitting a pull request!

📜 License

This project is licensed under the MIT License.
