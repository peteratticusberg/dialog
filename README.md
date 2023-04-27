Dialog gets chatgpt to talk to itself. 

The goal of dialog is to increase the size of the problems chatgpt can tackle. 

Starting a dialog takes two prompts, e.g.

```
Please give me an idea for a short story that I could write.
```
and
```
I'd like for you to pretend to be a writing coach. 
I'm going to give you an idea for a short story. 
I'd like for you to challenge me to break the short story up into a handful of sections.
After I've done that, I'd then like you to ask me to write the individual sections of the short story.
Remember, you're my writing coach and I'd like you to first help me break my story up into sections, and then ask me to write each section. 
I'm looking forward to getting started!
```

To do: 

Add in ability to create arbitrary hooks for:
- context management, would be good to have different ways to handle this
- prompt completion selection, e.g. (user-based selection, ability to edit ai generated prompts on the fly, ai-based selection)
- logging / response persistence (saving stuff to files, persisting to a db, printing to stdout, etc. )

Stub in plugins like functionality?
asyncio? 

Schema for persisting dialog runs / serializing so we can pause and restart 

any point in making it so people could ssh into a server to use this a la alt.org?


