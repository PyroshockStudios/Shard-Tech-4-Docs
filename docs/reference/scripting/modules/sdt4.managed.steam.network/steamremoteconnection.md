# SteamRemoteConnection



## Definition

**Namespace:** `SDT4.Managed.Steam.Network`  
**Assembly:** `SDT4.Managed.Steam.Network.dll`

```csharp
class SteamRemoteConnection
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **SteamRemoteConnection**
**Implements:**

##### [IRemoteConnection](../sdt4.managed.network/iremoteconnection.md)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |


---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; Status` | [RemoteConnectionStatus](../sdt4.managed.network/remoteconnectionstatus.md) |  |
| `public get; RoundTripTime` | [Int64](https://learn.microsoft.com/dotnet/api/system.int64) |  |
| `public get; ConnectionTime` | [Int64](https://learn.microsoft.com/dotnet/api/system.int64) |  |


---

## Methods

#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) StartListeningAsync()

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Disconnect()

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) SendPacket([Byte[]](https://learn.microsoft.com/dotnet/api/system.byte) data, [PacketProtocol](../sdt4.managed.network/packetprotocol.md) protocol)

**Parameters:**

- `data` ([Byte[]](https://learn.microsoft.com/dotnet/api/system.byte)): 

- `protocol` ([PacketProtocol](../sdt4.managed.network/packetprotocol.md)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) AddPacketListener([PacketListenerDelegate](../sdt4.managed.network/packetlistenerdelegate.md) listener)

**Parameters:**

- `listener` ([PacketListenerDelegate](../sdt4.managed.network/packetlistenerdelegate.md)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) RemovePacketListener([PacketListenerDelegate](../sdt4.managed.network/packetlistenerdelegate.md) listener)

**Parameters:**

- `listener` ([PacketListenerDelegate](../sdt4.managed.network/packetlistenerdelegate.md)): 


---


---