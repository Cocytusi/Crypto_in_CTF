# 2020网鼎杯——you_raise_me_up wp
2020年第二届网鼎杯，密码学you_raise_me_up，这道题是一个离散对数问题。

原题如下：

```
from Crypto.Util.number import *
import random n = 2 ** 512
m = random.randint(2, n-1) | 1
c = pow(m, bytes_to_long(flag), n)
print 'm = ' + str(m)
print 'c = ' + str(c)
```

重点就在 `c = pow(m, bytes_to_long(flag), n)` 这个式子。

意思是 mflag ≡ c (mod n)，即 `m` 的flag次方模 `n` 得 `c` ，

其中参数 `m` ， `n` 和 `c` 都是已知的， 唯一的未知参数就是我们要找的flag。

而离散对数就是求解这样一类问题：

> ax ≡ b (mod m)  

> 求解x  

因此这道题是一个标准的离散对数问题，求解离散对数可以使用python的sympy库。

SymPy是用于符号数学的Python库，可以完成多种数学计算问题，例如多项式求值、求极限、解方程、求积分、微分方程、级数展开、矩阵运算、离散数学等等。

使用sympy库中的discrete_log函数。

discrete_log()使用示例：

```
>>> from sympy.ntheory import discrete_log
>>> discrete_log(41, 15, 7)
3
```

即是 73 ≡ 15 (mod 41)

可知函数discrete_log(x,y,z)中，x是模数，y是余数，z是底数，返回值就是要求的指数。

由此我们可使用python来解题，代码如下：

```
from sympy.ntheory import discrete_log
n = 2**512
m = 391190709124527428959489662565274039318305952172936859403855079581402770986890308469084735451207885386318986881041563704825943945069343345307381099559075
c = 6665851394203214245856789450723658632520816791621796775909766895233000234023642878786025644953797995373211308485605397024123180085924117610802485972584499
flag_dec = discrete_log(n,c,m) print(hex(flag_dec))
```

得到flag的十六进制值为：
`0x666c61677b35663935636139332d313539342d373632642d656430622d6139313339363932636234617d`

然后将这个hex值转为ascii，直接使用python的binascii库，binascii库中的a2b_hex函数将一个hex字符串转为ascii字符串。

这里注意要将前面的0x去掉，

如下:

![](you_raise_me_up%20wp/2020072420540056.png)
得到flag:

`flag{5f95ca93-1594-762d-ed0b-a9139692cb4a}`


[2020网鼎杯——you_raise_me_up wp](https://blog.csdn.net/qq_43531895/article/details/106108139)