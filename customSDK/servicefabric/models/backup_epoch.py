# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BackupEpoch(Model):
    """An Epoch is a configuration number for the partition as a whole. When the
    configuration of the replica set changes, for example when the Primary
    replica changes, the operations that are replicated from the new Primary
    replica are said to be a new Epoch from the ones which were sent by the old
    Primary replica.

    :param configuration_number: The current configuration number of this
     Epoch. The configuration number is an increasing value that is updated
     whenever the configuration of this replica set changes.
    :type configuration_number: str
    :param data_loss_number: The current dataloss number of this Epoch. The
     data loss number property is an increasing value which is updated whenever
     data loss is suspected, as when loss of a quorum of replicas in the
     replica set that includes the Primary replica.
    :type data_loss_number: str
    """

    _attribute_map = {
        'configuration_number': {'key': 'ConfigurationNumber', 'type': 'str'},
        'data_loss_number': {'key': 'DataLossNumber', 'type': 'str'},
    }

    def __init__(self, configuration_number=None, data_loss_number=None):
        super(BackupEpoch, self).__init__()
        self.configuration_number = configuration_number
        self.data_loss_number = data_loss_number
