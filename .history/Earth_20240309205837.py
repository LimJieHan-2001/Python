import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

def plot_3d_earth():
    # Create a Basemap instance for Orthographic projection
    m = Basemap(projection='ortho', lat_0=0, lon_0=0)

    # Draw coastlines, countries, and continents
    m.drawcoastlines(linewidth=0.5)
    m.drawcountries(linewidth=0.5)
    m.fillcontinents(color='lightgreen', lake_color='lightblue')

    # Draw parallels and meridians
    m.drawparallels(np.arange(-90., 91., 30.), labels=[True, False, False, True], dashes=[2, 2])
    m.drawmeridians(np.arange(-180., 181., 60.), labels=[False, True, False, True], dashes=[2, 2])

    # Create a grid of latitude and longitude points
    lats = np.linspace(-90, 90, 181)
    lons = np.linspace(-180, 180, 361)

    # Convert latitude and longitude points to x, y, z coordinates
    lons, lats = np.meshgrid(lons, lats)
    x, y = m(lons, lats)

    # Create a colormap for the Earth
    cmap = plt.get_cmap('terrain')

    # Plot the Earth with colors
    m.contourf(x, y, np.zeros_like(x), cmap=cmap)

    # Set title
    plt.title('3D Model of Earth')

    # Show the plot
    plt.show()

if __name__ == "__main__":
    plot_3d_earth()
