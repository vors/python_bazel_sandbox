# load("@aspect_rules_py//py:defs.bzl", "py_library", "py_pytest_main", "py_test")

# py_pytest_main(
#     name = "__test__",
#     deps = ["@pypi_pytest//:pkg"],  # change this to the pytest target in your repo.
# )

py_library(
    name = "project1",
    srcs = ["foo.py"],
    imports = [".",],
    visibility = ["//visibility:public"],
)

py_test(
    name = "project1_test",
    srcs = ["test_foo.py"] + ["//bazel:pytest.py"],
    main = "//bazel:pytest.py",
    deps = [":project1"],
    imports = ["."],
)
