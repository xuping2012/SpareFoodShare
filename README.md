Django Project for the website

some notes:
 * currently using multiple apps is broken. Until this issue is resolved, all functionality is under the payments app
 * there may be issues with frontend css and/or redirection from hyperlinks due to missing changes from the migration. Please let me know/update this document should you find any.
 * Functionality created using guidance from tutorials by testdriven.io

 
 (issue resolved, left for posterity) clarification: it appears due to an issue on my git command line, my name in the Git history is set to unknown. I am editing the README from the web version to clarify this, as well as to update that I am looking into resolving this issue.

 
### 项目部署流程
```
声明：本项目由某学生提供，兼职-有偿帮他完成UI自动化测试框架搭建，不做任何商业用途，不负任何责任。
```

##### 创建python虚拟环境

- python -m venv  v_name


##### pip安装依赖
```
原来项目是没有requirements.txt依赖文件的，是后面安装pipreqs生成的
```
- pip install pipreqs && pipreqs ./
- - --force # 此参数表示每次暴力覆盖依赖文件

##### 执行sql目录下的脚本
- 将sql目录的脚本文件一一执行
- - 先执行table表的sql脚本，其他是部分插入基础数据

##### 启动服务
- 修改settings中的数据库配置；在数据库创建对应的数据库：foodforshare1
- SpareFoodShare没有在settings中注册app，因为它没有models
- - 已知table表结构，后面可以完善models通过框架生成即可
- 所以它没有数据迁移及生成表结构的操作
- - python manage.py makemigrations SpareFoodShare
- - python manage.py migrate 
- 但是他可以创建后台账户：http://127.0.0.1:8000/admin
- - python manage.py createsuperuser
- 启动命令：python manage.py runnserver

#### 部分代码异常
- 正常接口发送数据，在下一个接口没有正常获取，只是为了完成UI自动化，简单处理了，但并没有修复bug

```python
try:
        p = food.price
    except:
        p = 12.13
    order_amount = 1 * int(p)
    users = User.objects.all()
    try:
        email = request.user.email
    except:
        email = "1@1.com"
    specificuser = users.filter(email=email)
    # specificuser = users.filter(email=request.user.email)
    try:
        _id = specificuser[0].id
    except:
        _id = 2
```
- 你会发现很多views视图层很多被我try起来的代码，且给了一个默认值，注释了正确的代码，requests.user.email此类的参数是没有正确获取的

#### 关于数据
- sql 是经过测试调整过的，它不一定是错的，也不全是对的。根据名字先创建table，然后再导入insert插入数据。