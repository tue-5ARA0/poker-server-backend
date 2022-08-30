import os 

# Initialise GRPC protocol files
os.system("python -m grpc_tools.protoc --proto_path=./ --python_out=./ --grpc_python_out=./ ./proto/game/game.proto")
# Apply migrations
os.system("python manage.py makemigrations coordinator --settings=configurations.dev.settings")
os.system("python manage.py makemigrations --settings=configurations.dev.settings")
os.system("python manage.py migrate coordinator --settings=configurations.dev.settings")
os.system("python manage.py migrate --settings=configurations.dev.settings")