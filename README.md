# Kivy Image Meme

This is a simple Kivy project to create an image meme for your phone or tablet.

## Designing your image

You will need an image, a top caption, and a bottom caption. The image should ideally be a Creative Commons licensed image. You can search for Creative Commons licensed file by choosing the `Tools` option and `usage rights` and then choosing the `Labelled for noncommercial reuse with modification` option. You can also choose other filters here such as size, colour, and image type.

You can supply your own font here, or use the one from this repository. This font is called `pressuru.otf`.

## Create your code file

Use an editor to create a `main.py` file. You can copy the following template code into this file:

~~~
from kivy.app import App
from kivy.uix.widget import Widget

class MemeScreen(Widget):
    pass

class MemeApp(App):
    def build(self):
        return MemeScreen()

if __name__ == '__main__':
    MemeApp().run()
~~~

## Create your layout file

Use an editor to create a `meme.kv` file. You can copy the following template layout into this file:
~~~
#:kivy 1.9.0
#:import utils kivy.utils

<ImageLabel@Label>
    font_name: "pressuru.otf"
    color: (1,1,1,1)
    outline_color: (0,0,0,1)
    outline_width: pt(2)
    halign: 'center'

<MemeScreen>:
    Image:
        source: 'image.jpg'
        size: (root.width, root.height)
            
    ImageLabel:
        font_size: pt(24)
        center_x: root.width / 2
        center_y: root.height - pt(18)
        text: "TOP CAPTION"

    ImageLabel:
        font_size: pt(20)
        center_x: root.width / 2
        center_y: pt(20)
        text: "BOTTOM CAPTION"
~~~

If you are using your own font, make sure to replace the line `font_name: 'pressuru.otf'` with your own font. Also replace the line `source: 'image.jpg'` with your chosen image file.

## Test your image meme

You can test by running the following command from the Anaconda prompt:
~~~
set KIVY_DPI=92
python main.py --size 210x380
~~~
This runs an emulation of an iPhone sized window on your PC monitor.