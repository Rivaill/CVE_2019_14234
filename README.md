# CVE_2019_14234

`python 2.7.x` `CentOS7`

- install python 2.7

    ```
    curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
    python get-pip.py
    yum install gcc openssl-devel bzip2-devel python-devel -y
    ```
- install postgres via docker

    ```
    curl -sSL https://get.docker.com/ | sudo sh
    usermod -aG docker root
    systemctl start docker

    docker run --name some-postgres -e POSTGRES_USER=root -e POSTGRES_PASSWORD=minhkma -e POSTGRES_DB=test -p 5432:5432 -d postgres
    ```

- Install and setup django to PoC

    ```bash
    pip install requirements.txt
    ```

    ```bash
    vim app/settings.py # update DATABASES
    ```

    ```bash
    python manage.py migrate
    ```

- PoC

    ```bash
    python PoC.py
    ```

- output 

    ```
    [root@grafana CVE_2019_14234]# python PoC.py 
    /usr/lib/python2.7/site-packages/requests/__init__.py:91: RequestsDependencyWarning: urllib3 (1.25.3) or chardet (2.2.1) doesn't match a supported version!
    RequestsDependencyWarning)
    Vulnerability!
    ```
