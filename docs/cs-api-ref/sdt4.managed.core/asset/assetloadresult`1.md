# AssetLoadResult&lt;&gt;

## Summary




## Definition

**Namespace:** `SDT4.Managed.Core.Asset`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
struct AssetLoadResult<>
```
**Implements:**

##### [IEquatable&lt;AssetLoadResult&lt;TResource&gt;&gt;](https://learn.microsoft.com/dotnet/api/system.iequatable-1)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; set; ErrorCode` | [AssetErrorCode](./asseterrorcode.md) |  |
| `public get; set; Resource` | TResource |  |



---

## Methods

#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()

**Returns:**

- [String](https://learn.microsoft.com/dotnet/api/system.string): 

---
#### public virtual [Int32](https://learn.microsoft.com/dotnet/api/system.int32) GetHashCode()

**Returns:**

- [Int32](https://learn.microsoft.com/dotnet/api/system.int32): 

---
#### public virtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([Object](https://learn.microsoft.com/dotnet/api/system.object) obj)

**Parameters:**

- `obj` ([Object](https://learn.microsoft.com/dotnet/api/system.object)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) Equals([AssetLoadResult&lt;TResource&gt;](./assetloadresult`1.md) other)

**Parameters:**

- `other` ([AssetLoadResult&lt;TResource&gt;](./assetloadresult`1.md)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Deconstruct(out [AssetErrorCode](./asseterrorcode.md) ErrorCode, out TResource Resource)

**Parameters:**

- `ErrorCode` ([AssetErrorCode](./asseterrorcode.md)): 

- `Resource` (TResource): 


---


---