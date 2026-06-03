# RMLEventParameters

## Summary




## Definition

**Namespace:** `SDT4.Managed.UI.RML`  
**Assembly:** `SDT4.Managed.UI.dll`

```csharp
sealed class RMLEventParameters
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔  **RMLEventParameters**
**Implements:**

##### [IReadOnlyDictionary&lt;String, RMLVariant&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlydictionary-2), [IEnumerable&lt;KeyValuePair&lt;String, RMLVariant&gt;&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable), [IReadOnlyCollection&lt;KeyValuePair&lt;String, RMLVariant&gt;&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection-1)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; Keys` | [IEnumerable&lt;String&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) |  |
| `public get; Values` | [IEnumerable&lt;RMLVariant&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1) |  |
| `public get; Count` | [Int32](https://learn.microsoft.com/dotnet/api/system.int32) |  |
| `public get; Item` | [RMLVariant](./rmlvariant.md) |  |



---

## Methods

#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) ContainsKey([String](https://learn.microsoft.com/dotnet/api/system.string) key)

**Parameters:**

- `key` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) TryGetValue([String](https://learn.microsoft.com/dotnet/api/system.string) key, out [RMLVariant](./rmlvariant.md) value)

**Parameters:**

- `key` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 

- `value` ([RMLVariant](./rmlvariant.md)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public [IEnumerator&lt;KeyValuePair&lt;String, RMLVariant&gt;&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1) GetEnumerator()

**Returns:**

- [IEnumerator&lt;KeyValuePair&lt;String, RMLVariant&gt;&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1): 

---


---