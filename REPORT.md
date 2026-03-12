# Report

##### The project REPORT is where students will document key learnings, challenges, and reflections on their experience using CoPilot for software development. 

## First Impressions

#### Initial Take on the Project Assignment

##### In this section, students will provide their initial thoughts on the project assignment, including their understanding of the requirements, any assumptions they made, points that need clarification, and their overall approach to tackling the project.
### Initial Thoughts

At first, I thought this project maybe a project to learning using AI to code for me, and build a mid-large project by prompting AI agent.

### Assumptions Made

I don't know about Hangman games at all, I thought the game more likely to guess the whole word.

> Like:
>
> |        | Word                                     |
> | ------ | ---------------------------------------- |
> | Answer | HELLO                                    |
> | Guess  | LEMON                                    |
> | Repo   | _ E _ _ _<br />L and O in wrong position |

### Points Needing Clarification

What we need to do is the most important thing in develop.

## Key Learnings
##### Here, students will summarize the most important things they learned while working on the project. This could include computer science related concepts, technical skills, insights about using CoPilot effectively, and any new concepts or tools they encountered
### Computer Science Concepts and Technical Skills

- How to write pytest for python files.
- Some small but useful methods in python.
- How to write a good prompt and using Agents files to modify CoPilot.

### Insights about Using CoPilot Effectively

Write docs with CoPilot helps a lot, makes boring work less and have more time focusing on important things.

### New Concepts or Tools Encountered

Pytest, Documentation in functions, Agents files

## Report on CoPilot Prompting Experience
##### Student may pull examples from the JOURNAL.md to illustrate their experience, including specific interactions that were particularly helpful or challenging.
### Types of prompts that worked well

- I've started implementing a guess the word game (hangman).  
  Can you review my `update_game_state` function?
- how to write tests? am i doing right? if not, please show and teach me

Clear requirement, simple but plain questions

### Types of prompts that did not work well or failed

- Can you suggest tests for this function?
- i ran pytest -q, but get an error, how to run pytest?

Too simple or too short, didn't state clearly.

## Limitations, Hallucinations and Failures
##### In this section, students will document any instances where CoPilot provided incorrect or misleading information (hallucinations) or where it failed to provide a useful response. They will analyze why these issues occurred and how they impacted their work on the project.
##### For example: Fabricated APIs, Deprecated functions, Subtle logical errors, Confident but wrong explanations, Over-engineered solutions, Under-engineered solutions, overcomplicated code, oversimplified code, etc.
### Examples of Hallucinations or Failures or Misleading Information or Confident but Wrong Explanations, or Over-engineered or Under-engineered Solutions

When I ask AI to write tests, it tried to run ` pytest -q`, cause a failure. I ask `i ran pytest -q, but get an error, how to run pytest?`, it suddenly change the command and it works.

```bash
# Here's how to run pytest correctly:
python3 -m pytest -q
# Or without the -q flag for more verbose output:
python3 -m pytest
```

### Analysis of Why These Issues Occurred

Maybe caused by a long conversation or model's coding ability unstable in auto mode.

### Impact on the Project

Wasted some time.

## AI Trust
### When did I trust the AI?

When it is taking about an area that I'm familiar with. Or very simple tasks

### When did I stop trusting it?

When hallucinations/wrong things given.

### What signals or situations or patterns indicated low reliability?

Too complex or lack of information.

## What I Learned
### What did you learn about software development?

There are new development ways nowadays, we need to follow up.

### What did you learn about using AI tools?

Be careful, think twice, think more, don't rely on them without thinking.

### When should you trust AI? When should you double-check it?

Never trust AI 100%, check each time especially facing an AI agent, don't give them full rights.

## Reflection
### Did AI make you faster? Why or why not?

Yes, help me do a lot of boring, simple tasks.

### Did you feel in control of the code?

Yes, I can ask it to change anytime anywhere I want.

### Would you use AI the same way next time? What would you change?

Yes, think more in the first place.