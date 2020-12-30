import skimage

import napari

with napari.gui_qt():
    v = napari.Viewer()
    image_layer = v.add_image(
        skimage.data.astronaut(), source=skimage.data.astronaut
    )
    print(image_layer.source)
    print(image_layer.metadata['source'])
