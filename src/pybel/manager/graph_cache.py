# -*- coding: utf-8 -*-

import logging

from . import models
from .cache import BaseCacheManager
from ..constants import METADATA_NAME
from ..io import to_bytes, from_bytes

log = logging.getLogger(__name__)


class GraphCacheManager(BaseCacheManager):
    def store_graph(self, graph):
        """Stores a graph in the database

        :param graph: a BEL network
        :type graph: :class:`pybel.BELGraph`
        """
        log.info('Storing network: %s', graph.document[METADATA_NAME])

        network = models.Network(blob=to_bytes(graph), **graph.document)

        self.session.add(network)
        self.session.commit()

        return network

    def get_graph_versions(self, name):
        """Returns all of the versions of a graph with the given name"""
        return {x for x, in self.session.query(models.Network.version).filter(models.Network.name == name).all()}

    def get_graph(self, name, version=None):
        """Loads most recent graph, or allows for specification of version

        :param name: The name of the graph
        :type name: str
        :param version: The version string of the graph. If not specified, loads most recent graph added with this name
        :type version: str
        :return:
        """
        if version is not None:
            n = self.session.query(models.Network).filter(models.Network.name == name,
                                                          models.Network.version == version).one()
        else:
            n = self.session.query(models.Network).filter(models.Network.name == name).order_by(
                models.Network.created.desc()).limit(1).one()

        return from_bytes(n.blob)

    def ls(self):
        return [(network.name, network.version) for network in self.session.query(models.Network).all()]
