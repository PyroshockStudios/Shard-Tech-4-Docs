# PacketCharSet

## Summary
Character set for string packet marshalling



## Definition

**Namespace:** `SDT4.Managed.Network.Attributes`  
**Assembly:** `SDT4.Managed.Network.dll`

```csharp
enum PacketCharSet
```

---

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `ASCII` | [PacketCharSet](./packetcharset.md) | ASCII encoding of strings. Uses 1 byte per character, however has limited character sets. This character set estimates the maximal packet size to be 1 * string.Length |
| `Unicode` | [PacketCharSet](./packetcharset.md) | UTF8 encoding of strings. Uses between 1-4 bytes per character. This character set overestimates the  maximal packet size to be 4 * string.Length. |

---


## Properties

| Name | Type | Description |
| --- | --- | --- |

---


## Methods



---