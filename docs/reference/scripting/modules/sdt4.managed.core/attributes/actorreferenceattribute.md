# ActorReferenceAttribute

## Summary
Allows referencing an actor either locally or globally by its ID. This automatically populates the field with a strong reference to the actor.
It can be applied on [Actor](../actor.md) or any class deriving from [ActorScript](../script/actorscript.md).



## Definition

**Namespace:** `SDT4.Managed.Core.Attributes`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
sealed class ActorReferenceAttribute
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔ [Attribute](https://learn.microsoft.com/dotnet/api/system.attribute) ➔  **ActorReferenceAttribute**
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
| `public get; LocalId` | [UInt64](https://learn.microsoft.com/dotnet/api/system.uint64) |  |
| `public get; GlobalId` | [Guid](https://learn.microsoft.com/dotnet/api/system.guid) |  |
| `public get; IsGlobal` | [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean) |  |



---

## Methods



---