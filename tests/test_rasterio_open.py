from pathlib import Path
import shutil

import rasterio


FILEPATH = "./data/MOD13A2.A2020081.h18v08.006.2020100121033.hdf"


def test_rasterio_open(tmp_path: Path):
    num_files = 4
    filepaths = [tmp_path / f"file{i}" for i in range(num_files)]

    for i in range(num_files):
        shutil.copyfile(FILEPATH, filepaths[i])

    all_layer_names: list[str] = []
    for i in range(num_files):
        all_layer_names.extend(
            [
                f"HDF4_EOS:EOS_GRID:{tmp_path}/file{i}:MODIS_Grid_16DAY_1km_VI:1 km 16 days NDVI",
                f"HDF4_EOS:EOS_GRID:{tmp_path}/file{i}:MODIS_Grid_16DAY_1km_VI:1 km 16 days relative azimuth angle",
                f"HDF4_EOS:EOS_GRID:{tmp_path}/file{i}:MODIS_Grid_16DAY_1km_VI:1 km 16 days composite day of the year",
                f"HDF4_EOS:EOS_GRID:{tmp_path}/file{i}:MODIS_Grid_16DAY_1km_VI:1 km 16 days pixel reliability",
                f"HDF4_EOS:EOS_GRID:{tmp_path}/file{i}:MODIS_Grid_16DAY_1km_VI:1 km 16 days EVI",
                f"HDF4_EOS:EOS_GRID:{tmp_path}/file{i}:MODIS_Grid_16DAY_1km_VI:1 km 16 days VI Quality",
                f"HDF4_EOS:EOS_GRID:{tmp_path}/file{i}:MODIS_Grid_16DAY_1km_VI:1 km 16 days red reflectance",
                f"HDF4_EOS:EOS_GRID:{tmp_path}/file{i}:MODIS_Grid_16DAY_1km_VI:1 km 16 days NIR reflectance",
                f"HDF4_EOS:EOS_GRID:{tmp_path}/file{i}:MODIS_Grid_16DAY_1km_VI:1 km 16 days blue reflectance",
                f"HDF4_EOS:EOS_GRID:{tmp_path}/file{i}:MODIS_Grid_16DAY_1km_VI:1 km 16 days MIR reflectance",
                f"HDF4_EOS:EOS_GRID:{tmp_path}/file{i}:MODIS_Grid_16DAY_1km_VI:1 km 16 days view zenith angle",
                f"HDF4_EOS:EOS_GRID:{tmp_path}/file{i}:MODIS_Grid_16DAY_1km_VI:1 km 16 days sun zenith angle",
            ]
        )

    for layer in all_layer_names:
        with rasterio.open(layer):
            ...
