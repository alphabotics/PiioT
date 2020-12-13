import abc
from sqlalchemy import inspect
from App.Http.responses.pagination_response import PaginationResponse

class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def to_dict(self, obj):
        raise NotImplementedError

    @abc.abstractmethod
    def to_list(self, l):
        raise NotImplementedError



class BaseRepository(AbstractRepository):

    def __init__(self, session):
        self.session = session

    def to_dict(self, obj):
        if obj is not None:
            return {c.key: getattr(obj, c.key)
                for c in inspect(obj).mapper.column_attrs}
        else:
            return {}

    def to_list(self, _list):
        if isinstance(_list, list) and len(_list):
            output = []
            for item in _list:
                output.append(self.to_dict(item))
            return output
        else:
            print("A list is reuired!")
            return []

    def formatted_paginate(self, results):
        return PaginationResponse(
            total = results.total,
            per_page = results.per_page,
            last_page = results.last_page,
            current_page = results.current_page,
            data = results.serialize()
        )
        