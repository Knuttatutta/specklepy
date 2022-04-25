# generated by datamodel-codegen:
#   filename:  stream_schema.json
#   timestamp: 2020-11-17T14:33:13+00:00

from datetime import datetime
from typing import Any, Dict, List, Optional


from pydantic import BaseModel


class Collaborator(BaseModel):
    id: Optional[str]
    name: Optional[str]
    role: Optional[str]
    avatar: Optional[str]


class Commit(BaseModel):
    id: Optional[str]
    message: Optional[str]
    authorName: Optional[str]
    authorId: Optional[str]
    authorAvatar: Optional[str]
    branchName: Optional[str]
    createdAt: Optional[datetime]
    sourceApplication: Optional[str]
    referencedObject: Optional[str]
    totalChildrenCount: Optional[int]
    parents: Optional[List[str]]

    def __repr__(self) -> str:
        return f"Commit( id: {self.id}, message: {self.message}, referencedObject: {self.referencedObject}, authorName: {self.authorName}, branchName: {self.branchName}, createdAt: {self.createdAt} )"

    def __str__(self) -> str:
        return self.__repr__()


class Commits(BaseModel):
    totalCount: Optional[int]
    cursor: Optional[datetime]
    items: List[Commit] = []


class Object(BaseModel):
    id: Optional[str]
    speckleType: Optional[str]
    applicationId: Optional[str]
    totalChildrenCount: Optional[int]
    createdAt: Optional[datetime]


class Branch(BaseModel):
    id: Optional[str]
    name: Optional[str]
    description: Optional[str]
    commits: Optional[Commits]


class Branches(BaseModel):
    totalCount: Optional[int]
    cursor: Optional[datetime]
    items: List[Branch] = []


class Stream(BaseModel):
    id: Optional[str]
    name: Optional[str]
    role: Optional[str]
    isPublic: Optional[bool]
    description: Optional[str]
    createdAt: Optional[datetime]
    updatedAt: Optional[datetime]
    collaborators: List[Collaborator] = []
    branches: Optional[Branches]
    commit: Optional[Commit]
    object: Optional[Object]
    commentCount: Optional[int]
    favoritedDate: Optional[datetime]
    favoritesCount: Optional[int]

    def __repr__(self):
        return f"Stream( id: {self.id}, name: {self.name}, description: {self.description}, isPublic: {self.isPublic})"

    def __str__(self) -> str:
        return self.__repr__()


class Streams(BaseModel):
    totalCount: Optional[int]
    cursor: Optional[datetime]
    items: List[Stream] = []


class User(BaseModel):
    id: Optional[str]
    email: Optional[str]
    name: Optional[str]
    bio: Optional[str]
    company: Optional[str]
    avatar: Optional[str]
    verified: Optional[bool]
    role: Optional[str]
    streams: Optional[Streams]

    def __repr__(self):
        return f"User( id: {self.id}, name: {self.name}, email: {self.email}, company: {self.company} )"

    def __str__(self) -> str:
        return self.__repr__()


class Activity(BaseModel):
    actionType: Optional[str]
    info: Optional[dict]
    userId: Optional[str]
    streamId: Optional[str]
    resourceId: Optional[str]
    resourceType: Optional[str]
    message: Optional[str]
    time: Optional[datetime]

    def __repr__(self) -> str:
        return f"Activity( streamId: {self.streamId}, actionType: {self.actionType}, message: {self.message}, userId: {self.userId} )"

    def __str__(self) -> str:
        return self.__repr__()


class ActivityCollection(BaseModel):
    totalCount: Optional[int]
    items: Optional[List[Activity]]
    cursor: Optional[datetime]

    def __repr__(self) -> str:
        return f"ActivityCollection( totalCount: {self.totalCount}, items: {len(self.items) if self.items else 0}, cursor: {self.cursor.isoformat()} )"

    def __str__(self) -> str:
        return self.__repr__()


class ServerInfo(BaseModel):
    name: Optional[str]
    company: Optional[str]
    url: Optional[str]
    description: Optional[str]
    adminContact: Optional[str]
    canonicalUrl: Optional[str]
    roles: Optional[List[dict]]
    scopes: Optional[List[dict]]
    authStrategies: Optional[List[dict]]
    version: Optional[str]
