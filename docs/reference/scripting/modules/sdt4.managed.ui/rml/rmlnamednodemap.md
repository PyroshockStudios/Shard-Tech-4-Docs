# RMLNamedNodeMap



## Definition

**Namespace:** `SDT4.Managed.UI.RML`  
**Assembly:** `SDT4.Managed.UI.dll`

```csharp
sealed class RMLNamedNodeMap
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔ [DynamicObject](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject) ➔  **RMLNamedNodeMap**
**Implements:**

##### [IDynamicMetaObjectProvider](https://learn.microsoft.com/dotnet/api/system.dynamic.idynamicmetaobjectprovider)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |


---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; set; Item` | [RMLVariant](./rmlvariant.md) |  |
| `public get; Length` | [Int32](https://learn.microsoft.com/dotnet/api/system.int32) |  |


---

## Methods

#### public virtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) TryGetMember([GetMemberBinder](https://learn.microsoft.com/dotnet/api/system.dynamic.getmemberbinder) binder, out [Object](https://learn.microsoft.com/dotnet/api/system.object) result)

**Parameters:**

- `binder` ([GetMemberBinder](https://learn.microsoft.com/dotnet/api/system.dynamic.getmemberbinder)): 

- `result` ([Object](https://learn.microsoft.com/dotnet/api/system.object)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public virtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) TrySetMember([SetMemberBinder](https://learn.microsoft.com/dotnet/api/system.dynamic.setmemberbinder) binder, [Object?](https://learn.microsoft.com/dotnet/api/system.object) value)

**Parameters:**

- `binder` ([SetMemberBinder](https://learn.microsoft.com/dotnet/api/system.dynamic.setmemberbinder)): 

- `value` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---


---