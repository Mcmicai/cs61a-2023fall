import schemdraw
import schemdraw.elements as elm

# 创建一个新的绘图
d = schemdraw.Drawing()

# 4选1选择器
mux = d.add(elm.Multiplexer(inputs=['I3', 'I2', 'I1', 'I0'], outputs=['F'])
            .label('4x1\nMUX'))

# 添加输入信号
d.add(elm.Line().left().length(d.unit/2))
d.add(elm.Dot())
d.push()
d.add(elm.Line().up().length(d.unit/2))
d.add(elm.SourceControl().label('A', loc='top'))
d.pop()
d.add(elm.Line().down().length(d.unit/2))
d.add(elm.SourceControl().label('B', loc='bottom'))

# 输入信号 C 和 非C
d.add(elm.Line().at(mux.I0).left().length(d.unit/2))
d.push()
d.add(elm.Line().up().length(d.unit/4))
d.add(elm.SourceControl().label('C', loc='top'))
d.pop()
d.add(elm.Line().down().length(d.unit/4))
d.add(elm.Dot().label('I0, I1'))

d.add(elm.Line().at(mux.I2).left().length(d.unit/2))
d.push()
d.add(elm.Line().up().length(d.unit/4))
d.add(elm.SourceControl().label('C', loc='top'))
d.pop()
d.add(elm.Line().down().length(d.unit/4))
d.add(elm.Dot().label('I2, I3'))

# 输出
d.add(elm.Line().at(mux.F).right().length(d.unit/2))
d.add(elm.Dot().label('F'))

# 画图
d.draw(show=True) 

