# ActorScript

## Summary




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
| `public get; UniqueIdentifier` | [Guid](https://learn.microsoft.com/dotnet/api/system.guid) |  |



---

## Methods

#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) OnCreate([ScriptPayload](./scriptpayload.md) payload)


**Summary:**
Gets called when script is being created. Level may not have started playing yet,
and any rigid bodies will not have been added yet!
Creation may be vetoed. If creation is vetoed, it is <em>strongly</em> assumed that 
the actor is in a safe state to remove from memory (e.g. no dangling objects)!
<list>
<item><param name="payload">The creation payload.</param></item>
</list>
<strong>Actor States:</strong>
<list>
<item><strong>Script:</strong> <em>Valid</em></item>
<item><strong>Physics:</strong> <em>INVALID</em></item>
<item><strong>Renderer:</strong> <em>INVALID</em></item>
</list>

**Parameters:**

- `payload` ([ScriptPayload](./scriptpayload.md)): 


---
#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) OnSpawn()


**Summary:**
Gets called when actor is fully initialised, but before it started ticking.
This means that the level might not have been fully loaded in yet!
<strong>Actor States:</strong>
<list>
<item><strong>Script:</strong> <em>Valid</em></item>
<item><strong>Physics:</strong> <em>Valid</em></item>
<item><strong>Renderer:</strong> <em>Valid</em></item>
</list>

---
#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) OnBegin()


**Summary:**
Gets called when this Actor starts ticking.
<strong>Actor States:</strong>
<list>
<item><strong>Script:</strong> <em>Valid</em></item>
<item><strong>Physics:</strong> <em>Valid</em></item>
<item><strong>Renderer:</strong> <em>Valid</em></item>
</list>

---
#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) OnTick([Single](https://learn.microsoft.com/dotnet/api/system.single) dt)


**Summary:**
Gets called per frame.
<list type="number">
<item><param name="dt">Delta time in <em>seconds</em></param></item>
</list>

**Parameters:**

- `dt` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


---
#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) OnStep([Single](https://learn.microsoft.com/dotnet/api/system.single) ts)


**Summary:**
Gets called per fixed step. May be called multiple times per frame, or even be skipped!
<list type="number">
<item><param name="ts">Fixed step time in <em>seconds</em></param></item>
</list>

**Parameters:**

- `ts` ([Single](https://learn.microsoft.com/dotnet/api/system.single)): 


---
#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) OnEnd()


**Summary:**
Gets called when this Actor stops ticking.
<strong>Actor States:</strong>
<list>
<item><strong>Script:</strong> <em>Valid</em></item>
<item><strong>Physics:</strong> <em>Valid</em></item>
<item><strong>Renderer:</strong> <em>Valid</em></item>
</list>

---
#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) OnKill()


**Summary:**
Gets called when this Actor is destroyed.
<strong>Actor States:</strong>
<list>
<item><strong>Script:</strong> <em>Valid</em></item>
<item><strong>Physics:</strong> <em>Valid</em></item>
<item><strong>Renderer:</strong> <em>Valid</em></item>
</list>

---
#### protected virtual [Void](https://learn.microsoft.com/dotnet/api/system.void) OnDestroy()


**Summary:**
Gets called when the script instance is destroyed.
<strong>Actor States:</strong>
<list>
<item><strong>Script:</strong> <em>Valid</em></item>
<item><strong>Physics:</strong> <em>INVALID</em></item>
<item><strong>Renderer:</strong> <em>Unknown</em></item>
</list>

---


---