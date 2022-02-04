from player import Player

Player.set_cls_field(10)
x = Player()
print(x.lvl)

Player.set_cls_field(1)
y = Player()
print(y.lvl)

y.lvl = 2.3 #should error