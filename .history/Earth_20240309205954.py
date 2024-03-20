import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.image import imread

def plot_real_earth():
    # Create a Basemap instance for Orthographic projection
    m = Basemap(projection='ortho', lat_0=0, lon_0=0)

    # Define the path to the Blue Marble image
    image_path = 'bluemarble.jpg'

    # Read the Blue Marble image
    img = imread(image_path)

    # Draw coastlines, countries, and continents
    m.drawcoastlines(linewidth=0.5)
    m.drawcountries(linewidth=0.5)
    m.fillcontinents(color='lightgreen', lake_color='lightblue')

    # Create a grid of latitude and longitude points
    lats = np.linspace(-90, 90, img.shape[0])
    lons = np.linspace(-180, 180, img.shape[1])

    # Convert latitude and longitude points to x, y coordinates
    lons, lats = np.meshgrid(lons, lats)
    x, y = m(lons, lats)

    # Plot the Blue Marble image
    m.imshow(img, origin='upper', extent=[-180, 180, -90, 90])

    # Set title
    plt.title('Real Earth')

    # Show the plot
    plt.show()

if __name__ == "__main__":
    plot_real_earth()
