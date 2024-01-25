load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

SHA="d70cd72a7a4880f0000a6346253414825c19cdd40a28289bdf67b8e6480edff8"

VERSION="0.28.0"

http_archive(
    name = "rules_python",
    sha256 = SHA,
    strip_prefix = "rules_python-{}".format(VERSION),
    url = "https://github.com/bazelbuild/rules_python/releases/download/{}/rules_python-{}.tar.gz".format(VERSION,VERSION),
)

load("@rules_python//python:repositories.bzl", "python_register_toolchains")

python_register_toolchains(
    name = "python311",
    python_version = "3.11",
)

# http_archive(
#     name = "aspect_rules_py",
#     sha256 = "e1d1023bc9ba8545dc87c6df10508d9d7c20f489f5e5c5c1e16380b33c013485",
#     strip_prefix = "rules_py-0.5.0",
#     url = "https://github.com/aspect-build/rules_py/releases/download/v0.5.0/rules_py-v0.5.0.tar.gz",
# )
# # Fetches the rules_py dependencies.
# # If you want to have a different version of some dependency,
# # you should fetch it *before* calling this.
# # Alternatively, you can skip calling this function, so long as you've
# # already fetched all the dependencies.
# load("@aspect_rules_py//py:repositories.bzl", "rules_py_dependencies")
# rules_py_dependencies()
