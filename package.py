name = "alembic"

version = "1.8.6.hh.1.0.0"

authors = [
    "Sony Pictures Imageworks",
]

description = """Open computer graphics interchange framework"""

with scope("config") as c:
    import os

    c.release_packages_path = os.environ["HH_REZ_REPO_RELEASE_EXT"]

requires = [
    "hdf5-1.10",
    "openexr-3.1",
    "boost-1.82",
]

private_build_requires = []

variants = [
    ["python-3.7"],
    ["python-3.9"],
    ["python-3.10"],
    ["python-3.11"],
    ["python-3.12"],
]


# NOTE: Arguments for REZ build/release
# rez-build -i -- -DCMAKE_CXX_FLAGS="-D H5_BUILT_AS_DYNAMIC_LIB"
# rez-release -- -DCMAKE_CXX_FLAGS="-D H5_BUILT_AS_DYNAMIC_LIB"


def commands():
    env.REZ_ALEMBIC_ROOT = "{root}"
    env.ALEMBIC_ROOT = "{root}"
    env.ALEMBIC_LOCATION = "{root}"
    env.ALEMBIC_INCLUDE_DIR = "{root}/include"

    env.PATH.append("{root}/bin")
    env.LD_LIBRARY_PATH.append("{root}/lib")

    if "python" in resolve:
        python_ver = resolve["python"].version
        if python_ver.major == 3:
            if python_ver.minor == 7:
                env.PYTHONPATH.append("{root}/lib/python3.7/site-packages")
            elif python_ver.minor == 9:
                env.PYTHONPATH.append("{root}/lib/python3.9/site-packages")
            elif python_ver.minor == 10:
                env.PYTHONPATH.append("{root}/lib/python3.10/site-packages")
            elif python_ver.minor == 11:
                env.PYTHONPATH.append("{root}/lib/python3.11/site-packages")
            elif python_ver.minor == 12:
                env.PYTHONPATH.append("{root}/lib/python3.12/site-packages")


uuid = "repository.alembic"
