from distutils.core import setup

setup(
    name="foo",
    version="1.0",
    packages=["foo"],
    package_data={
        "foo": ["config/config.xml"],
    },
    # data_files=[
    #     ("config", ["config/config.xml"])
    # ],
    # include_package_data=True,
)
