from dataclasses import dataclass
from typing import List, Tuple
import math

@dataclass
class Point:
    x: float
    y: float

@dataclass
class Line:
    start: Point
    end: Point

@dataclass
class Circle:
    center: Point
    radius: float

class GeometryManager:
    def __init__(self):
        self.shapes = []
        self.selected_shape = None
    
    def create_line(self, start_x: float, start_y: float, end_x: float, end_y: float) -> Line:
        line = Line(Point(start_x, start_y), Point(end_x, end_y))
        self.shapes.append(line)
        return line
    
    def create_circle(self, center_x: float, center_y: float, radius: float) -> Circle:
        circle = Circle(Point(center_x, center_y), radius)
        self.shapes.append(circle)
        return circle
    
    def delete_shape(self, shape):
        if shape in self.shapes:
            self.shapes.remove(shape)
    
    def select_shape(self, x: float, y: float):
        min_distance = float('inf')
        selected = None
        
        for shape in self.shapes:
            if isinstance(shape, Line):
                dist = self._point_to_line_distance(Point(x, y), shape)
                if dist < min_distance:
                    min_distance = dist
                    selected = shape
            elif isinstance(shape, Circle):
                dist = math.sqrt((x - shape.center.x)**2 + (y - shape.center.y)**2)
                if abs(dist - shape.radius) < min_distance:
                    min_distance = abs(dist - shape.radius)
                    selected = shape
        
        if min_distance < 5:  # Selection threshold
            self.selected_shape = selected
            return selected
        return None
    
    def _point_to_line_distance(self, point: Point, line: Line) -> float:
        numerator = abs((line.end.y - line.start.y) * point.x - 
                       (line.end.x - line.start.x) * point.y + 
                       line.end.x * line.start.y - 
                       line.end.y * line.start.x)
        denominator = math.sqrt((line.end.y - line.start.y)**2 + 
                              (line.end.x - line.start.x)**2)
        return numerator / denominator if denominator != 0 else float('inf')
