# IRemoteConnection

## Summary




## Definition

**Namespace:** `SDT4.Managed.Network`  
**Assembly:** `SDT4.Managed.Network.dll`

```csharp
interface IRemoteConnection
```
**Implements:**

##### 
---

## Fields

| Name | Type | Description |
| --- | --- | --- |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; Status` | [RemoteConnectionStatus](./remoteconnectionstatus.md) |  |
| `public get; RoundTripTime` | [Int64](https://learn.microsoft.com/dotnet/api/system.int64) |  |
| `public get; ConnectionTime` | [Int64](https://learn.microsoft.com/dotnet/api/system.int64) |  |



---

## Methods

#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Disconnect()

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) SendPacket([Byte[]](https://learn.microsoft.com/dotnet/api/system.byte) data, [PacketProtocol](./packetprotocol.md) protocol)

**Parameters:**

- `data` ([Byte[]](https://learn.microsoft.com/dotnet/api/system.byte)): 

- `protocol` ([PacketProtocol](./packetprotocol.md)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) AddPacketListener([PacketListenerDelegate](./packetlistenerdelegate.md) listener)

**Parameters:**

- `listener` ([PacketListenerDelegate](./packetlistenerdelegate.md)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) RemovePacketListener([PacketListenerDelegate](./packetlistenerdelegate.md) listener)

**Parameters:**

- `listener` ([PacketListenerDelegate](./packetlistenerdelegate.md)): 


---


---