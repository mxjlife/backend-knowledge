# git操作
> 如何使用git

## 配置

### 安装git

### 生成ssh key

### 初始设置

## 常用命令

### 提交

### 分支操作 branch

### 合并 

### 查看状态 status 

### 标签 tag

### 回退

### 开发中遇到的场景

## Git开发规范

### 分支开发流程
一般来说正式项目都会有2个保护分支,不允许直接提交代码,只允许提交merge request:
* master  release分支,用来进行线上的发布,一般版本号为release-x.x.x或x.x.x
* develop  snapshot分支,拉取开发分支,测试功能等,一般版本号为x.x.x-SNAPSHOT

#### 一般的分支开发步骤:
1. 从develop分支拉取开发分支,一般命名规则为: 开发人-功能 (单词用下划线分隔)
2. 在开发分支上开发完成后,在本分支上进行自测,或将此分支部署到开发环境自测
3. 自测完成后提交mr(merge request)到develop分支,走提测流程让测试人员测试(一般会在develop创建tag,部署tag到测试环境)
4. 如有修改则继续在原来的开发分支修改,修改后再提交mr
5. 测试通过后, 从develop拉取release分支(命名:release-x.x.x),修改版本号为正式版本号(如果不确定master分支与develop分支是否同步,此时可以先将master分支合并到此release分支),若需要deploy可在此时进行打包,push分支后提交mr将此release分支合并到master。注（也可以直接修改develop分支版本号然后合并到master,但不推荐）
6. 合并到master分支后,将master部署到preview环境进行验证,或者线上小流量灰度验证
7. 全量上线, 上线完成后在master分支打tag记录上线commit并删除无用分支
8. 合并到master后从master拉取snapshot分支(命名:snapshot-x.x.x),修改版本号(升级数字版本号,添加SNAPSHOT后缀),此时可以打snapshot包,提交mr将snapshot分支合并到develop。注（也可以直接修改develop分支版本号,但不推荐）
9. 将snapshot合并到develop分支, 删除无用分支

#### hotfix开发步骤:
1. 从master拉取hotfix分支(命名:hotfix-缺陷描述)
2. 修复缺陷, 并自测
3. 将hotfix分支部署到preview分支进行验证
4. 提交mr到将hotfix分支合并到master(hotfix无需修改版本号)
5. 将master部署到preview环境进行验证,或者线上小流量灰度验证
6. 全量上线, 上线完成后在master分支打tag记录上线commit并删除无用分支
7. 合并master到develop分支(注意master与develop分支版本号都保持原来的即可)

### 操作规范
1. 禁止在master分支上直接开发,必须通过创建新分支来进行开发
2. 未经过测试的代码不得合并到master
3. 合并到develop分支的代码必须确保无报错并可以正常编译部署
4. 多分支开发时开发分支只能与maser与develop分支合并,尽量不要进行开发分支之间的合并
5. 提交mr前确保无冲突, 如果develop分支已经发生了变更,应先将develop分支合并到自己的分支并验证无问题后再提交mr
6. 解决冲突代码时禁止再master与develop分支操作,如果无把握也不要在自己的开发分支操作,可以从开发分支创建新分支解决冲突,无问题后再合到自己的开发分支
7. 关键节点创建tag,方便回溯
