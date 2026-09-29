# AssetId

## Summary
Represents an immutable identifier for an asset, wrapping its string path or name
and providing access to its corresponding unique identifier.

## Remarks
This struct is immutable and intrinsically thread-safe for concurrent read operations.

## Definition

**Namespace:** `SDT4.Managed.Core.Asset`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
struct AssetId
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
| `public static get; Null` | [AssetId](./assetid.md) | Gets an empty or uninitialized [AssetId](./assetid.md) instance. |
| `public get; Asset` | [String](https://learn.microsoft.com/dotnet/api/system.string) | Gets the underlying asset path or name string. |
| `public get; Id` | [Guid](https://learn.microsoft.com/dotnet/api/system.guid) | Gets the globally unique identifier ([Guid](https://learn.microsoft.com/dotnet/api/system.guid)) associated with this asset. |



---

## Methods

#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()


**Summary:**
Returns the string representation of the asset identifier.

**Returns:**

- [String](https://learn.microsoft.com/dotnet/api/system.string): The string value of [AssetId.Asset](./assetid.md#asset).

---


---