# python_bazel_sandbox
Playing around with different python rules for bazel

## repro

```
bazel run //:main     
```

```
3.11.7 (main, Jan  7 2024, 14:26:33) [Clang 15.0.0 (clang-1500.1.0.2.5)]
/Users/sergei/.virtualenvs/venv/bin/python3
```

Expected
```
3.9.x
/something-in-bazel-sandbox
```
