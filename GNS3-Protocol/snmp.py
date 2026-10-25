import asyncio

from pysnmp.hlapi.asyncio import (
    CommunityData,
    ContextData,
    ObjectIdentity,
    ObjectType,
    SnmpEngine,
    UdpTransportTarget,
    get_cmd,
    next_cmd,
)


IF_DESCR_OID = "1.3.6.1.2.1.2.2.1.2"
IF_OPER_STATUS_OID = "1.3.6.1.2.1.2.2.1.8"
IF_OPER_STATUS = {
    1: "up",
    2: "down",
    3: "testing",
    4: "unknown",
    5: "dormant",
    6: "notPresent",
    7: "lowerLayerDown",
}


async def _snmp_find_interface_index(host, interface_name, community="public"):
    transport = await UdpTransportTarget.create((host, 161), timeout=2, retries=1)

    async for error_indication, error_status, error_index, var_binds in next_cmd(
        SnmpEngine(),
        CommunityData(community, mpModel=1),
        transport,
        ContextData(),
        ObjectType(ObjectIdentity(IF_DESCR_OID)),
        lexicographicMode=False,
    ):
        if error_indication:
            raise RuntimeError(error_indication)

        if error_status:
            raise RuntimeError(
                f"{error_status.prettyPrint()} at {error_index}"
            )

        for oid, value in var_binds:
            if str(value) == interface_name:
                return int(str(oid).split(".")[-1])

    raise RuntimeError(f"Interface {interface_name!r} was not found over SNMP")


async def _snmp_get_portchannel_state(host, community="public"):
    interface_index = await _snmp_find_interface_index(
        host,
        "Port-channel1",
        community,
    )
    transport = await UdpTransportTarget.create((host, 161), timeout=2, retries=1)

    error_indication, error_status, error_index, var_binds = await get_cmd(
        SnmpEngine(),
        CommunityData(community, mpModel=1),
        transport,
        ContextData(),
        ObjectType(ObjectIdentity(f"{IF_OPER_STATUS_OID}.{interface_index}")),
    )

    if error_indication:
        raise RuntimeError(error_indication)

    if error_status:
        raise RuntimeError(f"{error_status.prettyPrint()} at {error_index}")

    return IF_OPER_STATUS.get(int(var_binds[0][1]), "unknown")


def snmp_get_portchannel_state(host, community="public"):
    return asyncio.run(_snmp_get_portchannel_state(host, community))


def test_r1_portchannel_snmp():
    state = snmp_get_portchannel_state("10.10.10.1")

    assert state == "up"
