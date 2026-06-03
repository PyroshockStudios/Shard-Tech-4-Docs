# RCSSStyleDeclaration

## Summary




## Definition

**Namespace:** `SDT4.Managed.UI.RML`  
**Assembly:** `SDT4.Managed.UI.dll`

```csharp
sealed class RCSSStyleDeclaration
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔ [DynamicObject](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject) ➔  **RCSSStyleDeclaration**
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
| `public get; set; Item` | [String](https://learn.microsoft.com/dotnet/api/system.string) | Access style value by exact string name (e.g., Style["background-color"]) |



---

## Methods

#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Remove([String](https://learn.microsoft.com/dotnet/api/system.string) name)


**Summary:**
Removes style from element

**Parameters:**

- `name` ([String](https://learn.microsoft.com/dotnet/api/system.string)): 


---
#### public virtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) TryGetMember([GetMemberBinder](https://learn.microsoft.com/dotnet/api/system.dynamic.getmemberbinder) binder, out [Object](https://learn.microsoft.com/dotnet/api/system.object) result)


**Summary:**
Handles dynamic property reads (e.g., var color = Style.Color;)

**Parameters:**

- `binder` ([GetMemberBinder](https://learn.microsoft.com/dotnet/api/system.dynamic.getmemberbinder)): 

- `result` ([Object](https://learn.microsoft.com/dotnet/api/system.object)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---
#### public virtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) TrySetMember([SetMemberBinder](https://learn.microsoft.com/dotnet/api/system.dynamic.setmemberbinder) binder, [Object?](https://learn.microsoft.com/dotnet/api/system.object) value)


**Summary:**
Handles dynamic property writes (e.g., Style.BackgroundColor = "red";)

**Parameters:**

- `binder` ([SetMemberBinder](https://learn.microsoft.com/dotnet/api/system.dynamic.setmemberbinder)): 

- `value` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): 


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): 

---


---