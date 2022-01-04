## 标题
### 分级标题
标题可以使用#实现, 也可以使用 html中的标题标签,标签的好处是指定id后方便跳转到此处

```
<h4 id='1.1.1'> html标题 </h4>

# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题  <!--最多6级标题-->
```
<h4 id='1.1.1'> html标题 </h4>

# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题

### 任务列表
```
- [ ] 任务一 未做任务
- [x] 任务二 已做任务
```
- [ ] 任务一 未做任务
- [x] 任务二 已做任务

### 有序列表
有序列表可以使用 数字+点+空格 来实现, 数字相同也不影响
```
1. 列表1
    1. 列表1.1
        1. 列表1.1.1
   1. 列表1.2
2. 列表2
3. 列表3
```
1. 列表1
    1. 列表1.1
        1. 列表1.1.1
    1. 列表1.2
2. 列表2
3. 列表3

### 无序列表
无序列表可以使用 * ,+, - 空格来实现
```
* 列表1
  * 列表1.1
    * 列表1.1.1
  * 列表1.2
* 列表2
* 列表3
---
+ 列表1
    + 列表1.1
        + 列表1.1.1
  + 列表1.2
+ 列表2
+ 列表3
---
- 列表1
    - 列表1.1
        - 列表1.1.1
    - 列表1.2
- 列表2
- 列表3
```
* 列表1
  * 列表1.1
    * 列表1.1.1
  * 列表1.2
* 列表2
* 列表3
---
+ 列表1
    + 列表1.1
        + 列表1.1.1
  + 列表1.2
+ 列表2
+ 列表3
---
- 列表1
    - 列表1.1
        - 列表1.1.1
    - 列表1.2
- 列表2
- 列表3

## 字体
```
*斜体*
_斜体_
**加粗**
***加粗斜体***
markdown 原生不支持下划线/字体颜色/背景色等,可以使用html语法实现
<span style="border-bottom:1px dashed black;">下划线</span>
<span style="color:red;">字体颜色</span>
<span style="background:#5151A2;">背景颜色</span>
```
*斜体*
_斜体_

**加粗**

***加粗斜体***

~~删除线~~

<span style="border-bottom:1px dashed black;">下划线</span>

<span style="color:red;">字体颜色</span>

<span style="background:#5151A2;">背景颜色</span>

### 角标
```
角标
H<sub>2</sub>O  CO<sub>2</sub>
C<sup>60</sup>
```
H<sub>2</sub>O  CO<sub>2</sub>
C<sup>60</sup>

### <span id="1">测试跳转</span>

## 分隔线
三个 -/*/_ 都可以实现分隔线
```
---
***
___
```
---
***
___

## 引用

```
>引用此文本
>> 文本内二级引用 
```
>引用此文本
>> 文本内二级引用 

## 代码块
使用前后各三个` 来标识是代码块
```
    public void test(){
        print("success")
    }
```

## 链接
### 行内式：
[]里写链接文字，()里写链接地址, ()中的""中可以为链接指定title属性，title属性可加可不加
```
[行内式](https:://github.com "行内式")
```
[行内式](https:://github.com "行内式")

#### 锚点(页内链接)
需要指定要跳转到的标题的id
```
[页内跳转](#1)
```
[页内跳转](#1)

### 参考式：
适用于链接在文章中多处使用, 或是论文引用等, 引用可以放到文本最下方,方便管理
```
[参考式1][1]
[参考式2][2]
[1]:https:://github.com "参考式1"
[2]:https:://github.com "参考式2"
```
[参考式1][1]

[参考式2][2]

[1]:https:://github.com "参考式1"
[2]:https:://github.com "参考式2"

注意：上述的`[1]`,`[2]`信息不出现在内容中


## 插入图片

```
![github](resources/1.jpg)
![github](https://raw.githubusercontent.com/mxjlife/static/main/1.jpg)

文件居中
<div align="center">
<img src="https://raw.githubusercontent.com/mxjlife/static/main/1.jpg" width="100" height="100">
</div>

<div align="center">
![github](resources/1.jpg)
</div>

```

![github](resources/1.jpg)

![github](https://raw.githubusercontent.com/mxjlife/static/main/1.jpg)

文件居中
<div align="center">
<img src="https://raw.githubusercontent.com/mxjlife/static/raw/main/1.jpg" width="100" height="100">
</div>

<div align="center">

![github](resources/1.jpg)

</div>

## 表格
第一行为表头，第二行分隔表头和主体部分，第三行开始每一行为一个表格行。
列于列之间用管道符|隔开。
第二行可以为不同的列指定对齐方向。默认为左对齐，:---: 中心对齐，---: 右对齐

```
|学号|姓名|年龄|
|---:|:---|:---:|
|1|小明|5|
|2|小王|79|
|245|张小四|192|
```
|学号|姓名|年龄|
|---:|:---|:---:|
|1|小明|5|
|2|小王|79|
|245|张小四|192|
