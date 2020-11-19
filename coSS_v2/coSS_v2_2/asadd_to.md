| 原文 | 译文 |
| :---- | ---- |
| make a macro which will expand into a regular statement, not into a compound statement. | 创建一个宏，它将展开为一个常规语句，而不是一个复合语句。 |
| This is done in order to make the use of function-style macros uniform with the use of ordinary functions in all contexts. | 这样做是为了在所有上下文中使函数式宏的使用与普通函数的使用一致。 |
| This will compile and work as expected, but this is not uniform. The more elegant solution is to make sure that macro expand into a regular statement, | 这将按照预期进行编译和工作，但这不是统一的。 |
