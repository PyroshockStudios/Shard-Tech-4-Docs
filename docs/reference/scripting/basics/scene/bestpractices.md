# Best Practices

Scenes are the heaviest resources, as they hold many resources, contain a lot of state information, and are the general drivers of the game. With such great power comes great responsibility, which is what this brief list of DO's and DONT's is here to guide.

## DO's

- DO: Dispose [SceneAsset](../../../../cs-api-ref/sdt4.managed.core/asset/sceneasset.md) as soon as you are not creating the scene again.
    - This reduces memory usage, as well as removes references from assets that may no longer be loaded in the scene, that otherwise would take up precious system resources.
- DO: Use async and await when managing scenes.
    - C# is a very asynchronous capable language, and Shard Tech 4 accommodates that by providing many features to accompany this. Use them!
- DO: Use `Scene.StartAsync()` and `Scene.StopAsync()` for maximum concurrency. This also allows the scene to (optionally) start ticking before the entire actor hierarchy has loaded in. 

## DONT's

- DONT: Omit Dispose() when finished with a scene.
    - This will cause a scene resource leak, and you will receive errors when the game terminates notifying you of this mistake!
- DONT: Abuse [Threads.RunLater(ThreadStart)](../../../../cs-api-ref/sdt4.managed.core/threads.md) in an asynchronous task to manipulate the scene. It is best to directly manage the scene on the master thread in a suitable subroutine!