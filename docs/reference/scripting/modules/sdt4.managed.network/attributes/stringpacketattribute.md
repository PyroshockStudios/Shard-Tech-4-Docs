# StringPacketAttribute

## Summary
Allows managed strings to be sent to remote connections.



## Definition

**Namespace:** `SDT4.Managed.Network.Attributes`  
**Assembly:** `SDT4.Managed.Network.dll`

```csharp
sealed class StringPacketAttribute
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔ [Attribute](https://learn.microsoft.com/dotnet/api/system.attribute) ➔  **StringPacketAttribute**
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
| `public get; MaxLength` | [Int32](https://learn.microsoft.com/dotnet/api/system.int32) | Maximum length for strings. Valid numbers range from 1 or above. |
| `public get; set; CharSet` | [PacketCharSet](./packetcharset.md) | Character set used when marshalling characters. This property modifies the packet size. Default value is ASCII |



---

## Methods



---