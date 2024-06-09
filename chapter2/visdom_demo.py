import torch
import visdom

# 创建一个 Visdom 实例，并指定环境名称为 'first'
vis = visdom.Visdom()

# 检查服务器连接是否成功
assert vis.check_connection(), "无法连接到 Visdom 服务器。请确保服务器已启动并在运行。"

# 在窗口 'text1' 中显示文本 'first visdom'
vis.text('first visdom', win='text1')

# 在相同的窗口 'text1' 中追加显示文本 'hello PyTorch'
vis.text('hello PyTorch', win='text1', append=True)

# 使用一个循环生成并绘制抛物线曲线 y = -x^2 + 20x + 1
for i in range(20):
    X = torch.FloatTensor([i])
    Y = torch.FloatTensor([-i**2 + 20*i + 1])
    vis.line(X=X, Y=Y, opts={'title': 'y=-x^2+20x+1'}, win='loss', update='append' if i > 0 else None)

# 在窗口 'random_image' 中显示一个随机生成的 3x256x256 图像
vis.image(torch.randn(3, 256, 256), win='random_image')

print("所有数据已发送到 Visdom，请在浏览器中查看 http://localhost:8097")
