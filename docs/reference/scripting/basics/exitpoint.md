# Script Exit Point

After the user is finished playing the game, we should give him an option to quit the game, after all, we don't want to keep gamers unhealthily hooked on the game... right?

## Requesting exit

[Window](../../../cs-api-ref/sdt4.managed.windowing/window.md).Close() is sufficient to request the exit of the application. Closing the Primary window will request a stop to the game loop and close the app resources.

```csharp
using SDT4.Managed.Core;
// ...
// Use our Window Platform that we have gotten from the capabilities!
WindowPlatform windowing = /*...*/;
windowing.PrimaryWindow.Close();
// Clean up our scenes and stop simulation
// ...
// Finally, terminate to stop the engine
instance.Terminate();
```