# ActorScript

## Summary
Represents a scriptable actor that provides a foundational blank slate for custom gameplay behaviours.

## Remarks
<para><b>Master Thread:</b> Operations on this type interact directly with scene and engine state, and must be executed exclusively on the Master Thread.</para>

## Definition

**Namespace:** `SDT4.Managed.Core.Script`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
class ActorScript
```
**Inheritance:**

##### [Object](https://learn.microsoft.com/dotnet/api/system.object) ➔ [Actor](../actor.md) ➔  **ActorScript**
**Implements:**

##### [IScriptTarget](./iscripttarget.md)
---

## Fields

| Name | Type | Description |
| --- | --- | --- |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |
| `public get; UniqueIdentifier` | [Guid](https://learn.microsoft.com/dotnet/api/system.guid) | Gets the globally unique identifier of this actor, corresponding to [Actor.GlobalId](../actor.md#globalid). |



---

## Methods

#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) OnCreate([ScriptPayload](./scriptpayload.md) payload)


**Summary:**
Invoked when the script is being created.

**Remarks:**
The level may not have started playing yet, and rigid bodies will not have been added at this stage.
Creation may be vetoed via [ScriptPayload.Veto](./scriptpayload.md#veto). If creation is vetoed, it is strongly 
assumed that the actor is in a safe state to be removed from memory with no dangling references.
<para><b>Actor States:</b></para>
<list type="bullet">
<item><description><b>Script:</b> <i>Valid</i></description></item>
<item><description><b>Physics:</b> <i>Invalid</i></description></item>
<item><description><b>Renderer:</b> <i>Invalid</i></description></item>
</list>

**Parameters:**

- `payload` ([ScriptPayload](./scriptpayload.md)): The creation payload containing initialisation state and veto controls.


---
#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) OnSpawn()


**Summary:**
Invoked when the actor is fully initialised, but before it starts ticking.

**Remarks:**
The level might not have been fully loaded at this point.
<para><b>Actor States:</b></para>
<list type="bullet">
<item><description><b>Script:</b> <i>Valid</i></description></item>
<item><description><b>Physics:</b> <i>Valid</i></description></item>
<item><description><b>Renderer:</b> <i>Valid</i></description></item>
</list>

---
#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) OnBegin()


**Summary:**
Invoked when this actor begins ticking.

**Remarks:**
<para><b>Actor States:</b></para>
<list type="bullet">
<item><description><b>Script:</b> <i>Valid</i></description></item>
<item><description><b>Physics:</b> <i>Valid</i></description></item>
<item><description><b>Renderer:</b> <i>Valid</i></description></item>
</list>

---
#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) OnTick([Single](https://learn.microsoft.com/dotnet/api/system.single) dt)


**Summary:**
Invoked every frame during the engine update cycle.

**Parameters:**

- `dt` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The delta time in seconds elapsed since the previous frame.


---
#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) OnStep([Single](https://learn.microsoft.com/dotnet/api/system.single) ts)


**Summary:**
Invoked per fixed physics step. May be called multiple times per frame, or skipped entirely if frame rate permits.

**Parameters:**

- `ts` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): The fixed timestep duration in seconds.


---
#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) OnEnd()


**Summary:**
Invoked when this actor ceases ticking.

**Remarks:**
<para><b>Actor States:</b></para>
<list type="bullet">
<item><description><b>Script:</b> <i>Valid</i></description></item>
<item><description><b>Physics:</b> <i>Valid</i></description></item>
<item><description><b>Renderer:</b> <i>Valid</i></description></item>
</list>

---
#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) OnKill()


**Summary:**
Invoked when this actor is killed or marked for destruction.

**Remarks:**
<para><b>Actor States:</b></para>
<list type="bullet">
<item><description><b>Script:</b> <i>Valid</i></description></item>
<item><description><b>Physics:</b> <i>Valid</i></description></item>
<item><description><b>Renderer:</b> <i>Valid</i></description></item>
</list>

---
#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) OnDestroy()


**Summary:**
Invoked when the script instance is destroyed.

**Remarks:**
<para><b>Actor States:</b></para>
<list type="bullet">
<item><description><b>Script:</b> <i>Valid</i></description></item>
<item><description><b>Physics:</b> <i>Invalid</i></description></item>
<item><description><b>Renderer:</b> <i>Unknown</i></description></item>
</list>

---


---