1. 这个是用来自动给奇石配座的代码
2. 输入的底座和奇石图片的背景都必须比较干净
3. 底座的处理：
    a.首先选择底座入口的两个点
    b.然后图片自动竖直
    c.将生成的图片和两个入口点保存到本地模型
4. 配座阶段：
    a. 首先制定石头最下面的两个边缘点
    b. 将两个边缘点和底座的边缘点重合
    c. 将重合之后的图片保存下来