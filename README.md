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

ChatGPT driven analysis and selection of completion.choices based on user input (think: "Select the choice that you think will make for the most (tragic|interesting|surreal) story")

ChatGPT driven turn-based control over Temperature and Top P based on user input (think: "Given what you know about the goals of this conversation, please choose values for temperature and top p that you think align best with these goals")

Recursive dialogs (e.g. you'd like to write multiple books with a single dialog, so you spawn dialog per book idea and one dialog per chapter for each book)

ChatGPT driven context summaries to expand what can be done within a given context limit

ChatGPT driven turn-based pruning of conversations based on relevance for a given prompt