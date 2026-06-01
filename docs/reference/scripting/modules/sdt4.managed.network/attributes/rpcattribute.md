# RPCAttribute

## Summary
Defines a method to be treated as a remote callable procedure. This restricts certain capabilities, such as requiring 
<strong>strict</strong> memory layouts on input parameters, having limited managed data type usage, and argument size.



## Definition

**Namespace:** `SDT4.Managed.Network.Attributes`  
**Assembly:** `SDT4.Managed.Network.dll`

```csharp
sealed class RPCAttribute
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔ [Attribute](https://learn.microsoft.com/dotnet/api/system.attribute) ➔  **RPCAttribute**
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
| `public get; Broadcast` | [PacketBroadcast](../packetbroadcast.md) | Type of broadcast. |
| `public get; set; Protocol` | [PacketProtocol](../packetprotocol.md) | Protocol under which this call should follow |
| `public get; set; Validation` | [String?](https://learn.microsoft.com/dotnet/api/system.string) | Name of validation method. Must be in the same scope. |

---


## Methods



---