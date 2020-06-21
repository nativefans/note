# 1.HTML、css、JS的作用
HTML是一套规则，是浏览器认识的规则。HTML可以类比成人的身体，组成人身体的各个部位的就是各种标签（要掌握的标签有20个左右）。而css是对网站标签的修饰作用，可调整HTML标签的颜色、位置、大小等属性，相当于给一个人穿上衣服（此时HTML+CSS就可实现一个静态页面了）。要想使这个人动起来就需要Javascript（简称JS），即实现动态页面。

# 2.HTML要点

    1、开发者：学习Html规则
    开发后台程序：
        -  写Html文件（充当模板的作用）
        -  数据库获取数据，然后替换到html文件的指定位置（web框架）
    2、本地测试
        -  找到文件路径，直接浏览器打开
        -  pycharm打开测试
    3、编写Html文件
        -  doctype对应关系
        -  html标签，标签内部可以写属性 ，html标签只能有一个
        -  注释： <!--   .........   -->
    4、标签分类
        -  自闭合标签:
        <meta charset="UTF-8">
        -  主动闭合标签(多数)：
        <title>Title</title>
        
  ## HTML标签（注：标签中大小写不区分）
  ### head标签中:
   1. Meta ：自闭合标签（自闭合标签最好加上斜杠作区分）
        1. 页面编码
        ```
        <meta charset="UTF-8" />
        ```
        2. 刷新和跳转(不常用，一般用js)
        ```
        <meta http-equiv="Refresh" content="30" />
        <meta http-equiv="Refresh" content="30;url=https://yande.re" />
        ```
        3. 关键词(用于搜索自己网站，爬虫)
        ```
        <meta name="keywords" content="meaqua" />
        ```
        4. 描述
        ```
        <meta name="descrption" content="........" />
        ```
        5. X-UA-Compatible ---
        与IE浏览器的兼容有关
        ```
        <meta http-equiv="X-UA-Compatible" content="IE=IE9;IE=IE8;IE=IE7;" />
        ```

   2. Title标签
   3. icon:小图标 
   ```
    <link /> 
    <link rel="shortcut icon" href="image/favicon.ico" />
   ```
    
   4. css
   ```
   <style />
   ```
   5. JS
   ```
   <script />
   ```

### body标签中:
- 所有标签分为：块级标签（占一整行），行内标签（内联标签，只占自身内容部分）
- 块级标签：H标签（加大加粗）、p标签（段落和段落之间有间距）、div标签（白板）
- 行内标签：span标签（白板，什么特性都没有，可通过CSS变成任何特性的标签）
- 标签之间可以嵌套
- 标签存在的意义，定位(css)操作方便，js操作方便
------------------

1. 图标
```
空格:&nbsp;
<:&lt;
>:&gt;
...符号代码
```
2. p标签：做段落，段落直接有间距,但是<br />(换行)之后是没有间距的

3. h标签:从h1到h6（由大到小）- 重点

4. span标签（白板）- 重点

5. div标签（白板）- 非常重要

6. input + form(传输数据到后台) - 重点

        input type="text" -name属性 value='默认值'
        input type="password" -name属性
        input type="submit" - value='提交' 提交按钮，表单
        input type="button" - value='登陆'按钮

        input type="radio" - value, name属性（name相同则互斥），单选框, checked='checked'（默认值）
        input type="checkbox" - value, name属性（批量获取数据），复选框, checked='checked'
        input type="file" - 依赖form表单一个属性，enctype="multipart/form-data"
        input type="reset" - 重置

        textarea - <textarea name="属性名" >默认值</textarea>

        select - selected="selected"默认值 multiple="multiple"多项 size="5"显示行数 optgroup label="..."分组组名（不可选）

7. a标签： - 重点
 - 跳转
 - 锚 href='#某个标签的ID' 标签的ID不允许重复
 - target - _blank:以新页面打开
 
8. img标签： - 重点
```
<img src="url或路径" title="..." style="height: ...px;width: ...px;" alt="鼠标停留时出现的title">
```
可用a标签包含使图片成为超链接

9. 列表标签：
    - 圆点:
          <ul>+<li>
     ```
     <ul>
        <li>loli</li>
        <li>loli</li>
        <li>loli</li>
        <li>loli</li>
    </ul>
    ```

    - 数字：
           <ol>+<li>
    ```
    <ol>
        <li>lolikon</li>
        <li>lolikon</li>
        <li>lolikon</li>
        <li>lolikon</li>
    </ol>
    ```

    - 标题+内容形式：
           <dl>+<dt>标题/<dd>内容
     ```
    <dl>
        <dt>ttt</dt>
        <dd>ddd</dd>
        <dd>ddd</dd>
        <dd>ddd</dd>
        <dd>ddd</dd>
    </dl>
    ```

10. 表格：
        <table>+<tr>行+<td>列 - 重点
     ```
    <table border="1">
        <tr>
            <td>1,1</td>
            <td colspan="2"> 横向占两格，rowspan="2"：纵向占两格,被占的单元格除去
                <a href="1.jpg">
                    查看
                </a>
                <a href="#"> #号可回到主页最前
                    修改
                </a>
            </td>
        </tr>
        <tr>
            <td>2,1</td>
            <td>2,2</td>
            <td>2,3</td>
        </tr>
    </table>
    ```
    
11. label
        用于点击文字，使得关联的标签获得光标
 ```
<label for="username">username:</label>
<input id="username" type="text" name="user">
```
12. fieldset
        文本框,legend可加文字

# 3.CSS样式

编写css样式：
1. 标签的style属性
2. 写在head里面的style属性
    - id选择器(少用)：
    ```
        #i1{
        background-color: rebeccapurple;
        height: 80px;
        }
    ```
    - class选择器：(常用)
    ```
        .c1{
        background-color: hsla(60, 100%, 52%, 0.4);
        height: 50px;
        }
    ```
    - 标签选择器：
    ```
        span{
        background-color: aqua;   背景色
        color:black;    字体颜色
        }
    ```
    - 层级选择器(空格):(常用)
    ```
        .c1 .c2 div{

        }
     ```
    - 组合选择器(逗号):(常用)
    ```
        #i1,.c2,div{

        }
     ```
    - 属性选择器:(常用)
            对选择到的标签再对属性进行一次筛选
      ```
        .c1[n='Alex']{

        }
        ```
    - 优先度：标签上style优先，编写顺序：就近原则
3. css样式也可以写在单独css文件中
        html文件引用：
    ```
    <link rel="stylesheet" href="common.css">
    ```
4. css的注释 
        /*  ....  */

5. 样式
        border - 宽度，样式，颜色
        height - 高度 像素，百分比
        width - 宽度 像素，百分比
        text-align:center - 水平方向居中
        line-height - 垂直方向根据标签高度
        color - 字体颜色
        font-size - 字体大小
        font-weight - 字体加粗
6. float
        让标签飘起来，使得块级标签也可以堆叠
```
    <div style="clear:both;"></div>
```
7. display

        display:none - 让标签消失（js会用到）
                
        display:inline; - 行内
        display:block; - 块级
        display:inline-block; - 默认自己有多少占多少，且可以设置高度，宽度，边距
            
    PS:行内标签：无法设置高度，宽度，边距
       块级标签：可以设置高度，宽度，边距

8. padding,margin 
        padding - 内行距
        margin - 外行距
        margin:auto - 留出空隙自动居中


