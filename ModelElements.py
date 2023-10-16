from typing import Tuple, List

from angle3d import Angle3D
from point3d import Point3D


class Texture:
    pass


class PolygonalModel:
    def __init__(self, textures: List[Texture]):
        self.textures = textures
        self.polygons: List[Polygon] = []
        self.points: List[Point3D] = []
        self.polygons.append(Polygon(self.points))


class Flash:
    def __init__(self):
        self.location: Point3D
        self.angle: Angle3D
        self.color: Tuple[int, int, int]
        self.power: float

    def Rotate(self, angle: Angle3D):
        pass

    def Move(self, location: Point3D):
        pass


class Camera:
    def __init__(self):
        self.location: Point3D
        self.angle: Angle3D

    def Rotate(self, angle: Angle3D):
        pass

    def Move(self, location: Point3D):
        pass


class Polygon:
    def __init__(self, points: List[Point3D]):
        self.points = points


class Scene:
    def __init__(self, id: int, models: List[PolygonalModel], flashes: List[Flash], cameras: List[Camera]):
        self.id = id
        if len(models) > 0:
            self.Models = models
        else:
            raise Exception("Должна быть одна модель")
        self.Flashes = flashes
        if len(cameras) > 0:
            self.cameras = cameras
        else:
            raise Exception("Должна быть одна модель")

    def method1(self, flash):
        return flash

    def method2(self, flash, camera):
        return flash