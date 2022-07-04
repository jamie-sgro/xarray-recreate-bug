from pathlib import Path
import shutil
import warnings

import rasterio
from rasterio.errors import NotGeoreferencedWarning
import xarray as xr


FILEPATH = "./data/MOD13A2.A2020081.h18v08.006.2020100121033.hdf"


def test_can_open_hdf4_closer_to_error_replication(tmp_path: Path):
    """A Unique bug discovered June 22nd 2022.
    In Docker environments only, throws the below error. This only occurs
    when trying to append the output of open_hdf4 to another object, and so
    far only fails on the 3rd iteration, regardless of the order of the files
    and the contents of the files themselves. Note we use a copy of a file
    for each iteration and it still fails

    ```bash
    rasterio.errors.RasterioIOError: HDF4_EOS:EOS_GRID:/tmp/pytest-of-root/
    pytest-5/test_can_open_hdf4_closer_to_e0/file3:MODIS_Grid_16DAY_1km_VI:1
    km 16 days blue reflectance: No such file or directory
    ```
    """

    num_files = 4
    filepaths = [tmp_path / f"file{i}" for i in range(num_files)]

    for i in range(num_files):
        shutil.copyfile(FILEPATH, filepaths[i])

    rtn = []
    for filepath in filepaths:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=NotGeoreferencedWarning)
            with rasterio.open(filepath) as src:
                layer_names = src.subdatasets
        layer = []
        for layer_name in layer_names:
            with xr.open_rasterio(layer_name) as da:
                layer.append(da)
        rtn.append(layer)

def test2(tmp_path: Path):
    """A Unique bug discovered June 22nd 2022.
    In Docker environments only, throws the below error. This only occurs
    when trying to append the output of open_hdf4 to another object, and so
    far only fails on the 3rd iteration, regardless of the order of the files
    and the contents of the files themselves. Note we use a copy of a file
    for each iteration and it still fails

    ```bash
    rasterio.errors.RasterioIOError: HDF4_EOS:EOS_GRID:/tmp/pytest-of-root/
    pytest-5/test_can_open_hdf4_closer_to_e0/file3:MODIS_Grid_16DAY_1km_VI:1
    km 16 days blue reflectance: No such file or directory
    ```
    """

    num_files = 4
    filepaths = [tmp_path / f"file{i}" for i in range(num_files)]

    for i in range(num_files):
        shutil.copyfile(FILEPATH, filepaths[i])


    rtn = []
    for filepath in filepaths:
        with xr.open_dataset(filepath, engine="rasterio") as ds_new:
            ...
        # with warnings.catch_warnings():
        #     warnings.simplefilter("ignore", category=NotGeoreferencedWarning)
        #     with rasterio.open(filepath) as src:
        #         layer_names = src.subdatasets
        # layer = []
        # for layer_name in layer_names:
        #     with xr.open_rasterio(layer_name) as da:
        #         layer.append(da)
        # rtn.append(layer)