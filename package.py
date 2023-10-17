name = "zimg"

# Remember to modify the commands function here
version = "3.0.5.sse.1.0.0"

authors = [
    "Zimg"
]

description = \
    """
    Z image colorspace ,depth, etc converter
    """

with scope("config") as c:
    import os
    c.release_packages_path = os.environ["SSE_REZ_REPO_RELEASE_EXT"]

requires = [
]

private_build_requires = [
]

variants = [
    ["platform-linux", "arch-x86_64", "os-centos-7"]
]

uuid = "repository.zimg"

# If want to use Ninja, run:
# rez-build -i --cmake-build-system "ninja"
# rez-release --cmake-build-system "ninja"
#
# Pass cmake arguments (with debug symbols):
# rez-build -i --build-system cmake --bt Debug
# rez-release --build-system cmake --bt Debug


def pre_build_commands():
    command("source /opt/rh/devtoolset-6/enable")


def commands():

    # NOTE: REZ package versions can have ".sse." to separate the external
    # version from the internal modification version.
    split_versions = str(version).split(".sse.")
    external_version = split_versions[0]
    internal_version = None
    if len(split_versions) == 2:
        internal_version = split_versions[1]

    env.ZIMG_VERSION = external_version
    env.ZIMG_PACKAGE_VERSION = external_version
    if internal_version:
        env.ZIMG_PACKAGE_VERSION = internal_version

    env.ZIMG_ROOT.append("{root}")
    env.ZIMG_LOCATION.append("{root}")

    env.ZIMG_INCLUDE_DIR = "{root}/include"
    env.ZIMG_LIBRARY_DIR = "{root}/lib"

    env.PATH.append("{root}/lib")
    env.LD_LIBRARY_PATH.append("{root}/lib")

    env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")
