# RPCBuilder

## Summary
A reserved structure for defining a remote procedure call.

## Remarks
!!! warning
    Do not use this structure, as this is used for engine reserved functionality.

## Definition

**Namespace:** `SDT4.Managed.Network`  
**Assembly:** `SDT4.Managed.Network.dll`

```csharp
struct RPCBuilder
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



---

## Methods

#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) AddStructuredParameter&lt;T&gt;(T p, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) size)

**Parameters:**

- `p` (T): 

- `size` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) AddStringParameter([String](https://learn.microsoft.com/dotnet/api/system.string) p, [Int32](https://learn.microsoft.com/dotnet/api/system.int32) maxLength, [Encoding](https://learn.microsoft.com/dotnet/api/system.text.encoding) encoding)

**Parameters:**

- `p` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 

- `maxLength` ([Int32](https://learn.microsoft.com/dotnet/api/system.int32)): 

- `encoding` ([Encoding](https://learn.microsoft.com/dotnet/api/system.text.encoding)): 


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Call()

---


---