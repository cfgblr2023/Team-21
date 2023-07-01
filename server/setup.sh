echo "Installing Node Modules"
cd frontend
npm install
echo "Node Modules Installed"


echo "Configuring Virtual Environment for the backend"
cd .. 
cd backend
python -m venv venv
source venv/bin/activate
echo "Installing Python Modules"
pip install -r requirements.txt
deactivate
echo "Python Environment Created and Deactived"

cd bloglite
touch .env
echo "Configuring .env file"
echo "COMMON_DB=sqlite:///bloglite.db" >> .env
echo SECRET_KEY =  "ash ah secet" >> .env

echo 
echo "Use run.sh to run the application"