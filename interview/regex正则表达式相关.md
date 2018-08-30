## 正则表达式 re 模块

#### match()和search()的区别
> re模块中match(pattern,string[,flags]),检查string的开头是否与pattern匹配。
```
>>> re.match(r'super', 'superable super')
<_sre.SRE_Match object; span=(0, 5), match='super'>
>>> re.match(r'super', 'superable super').groups()
()
>>> re.match(r'super', 'superable super').group()
'super'
```
> re模块中re.search(pattern,string[,flags]),在string搜索pattern的第一个匹配值。
```
>>> re.search(r'super', 'superable super')
<_sre.SRE_Match object; span=(0, 5), match='super'>
>>> re.search(r'super', 'superable super').groups()
()
>>> re.search(r'super', 'superable super').group()
'super'
```
> 区别，match从头匹配，search搜索匹配。
```
>>> re.match(r'super', 'superstition')
<_sre.SRE_Match object; span=(0, 5), match='super'>

>>> re.search(r'super', 'superstition')
<_sre.SRE_Match object; span=(0, 5), match='super'>

>>> re.match(r'super', 'insuperable') == None
True

>>> re.search(r'super', 'insuperable')
<_sre.SRE_Match object; span=(2, 7), match='super'>

```




