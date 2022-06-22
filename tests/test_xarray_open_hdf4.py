from pathlib import Path
import shutil
import warnings

# import rasterio
# from rasterio.errors import NotGeoreferencedWarning
import xarray as xr


FILEPATH = "./tests/data/test_raster_data/MOD13A2.A2020081.h18v08.006.2020100121033.hdf"


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

    filepaths = [
        tmp_path / "file1",
        tmp_path / "file2",
        tmp_path / "file3",
        tmp_path / "file4",
    ]

    shutil.copyfile(FILEPATH, filepaths[0])
    shutil.copyfile(FILEPATH, filepaths[1])
    shutil.copyfile(FILEPATH, filepaths[2])
    shutil.copyfile(FILEPATH, filepaths[3])

    rtn = []
    for filepath in filepaths:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=NotGeoreferencedWarning)
            with rasterio.open(filepath) as src:
                layer_names = src.subdatasets
        layer = []
        for x in layer_names:
            a = xr.open_rasterio(x)
            layer.append(a)
        rtn.append(layer)
