# Best Practices

Projects are where the game development phase starts, and while getting it right is undermined -- it is nonetheless important.

## DO's

- DO: PLACE PROJECTS IN PATHS WITH NO SPACES! This avoids any possible bugs due to software not properly escaping paths! While Shard Tech 4 in principle *should* fare correctly under those circumstances, it is best to use whitespace-free paths.
- DO: Set an upper limit on the SDK version, as the engine may introduce breaking changes in later versions!
- DO: Use long-term support .NET versions, e.g. .NET 10

## DONT's

- DONT: Use preview .NET version when shipping. As it is experimental, it may cause issues with the engine's code analysers, building, and shipping for the end user.  