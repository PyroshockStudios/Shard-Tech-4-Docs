# AssetErrorCode

## Summary
Represents the status or error state resulting from an asset management or load operation.



## Definition

**Namespace:** `SDT4.Managed.Core.Asset`  
**Assembly:** `SDT4.Managed.Core.dll`

```csharp
enum AssetErrorCode
```

---

## Fields

| Name | Type | Description |
| --- | --- | --- |
| `None` | [AssetErrorCode](./asseterrorcode.md) | No error or default status. |
| `Idle` | [AssetErrorCode](./asseterrorcode.md) | The resource exists and remains unchanged. |
| `Updated` | [AssetErrorCode](./asseterrorcode.md) | The resource exists and has been successfully updated. |
| `Emplaced` | [AssetErrorCode](./asseterrorcode.md) | The resource has been newly added. |
| `AssetMissing` | [AssetErrorCode](./asseterrorcode.md) | The content manager failed to find the specified asset. |
| `TypeMismatch` | [AssetErrorCode](./asseterrorcode.md) | The requested resource type does not match the stored asset type. |
| `OperationAborted` | [AssetErrorCode](./asseterrorcode.md) | The operation was unexpectedly cancelled, and the asset was not loaded. |
| `InsufficientMemory` | [AssetErrorCode](./asseterrorcode.md) | Memory was insufficient to complete the operation. |
| `FilesystemError` | [AssetErrorCode](./asseterrorcode.md) | A filesystem error occurred, causing the operation to fail. |
| `MissingImplementation` | [AssetErrorCode](./asseterrorcode.md) | The asset type is missing required serialization implementations. |
| `CatastrophicFailure` | [AssetErrorCode](./asseterrorcode.md) | An unrecoverable, severe system failure occurred. |



---

## Properties

| Name | Type | Description |
| --- | --- | --- |



---

## Methods



---