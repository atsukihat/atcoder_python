FROM python:3.10.2

ARG USERNAME=vscode
ARG GROUPNAME=${USERNAME}
ARG USER_UID=1000
ARG USER_GID=${USER_UID}

RUN apt-get update \
    && groupadd --gid ${USER_GID} ${GROUPNAME} \
    && useradd -s /bin/bash --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME} \
    && apt-get -y install sudo \
    && echo ${USERNAME} ALL=\(ALL\) NOPASSWD:ALL > /etc/sudoers.d/${USERNAME} \
    && chmod 0440 /etc/sudoers.d/${USERNAME}

# Python3, PyPy3の環境想定
RUN apt-get update && \
    apt-get install -y python3-pip pypy3 nodejs npm

# pythonライブラリをインストール
COPY requirements.txt /tmp/
RUN python -m pip install --upgrade pip

RUN pip install -r /tmp/requirements.txt


# コンテスト補助ツールをインストール
RUN pip3 install online-judge-tools
RUN pip install aclogin
RUN npm install -g atcoder-cli

# AtCoderの単位表記変更に対応した修正
RUN sed -i \
    -e 's/(KB|MB)/(KiB|MiB)/g' \
    -e "s/if memory_limit_unit == 'KB':/if memory_limit_unit == 'KiB':/g" \
    -e "s/elif memory_limit_unit == 'MB':/elif memory_limit_unit == 'MiB':/g" \
    /usr/local/lib/python3.10/site-packages/onlinejudge/service/atcoder.py

# AtCoder用エイリアスを.bashrcに追加
RUN echo "# AtCoder aliases" >> /home/${USERNAME}/.bashrc && \
    echo "alias test='oj t -c \"pypy3 main.py\" -d ./tests/'" >> /home/${USERNAME}/.bashrc && \
    echo "alias test2='oj t -c \"python3 main.py\" -d ./tests/'" >> /home/${USERNAME}/.bashrc && \
    echo "alias sb='acc s -- main.py --language 5078'" >> /home/${USERNAME}/.bashrc && \
    echo "alias sb2='acc s -- main.py --language 5055'" >> /home/${USERNAME}/.bashrc && \
    echo "alias c='cd contest'" >> /home/${USERNAME}/.bashrc && \
    echo "alias o='code main.py'" >> /home/${USERNAME}/.bashrc && \
    echo "alias d='python main.py'" >> /home/${USERNAME}/.bashrc