import visdom
import numpy as np

# 创建一个 Visdom 实例
vis = visdom.Visdom()

# 检查服务器连接是否成功
assert vis.check_connection(), "无法连接到 Visdom 服务器。请确保服务器已启动并在运行。"

# 生成数据
X = np.linspace(-10, 10, 100)
Y = np.sin(X)

# 绘制正弦曲线
vis.line(
    Y=Y,
    X=X,
    opts=dict(
        title='Sine Wave',
        xlabel='X-axis',
        ylabel='Y-axis',
        markers=False
    )
)

print("正弦曲线已绘制，请在浏览器中查看 http://localhost:8097")
