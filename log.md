# 更新日志

## Beta 3

### 描述

Beta3版本，用户将不用再调用底层模块了，修改了导入模块的逻辑：

**例子-新旧版本的导入io操作**:

**Beta_2**
```javascript
using io
```

**Beta_3**
```javascript
import plum::io
```

### 添加

- 添加`import`语句。
- 添加`object`关键字，用于创建对象。
- 添加`class`关键字，用于创建类。
- 添加`stc`关键字，用于创建类中方法。

### 热修复

- 修复了`stc`相关功能出现的有关`No match found.`的错误。