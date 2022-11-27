# progressBar
使用python裝飾器，加入prettytable套件顯示table
## 使用方式：
```python=
@progressBar_decorator('dummyLoop')
def dummyLoop():
    nb_iter = 13
    for i in range(nb_iter):
        time.sleep(0.1)
        yield (i + 1),nb_iter
    return f"completed={i+1}/{nb_iter}"
```
## Outputs:
```
The dummyLoop starts at 2022-11-27 05:44:29 .
dummyLoop = 100.0% [####################] 13/13 1.4s FPS=9.6
The dummyLoop ends at 2022-11-27 05:44:30 .
+-------+----------+---------+-----+
| Total | Progress | Time(s) | FPS |
+-------+----------+---------+-----+
|   13  |   1.0    |   1.4   | 9.6 |
+-------+----------+---------+-----+
result: completed=13/13
```
