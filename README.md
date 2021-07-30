## Simple Timer for profiling function with multiple sections.

usage:

```python
t = Tictoctimer()
t.start()
t.tic('part1')
time.sleep(1)
t.toc('part1')
t.tic('part2')
time.sleep(2)
t.toc('part2')
t.pause()
print(t.percent()) #prints an overview like: part1 33.5%, part2 66.5%, others 0.0%
```