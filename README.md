## 迭代说明 ##
### coSS_v1 ###
**problem**
* 无单元测试，模块划分不明确
* 翻译长句子被截断
* 占用剪贴板，覆盖其原始内容
  无剪贴板内容类型判断
* 按键时间过长导致重复执行
* 添加成功的反馈

### coSS_v2 ###
**solved**

* get text from clipboard
* send hotkey to system to get text from the global-field
* use busy waiting until release the key to prevent long time pressed 

**to solve**
* 翻译长句子被截断
* 添加成功的反馈（success + 译文 + 悬浮 2 秒）

### coSS_v3 ###
**TODO:**
* use database indexing by time and alphabetical

* 支持“删除”操作


## 最后搞 ##
用类似有道取词的方法，C++调用windows方法hook，编译成dll，python调用，写成第三方库。

## 放弃 ##
 * if os does not has clipboard list, save clipboard before copy 
 * judge if translation content is not text

