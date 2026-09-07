# ScriptCategoryAttribute

## Summary
Allows categorising a member into a hierarchy in the V-Script Node Context Menu
Valid categories contain strictly only alphanumeric characters, and are separated with a pipe |
            
Valid categories include:
* "Input|Utility": all members fall under "Input" &gt; "Utility"
* "MyHelpers": all members fall under "MyHelpers"
* "Audio and Music|Controls": all members fall under "Audio and Music" &gt; "Controls"
            
Note that if [ScriptCategoryAttribute.FlattenType](./scriptcategoryattribute.md#flattentype) is set to `false`, and this attribute is applied onto a class/struct/interface/enum,
the type <em>itself</em> will fall under the category. 
For instance for a class MyClass with  [ScriptCategoryAttribute.FlattenType](./scriptcategoryattribute.md#flattentype) set to false:
* "Input|Helpers": all members fall under "Input" &gt; "Utility" &gt; "MyClass"



## Definition

**Namespace:** `SDT4.Managed.Core.Attributes`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
sealed class ScriptCategoryAttribute
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔ [Attribute](https://learn.microsoft.com/dotnet/api/system.attribute) ➔  **ScriptCategoryAttribute**
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
| `public get; Categories` | [String](https://learn.microsoft.com/dotnet/api/system.string) |  |
| `public get; set; FlattenType` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) |  |



---

## Methods



---