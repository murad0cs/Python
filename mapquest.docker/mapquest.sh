#! /bin/bash

mkdir mytempdir

cp mapquest.py mytempdir/.

echo "FROM python" >> mytempdir/Dockerfile
echo "RUN pip install requests" >> mytempdir/Dockerfile

echo "COPY  mapquest.py /home/mymapquest/" >> mytempdir/Dockerfile

echo "CMD python3 /home/mymapquest/mapquest.py" >> mytempdir/Dockerfile

echo "ENTRYPOINT [\"python3\"]"

cd mytempdir
docker build -t mysampleapp .

docker run -t --name mydevapp mysampleapp
docker ps -a