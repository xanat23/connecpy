# -*- coding: utf-8 -*-
# Generated by https://github.com/i2y/connecpy/protoc-gen-connecpy.  DO NOT EDIT!
# source: haberdasher.proto

from typing import Protocol, Union

import httpx

from connecpy.async_client import AsyncConnecpyClient
from connecpy.base import Endpoint
from connecpy.server import ConnecpyServer
from connecpy.client import ConnecpyClient
from connecpy.context import ServiceContext

import haberdasher_pb2 as _pb2


class HaberdasherService(Protocol):
    async def MakeHat(self, req: _pb2.Size, ctx: ServiceContext) -> _pb2.Hat:
        ...


class HaberdasherServer(ConnecpyServer):
    def __init__(self, *, service: HaberdasherService, server_path_prefix=""):
        super().__init__(service=service)
        self._prefix = f"{server_path_prefix}/i2y.connecpy.example.Haberdasher"
        self._endpoints = {
            "MakeHat": Endpoint[_pb2.Size, _pb2.Hat](
                service_name="Haberdasher",
                name="MakeHat",
                function=getattr(service, "MakeHat"),
                input=_pb2.Size,
                output=_pb2.Hat,
            ),
        }


class HaberdasherClient(ConnecpyClient):
    def MakeHat(
        self,
        *,
        request,
        ctx,
        server_path_prefix="",
        **kwargs,
    ):
        return self._make_request(
            url=f"{server_path_prefix}/i2y.connecpy.example.Haberdasher/MakeHat",
            ctx=ctx,
            request=request,
            response_obj=_pb2.Hat,
            **kwargs,
        )


class AsyncHaberdasherClient(AsyncConnecpyClient):
    async def MakeHat(
        self,
        *,
        request,
        ctx,
        server_path_prefix="",
        session: Union[httpx.AsyncClient, None] = None,
        **kwargs,
    ):
        return await self._make_request(
            url=f"{server_path_prefix}/i2y.connecpy.example.Haberdasher/MakeHat",
            ctx=ctx,
            request=request,
            response_obj=_pb2.Hat,
            session=session,
            **kwargs,
        )
