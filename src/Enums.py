
from enum import Enum

class CameraMovement(Enum):
    Empty=0
    PanLeft=1
    PanUp = 2
    PanRight = 3
    PanDown = 4
    ZoomIn = 5
    ZoomOut = 6
    RotateXLeft = 7
    RotateXRight = 8
    RotateYLeft = 9
    RotateYRight = 10
    RotateZLeft = 11
    RotateZRight = 12