# ScriptComputationalComplexity

## Summary
Specifies the expected computational overhead or workload category of a function.



## Definition

**Namespace:** `SDT4.Managed.Core.Attributes`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
enum ScriptComputationalComplexity
```

---

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `Fast` | [ScriptComputationalComplexity](./scriptcomputationalcomplexity.md) | Negligible computational overhead; runs almost instantaneously. |
| `Low` | [ScriptComputationalComplexity](./scriptcomputationalcomplexity.md) | Minimal computational overhead; suitable for frequent execution. |
| `Moderate` | [ScriptComputationalComplexity](./scriptcomputationalcomplexity.md) | Moderate computational overhead; standard execution cost. |
| `High` | [ScriptComputationalComplexity](./scriptcomputationalcomplexity.md) | High computational overhead; may impact frame rate or throughput if executed frequently. |
| `Extreme` | [ScriptComputationalComplexity](./scriptcomputationalcomplexity.md) | Severe computational overhead; Should be used sparingly. |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |



---

## Methods



---