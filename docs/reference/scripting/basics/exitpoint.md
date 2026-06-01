# Script Exit Point

After the user is finished playing the game, we should give him an option to quit the game, after all, we don't want to keep gamers unhealthily hooked on the game... right?

## Requesting exit

[AppInstance](../modules/sdt4.managed.core/appinstance.md).RequestAppExitAsync() returns an exit code, if the application can be terminated. In most circumstances it will always return [AppExitRequest](../modules/sdt4.managed.core/appexitrequest.md).Success. In other cases, 

```csharp
using SDT4.Managed.Core;
// ...
// Use our app instance that we have gotten from the entry point!
AppInstance instance = /*...*/;
await request = instance.RequestAppExitAsync();
if (request == AppExitRequest.Success) {
    // Clean up our scenes and stop simulation
    // ...
    // Finally, terminate to stop the engine
    instance.Terminate();
}
```