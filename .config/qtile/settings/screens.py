from libqtile.config import Screen
from libqtile import bar
from .widgets import primary_widgets, secondary_widgets

def status_bar(widgets):
    return bar.Bar(widgets, 24)


screens = [Screen(top=status_bar(primary_widgets)),Screen(top=status_bar(secondary_widgets))]