#! /bin/bash

echo "Installing pyenv"
yum install -y epel-release
yum install -y git gcc gcc-c++ patch make zlib-devel bzip2-devel readline-devel sqlite-devel openssl-devel
curl -L https://raw.github.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

echo 'export PATH="/root/.pyenv/bin:$PATH"' >> /root/.bash_profile
echo 'eval "$(pyenv init -)"' >> /root/.bash_profile
echo 'eval "$(pyenv virtualenv-init -)"' >> /root/.bash_profile
source /root/.bash_profile

echo "Installing Python 2.7.7 and virtualenv"
pyenv install 2.7.7
pyenv virtualenv 2.7.7 python2

echo "Installing Python 3.5.5 and virtualenv"
pyenv install 3.5.5
pyenv virtualenv 3.5.5 python3
