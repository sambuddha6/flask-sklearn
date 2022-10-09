ssh-keygen -t rsa
cat /home/sambuddha/.ssh/id_rsa.pub

git clone git@github.com:sambuddha6/flask-sklearn.git

python3 -m venv ~/.flask-sklearn
source ~/.flask-sklearn/bin/activate

cd flask-sklearn

python -V
wget https://repo.continuum.io/miniconda/Miniconda3-4.5.4-Linux-x86_64.sh
sh Miniconda3-4.5.4-Linux-x86_64.sh -u
export PATH=~/miniconda3/bin:$PATH
python -V

make all

az webapp up -n flask-ml-service01

chmod 744 make_predict_azure_app.sh
./make_predict_azure_app.sh

az webapp log tail

git status

git add Makefile
git add requirements.txt
git add app.py
git add test_app.py

git commit -m "Changes made for successful run"

git config --global user.email "sambuddha6@gmail.com"
git config --global user.name "Sambuddha"

git commit -m "Changes made for successful run"
git push
