import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import geopandas as gpd
import rasterio
import rasterio.mask
import numpy as np
import pandas as pd

# ---------------------------------------------------------
# 1. Load GADM boundary
# ---------------------------------------------------------
boundary = gpd.read_file("data/gadm_boundary.gpkg", layer="ADM_ADM_1")
print(boundary.columns)



# ---------------------------------------------------------
# 2. Clip WorldPop raster to the country boundary
# ---------------------------------------------------------
with rasterio.open(r"C:\Users\alsol\OneDrive\Desktop\Automated Population\data\worldpop.tif") as src:

    # FIX 1: Ensure boundary matches raster CRS BEFORE clipping
    boundary_raster_crs = boundary.to_crs(src.crs)
    
    # Convert boundary polygons into a single geometry
    boundary_geom = [boundary_raster_crs.unary_union.__geo_interface__]

    # Clip raster
    out_image, out_transform = rasterio.mask.mask(src, boundary_geom, crop=True)
    out_meta = src.meta.copy()

# Update metadata for clipped raster
out_meta.update({
    "height": out_image.shape[1],
    "width": out_image.shape[2],
    "transform": out_transform
})

# Save clipped raster
with rasterio.open("data/worldpop_clipped.tif", "w", **out_meta) as dest:
    dest.write(out_image)

# ---------------------------------------------------------
# 3. Prepare boundary for zonal statistics
# ---------------------------------------------------------
with rasterio.open("data/worldpop_clipped.tif") as src:
    raster_crs = src.crs
    nodata = src.nodata

# Project boundary to raster CRS (already matches, but good practice)
boundary_proj = boundary.to_crs(raster_crs)

# ---------------------------------------------------------
# 4. Compute zonal statistics
# ---------------------------------------------------------
stats = []

with rasterio.open(r"C:\Users\alsol\OneDrive\Desktop\Automated Population\data\worldpop.tif") as src:
    for idx, row in boundary_proj.iterrows():
        geom = [row.geometry.__geo_interface__]

        # Clip raster to individual polygon
        out_img, _ = rasterio.mask.mask(src, geom, crop=True)
        data = out_img[0]

        # FIX 2: Robustly handle both numeric nodata and NaN values
        if nodata is not None:
            if np.isnan(nodata):
                data = data[~np.isnan(data)]
            else:
                data = data[data != nodata]
                data = data[~np.isnan(data)] # WorldPop often has NaNs regardless of metadata
        else:
            data = data[~np.isnan(data)]

        # FIX 3: Safe calculation for empty regions
        if data.size > 0:
            total_pop = float(data.sum())
            mean_density = float(data.mean())
        else:
            total_pop = 0.0
            mean_density = 0.0

        stats.append({
            "id": row["GID_1"],   # <-- change if your GADM uses a different field
            "total_pop": total_pop,
            "mean_density": mean_density
        })

# ---------------------------------------------------------
# 5. Merge stats back into boundary
# ---------------------------------------------------------
stats_df = pd.DataFrame(stats)
boundary_stats = boundary.merge(stats_df, left_on="GID_1", right_on="id")

# ---------------------------------------------------------
# 6. Export results
# ---------------------------------------------------------
boundary_stats.to_file("data/gadm_worldpop_stats.gpkg", driver="GPKG")

