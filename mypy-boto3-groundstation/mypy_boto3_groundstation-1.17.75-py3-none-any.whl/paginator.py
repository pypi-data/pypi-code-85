"""
Type annotations for groundstation service client paginators.

[Open documentation](./paginators.md)

Usage::

    ```python
    import boto3

    from mypy_boto3_groundstation import GroundStationClient
    from mypy_boto3_groundstation.paginator import (
        ListConfigsPaginator,
        ListContactsPaginator,
        ListDataflowEndpointGroupsPaginator,
        ListGroundStationsPaginator,
        ListMissionProfilesPaginator,
        ListSatellitesPaginator,
    )

    client: GroundStationClient = boto3.client("groundstation")

    list_configs_paginator: ListConfigsPaginator = client.get_paginator("list_configs")
    list_contacts_paginator: ListContactsPaginator = client.get_paginator("list_contacts")
    list_dataflow_endpoint_groups_paginator: ListDataflowEndpointGroupsPaginator = client.get_paginator("list_dataflow_endpoint_groups")
    list_ground_stations_paginator: ListGroundStationsPaginator = client.get_paginator("list_ground_stations")
    list_mission_profiles_paginator: ListMissionProfilesPaginator = client.get_paginator("list_mission_profiles")
    list_satellites_paginator: ListSatellitesPaginator = client.get_paginator("list_satellites")
    ```
"""
from datetime import datetime
from typing import Iterator, List

from botocore.paginate import Paginator as Boto3Paginator

from .literals import ContactStatusType
from .type_defs import (
    ListConfigsResponseTypeDef,
    ListContactsResponseTypeDef,
    ListDataflowEndpointGroupsResponseTypeDef,
    ListGroundStationsResponseTypeDef,
    ListMissionProfilesResponseTypeDef,
    ListSatellitesResponseTypeDef,
    PaginatorConfigTypeDef,
)

__all__ = (
    "ListConfigsPaginator",
    "ListContactsPaginator",
    "ListDataflowEndpointGroupsPaginator",
    "ListGroundStationsPaginator",
    "ListMissionProfilesPaginator",
    "ListSatellitesPaginator",
)


class ListConfigsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/groundstation.html#GroundStation.Paginator.ListConfigs)[Show boto3-stubs documentation](./paginators.md#listconfigspaginator)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListConfigsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/groundstation.html#GroundStation.Paginator.ListConfigs.paginate)
        [Show boto3-stubs documentation](./paginators.md#listconfigspaginator)
        """


class ListContactsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/groundstation.html#GroundStation.Paginator.ListContacts)[Show boto3-stubs documentation](./paginators.md#listcontactspaginator)
    """

    def paginate(
        self,
        endTime: datetime,
        startTime: datetime,
        statusList: List[ContactStatusType],
        groundStation: str = None,
        missionProfileArn: str = None,
        satelliteArn: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> Iterator[ListContactsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/groundstation.html#GroundStation.Paginator.ListContacts.paginate)
        [Show boto3-stubs documentation](./paginators.md#listcontactspaginator)
        """


class ListDataflowEndpointGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/groundstation.html#GroundStation.Paginator.ListDataflowEndpointGroups)[Show boto3-stubs documentation](./paginators.md#listdataflowendpointgroupspaginator)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListDataflowEndpointGroupsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/groundstation.html#GroundStation.Paginator.ListDataflowEndpointGroups.paginate)
        [Show boto3-stubs documentation](./paginators.md#listdataflowendpointgroupspaginator)
        """


class ListGroundStationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/groundstation.html#GroundStation.Paginator.ListGroundStations)[Show boto3-stubs documentation](./paginators.md#listgroundstationspaginator)
    """

    def paginate(
        self, satelliteId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListGroundStationsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/groundstation.html#GroundStation.Paginator.ListGroundStations.paginate)
        [Show boto3-stubs documentation](./paginators.md#listgroundstationspaginator)
        """


class ListMissionProfilesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/groundstation.html#GroundStation.Paginator.ListMissionProfiles)[Show boto3-stubs documentation](./paginators.md#listmissionprofilespaginator)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListMissionProfilesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/groundstation.html#GroundStation.Paginator.ListMissionProfiles.paginate)
        [Show boto3-stubs documentation](./paginators.md#listmissionprofilespaginator)
        """


class ListSatellitesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/groundstation.html#GroundStation.Paginator.ListSatellites)[Show boto3-stubs documentation](./paginators.md#listsatellitespaginator)
    """

    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSatellitesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.17.75/reference/services/groundstation.html#GroundStation.Paginator.ListSatellites.paginate)
        [Show boto3-stubs documentation](./paginators.md#listsatellitespaginator)
        """
