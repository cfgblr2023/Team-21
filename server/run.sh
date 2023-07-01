echo "Running the backend server"

cd backend
source venv/bin/activate

# check for the .flaskenv file 
if [ ! -f .flaskenv ]; then
    echo "FLASK_APP=app.py" >> .flaskenv
    echo "FLASK_ENV=development" >> .flaskenv
    echo "FLASK_DEBUG=1" >> .flaskenv
    echo "FLASK_RUN_PORT=5050" >> .flaskenv
    echo "FLASK_RUN_HOST=0.0.0.0" >> .flaskenv
    echo "Environment variables set"
else 
    echo "Environment variables already set"
fi

cd static/
mkdir -p image_data

flask run 

deactivate