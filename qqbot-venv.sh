# py3, env
sudo pip install virtualenv

mkdir ~/Py3Venv
cd ~/Py3Venv
virtualenv --python=python3 --no-site-packages qqbot-venv

# We source vars inside activate
cd qqbot-venv/bin/
source activate

# Install request, ssl trust, web framework
pip install -r requirements.txt

pip install qqbot

# 重新打开终端后，在使用 qqbot 和 qq 命令之前，需要运行：
# source ~/Py3Venv/qqbot-venv/bin/activate
