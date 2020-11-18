# generated by datamodel-codegen:
#   filename:  Plane.json
#   timestamp: 2020-11-18T11:56:16+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel


class Point(BaseModel):
    value: Optional[List[float]] = None
    id: Optional[Optional[str]] = None
    totalChildrenCount: Optional[int] = None
    applicationId: Optional[Optional[str]] = None
    speckle_type: Optional[Optional[str]] = None


class Vector(BaseModel):
    value: Optional[List[float]] = None
    id: Optional[Optional[str]] = None
    totalChildrenCount: Optional[int] = None
    applicationId: Optional[Optional[str]] = None
    speckle_type: Optional[Optional[str]] = None


class Plane(BaseModel):
    origin: Optional[Point] = None
    normal: Optional[Vector] = None
    xdir: Optional[Vector] = None
    ydir: Optional[Vector] = None
    id: Optional[Optional[str]] = None
    totalChildrenCount: Optional[int] = None
    applicationId: Optional[Optional[str]] = None
    speckle_type: Optional[Optional[str]] = None
