#flask模板工程

最近在学习python，然后呢，python的用处还很多，原来计划搞机器学习和数据挖掘的，不幸.....看到python可以开发后端，一时技痒，就学习了，当时从网上找了很多资料，还有就是当时要参加比赛，所以肯定是越快上手越好，越小越好，后来选择了flask，现在静下心来看《FlaskWeb开发：基于Python的Web应用开发实战》一书，首先第一个开源项目，当然是构建一个flask的大型架构模板咯。现在让我一一道来。



####一、启动

如果使用这个模板很简单，首先你需要下载源码（这是当然的），然后安装python2.7环境，对于linux用户，python2.7是标配的，windows需要根据版本下载python安装程序就好了。下面给出ubuntu下的python安装。

```bash
$sudo apt-get install python
```
然后需要安装依赖库，你也可以在虚拟环境中安装哦，这样更方便一点。
```bash
$sudo pip install -r requirements.txt
```
所有与环境相关的配置，都在**config.py**文件中，不过你不用修改它，因为这些配置信息都来自于系统的环境变量，你可以设置环境变量来大概修改配置的目的，同时满足了隐私。值得一提是，我们提供了一个脚本来自动的初始化配置信息和加载必要的环境变量，为了保护隐私，我给注释了但是使用者必须填写，具体操作在第八节，我先说明一下需要配置的环境变量。
```bash
# 加密密钥
#export SECRET_KE=
# 服务器绑定二级域名 端口 和过滤IP地址设置
#export WEBSERVER_HOST=
#export WEBSERVER_PORT=
export WEBSERVER_ACCESSIP=127.0.0.1
# 注册发送邮件服务器
#export MAIL_SERVE=
#export MAIL_SERVERPORT=
#export MAIL_USERNAME=
#export MAIL_PASSWORD=
#export MAIL_ADDR=
# Database地址
#export DEV_DATABASE_URL=
#export TEST_DATABASE_URL=
#export DATABASE_URL=
```
设置好后，可以直接运行**run.sh**进行测试（第八节），当然你也可以手动的把环境变量输入（这是必须的），然后直接运行manage.py脚本进行测试。
>最好的一个选择是，配置好run.sh下的环境变量，使用sudo执行，然后再进行下列命令，因为这时候系统已经保存有这些环境变量了。

```bash
$python manage.py runserver
```

这时候就可以完美访问你的服务器了，但是需要注意的是这时只能本机访问，如果需要外部计算机访问，可以添加参数，指定所有IP可访问，即0.0.0.0，同时可指定绑定的端口号。

```bash

$python manage.py runserver -h 0.0.0.0 -p 8000

 * Restarting with stat

 * Debugger is active!

 * Debugger pin code: 113-835-817

 * Running on http://0.0.0.0:8000/ (Press CTRL+C to quit)

```

如果需要更多功能选项，可以访问如下命令来查看。

```bash

$python manage.py runserver --help

```
值得一提是，模板实现了一个默认命令，也就是说直接执行：
```bash
$python manage.py
```
也可以运行服务器，而端口和可访问的ip段在**Config**类中定义，可以修改。

####二、在shell环境中使用flask和数据库

这个比较简单，在键入命令后，在后台模板会自动把app实例、sqlalchemy实例、数据库定义自动的加载到shell中，你可以在其中自由做测试，或者手动添加、修改数据库等。

```bash

$python manage.py shell

>>> app

<Flask 'app'>

>>> db

<SQLAlchemy engine='sqlite:///C:\\Users\\GalaIO\\Desktop\\GalaIO\\flask_pro\\data-dev.sqlite'>

>>> System

<class 'app.models.System'>

>>>

```

####三、使用数据库迁移工具

数据库迁移已经建立了一个基本版本，如果需要更新数据库模型，如果移动到新的部署环境，可以直接运行下面命令来同步数据库。

```bash
$python manage.py db upgrade
```

####四、修改配置文件

该结构框架提供了灵活的修改模式，如果添加一些配置项，可以添加在**Config**类中，如果想在生产环境和开发、测试环境使用不同的参数，需要在扩展类中进行修改，不过最通用的参数使用系统的环境变量。



这时一个从环境变量中引用密钥的例子，**or**的作用是在环境变量不起作用时，拥有替代方案。

```python

import os

SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess'

```

在配置文件可以同代项**app.config**字典中添加键值对，满足flask扩展库和全局通用量的需要，这些代码应写在如下：

```python

    @staticmethod

    def init_app(app):

		# you should write here

        pass

```

也就是说，我们的**SECRET_KEY**和**DATABASE_URL**默认从环境变量中引用，否则就使用默认字符串，或者在本地目录新建、寻找数据库。


同时我们还在Config中添加了，如下几个字段，由于配置生产环境时候，具体配置看8节。
```python
    HOST = 'blog.liketobe.cn'
    PORT = 8080
    ACCESSIPS = '127.0.0.1'
```

####五、增加模型

数据模型文件存在app目录下，添加数据模型很简单，只需要按照按照例子添加一个类就可以了，后台会自动完成，同时若想学习更多的**SQLalchemy**的**ORM**操作，可以访问<a href="http://www.sqlalchemy.org/support.html">SQLAlchemy官网</a>来获取资源。

```python

# test model

@addModel

class System(db.Model):

    name = db.Column(db.String(64), primary_key=True)

    def __repr__(self):

        return '<System %r>' % self.name

```

####六、模板与静态文件

**flask**会自动分发和处理对于**static**下的静态文件，一般包括**css**样式、**js**脚本、**img**图片等等。



**templates**目录下是所有的模板文件，由程序控制渲染展示给用户，这些都是flask的基础知识，这里不阐述，需要说明的是，我们提供了一个默认的根目录的模板**index.html**，还有常见错误类型**404.html**、**500.html**。如果想换成自己的样式，必须进行替换和更改，同时不影响你的其他创作。

####七、添加新的路由映射

模板提供了一个**index**路由的例子，可以先复制直接修改使用。值得提醒的是，可以把**errors**文件夹删除，因为他们定义的是全局的错误路由处理，主要修改的是**views.py**脚本，如果需要增加新的类声明的，在该文件夹下进行，最后当然需要在**__init__.py**中修改蓝图的名字，记得与包文件名一致，这些都是好的编码习惯哦。

####八、自动生成配置文件
使用python直接负责后台可能会有弊端，一般构造一个生产环境，现在是一个比较简单的，它会生成nginx和uwsgi的配置文件，这都是自动的，然后分别把配置文件放到相应的目录即可。更重要的是在其中会执行pip的依赖库备份，还有自动迁移和更新数据库。
```python
    # 利用bash命令删除所有的xml 和 conf文件，这些就是nginx和uwsgi的配置文件
    os.system('rm *-nginx.conf')
    os.system('rm *-uwsgi.xml')
    # 执行数据迁移和更新
    os.system('python manage.py db migrate')
    os.system('python manage.py db upgrade')
    # 执行角色更新
    Role.insert_roles()
    # 自动更新需求库
    os.system('pip freeze > requirements.txt')
```
命令执行如下：
```bash
$python manage.py conf
```
执行上述命令就会发现在本地目录出现一个****-nginx.conf和****-uswgi.xml两个文件，现在你需要电脑安装好这两个程序，一个是反向代理服务器nginx，另一个是python的通用网关接口uwsgi。安装命令如下：
```bash
$sudo apt-get install nginx
$sudo apt-get install uwsgi
```
把****-nginx.conf移动到nginx的配置文件，并且重新加载nginx的配置。
```bash
$sudo cp ./****-nginx.conf /etc/nginx/con.f/
$sudo /usr/sbin/nginx -s reload
```
启动uwsgi服务器，并手动设置log文件。
```bash
$sudo uwsgi -x ****-uwsgi.xml -d ./****.log
```
这样就简单搭建了生产环境。
>值得一提：我们提供了run.sh和exit.sh的脚本，用于自动运行和退出。
>

####九、添加新的库

在开发中往往需要添加新的库，但是需要说明的一点，希望大家进入虚拟环境中，使用pip安装，安装环境也打包了，当然这是windows上的虚拟环境，因为在虚拟环境安装会默认安装到**venv/Lib/site-packages/**中，我们程序每次动态吧改路径链入我们的库搜索路径，所以可以直接运行，就像步骤一说的一样。



如果安装了新的库，记得更新一下依赖库列表哦。运行如下命令。

```bash

$pip freeze > requiremwnts.txt

```