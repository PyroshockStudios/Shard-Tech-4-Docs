# RcssStyleDeclaration

## Summary
Represents an element's inline RCSS style declarations, mirroring the DOM <c>CSSStyleDeclaration</c> interface.
Supports direct property access, indexers, and dynamic PascalCase/camelCase to kebab-case resolution.

## Remarks
!!! danger
    All calls made within this class <strong>MUST</strong> be performed on the Master Thread. 
    See [Threads.RunLater](../../sdt4.managed.core/threads.md#runlater) on how to safely call this from an asynchronous thread.
    Failure to comply with this can cause catastrophical failures as the engine is not designed for this.

## Definition

**Namespace:** `SDT4.Managed.UI.Rml`  
**Assembly:** `SDT4.Managed.UI.dll`

```csharp
sealed class RcssStyleDeclaration
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔ [DynamicObject](https://learn.microsoft.com/dotnet/api/system.dynamic.dynamicobject) ➔  **RcssStyleDeclaration**
**Implements:**

##### [IDynamicMetaObjectProvider](https://learn.microsoft.com/dotnet/api/system.dynamic.idynamicmetaobjectprovider), [IEnumerable&lt;KeyValuePair&lt;String, RmlVariant&gt;&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; set; Properties` | [RmlVariant](./rmlvariant.md) | Gets or sets an RCSS property value by its exact CSS property name (e.g., <c>style["background-color"]</c>). |
| `public get; LocalProperties` | [KeyValuePair&lt;String, RmlVariant&gt;[]](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2) | Lists the local properties defined by this element. |



---

## Methods

#### public [RmlVariant](./rmlvariant.md) GetProperty([String](https://learn.microsoft.com/dotnet/api/system.string) name)


**Summary:**
Retrieves the value of an RCSS property by its exact kebab-case name.
Corresponds to JavaScript <c>element.style.getPropertyValue(name)</c>.

**Parameters:**

- `name` ([String](https://learn.microsoft.com/dotnet/api/system.string)): The CSS property name (e.g., <c>"background-color"</c>, <c>"font-size"</c>).


**Returns:**

- [RmlVariant](./rmlvariant.md): The value of the property as a variant, or an empty variant if the property is not set.

---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) SetProperty([String](https://learn.microsoft.com/dotnet/api/system.string) name, [RmlVariant](./rmlvariant.md) value)


**Summary:**
Sets the value of an RCSS property by its exact kebab-case name.
Corresponds to JavaScript <c>element.style.setProperty(name, value)</c>.

**Parameters:**

- `name` ([String](https://learn.microsoft.com/dotnet/api/system.string)): The CSS property name (e.g., <c>"background-color"</c>).

- `value` ([RmlVariant](./rmlvariant.md)): The style value to set.


---
#### public [Void](https://learn.microsoft.com/dotnet/api/system.void) Remove([String](https://learn.microsoft.com/dotnet/api/system.string) name)


**Summary:**
Removes an RCSS property declaration from the element.
Corresponds to JavaScript <c>element.style.removeProperty(name)</c>.

**Parameters:**

- `name` ([String](https://learn.microsoft.com/dotnet/api/system.string)): The CSS property name to remove (e.g., <c>"background-color"</c>).


---
#### public virtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) TryGetMember([GetMemberBinder](https://learn.microsoft.com/dotnet/api/system.dynamic.getmemberbinder) binder, out [Object](https://learn.microsoft.com/dotnet/api/system.object) result)


**Summary:**
Provides dynamic member retrieval, mapping PascalCase or camelCase member access (e.g., <c>Style.BackgroundColor</c>)
to equivalent kebab-case RCSS property names (e.g., <c>"background-color"</c>).

**Parameters:**

- `binder` ([GetMemberBinder](https://learn.microsoft.com/dotnet/api/system.dynamic.getmemberbinder)): Provides the dynamic member name.

- `result` ([Object](https://learn.microsoft.com/dotnet/api/system.object)): Receives the resolved string style value.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> always, resolving missing styles as empty strings.

---
#### public virtual [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) TrySetMember([SetMemberBinder](https://learn.microsoft.com/dotnet/api/system.dynamic.setmemberbinder) binder, [Object?](https://learn.microsoft.com/dotnet/api/system.object) value)


**Summary:**
Provides dynamic member assignment, mapping PascalCase or camelCase member assignments (e.g., <c>Style.BackgroundColor = "red"</c>)
to equivalent kebab-case RCSS property names (e.g., <c>"background-color"</c>).

**Parameters:**

- `binder` ([SetMemberBinder](https://learn.microsoft.com/dotnet/api/system.dynamic.setmemberbinder)): Provides the dynamic member name.

- `value` ([Object?](https://learn.microsoft.com/dotnet/api/system.object)): The value to set, serialized via [Object.ToString](https://learn.microsoft.com/dotnet/api/system.object#tostring) or set to an empty string if <see langword="null" />.


**Returns:**

- [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean): <see langword="true" /> always.

---
#### public [IEnumerator&lt;KeyValuePair&lt;String, RmlVariant&gt;&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1) GetEnumerator()

**Returns:**

- [IEnumerator&lt;KeyValuePair&lt;String, RmlVariant&gt;&gt;](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1): 

---
#### public virtual [String](https://learn.microsoft.com/dotnet/api/system.string) ToString()

**Returns:**

- [String](https://learn.microsoft.com/dotnet/api/system.string): 

---


---