## Purpose

First of all, thank you for your interest in the project! The main goal of this project is to be used as a learning opportunity for beginers in programming and/or Python. The project offers a great learning opportunity because it incorporates the following technologies and concepts:
* Python.
* API wrapper library.
* `discord.py` to create, manage and automate Discord bots.
* In the future, a database will be incorporated.
* Real-time communication, command pattern, and defensive programming.

Please feel free to familiarize yourself with the existing code, specifically on the `src/main.py` file. It should be straightforward, but don't fret if you don't understand some concepts (ex. `async`, `import`, etc.), there will be an opportunity for you to learn them in the future. Indeed, the focus is more on incremental learning rather than you being expected to be familiar with everything from the start.

If any of the steps outlined here do not make sense to you, or you are having trouble understanding instructions, please either ask for clarification by writing comments on the issues, or [join the Discord server](http://discord.gg/GPw3xnRE4y) for one-on-one help.

## How can I contribute or get started?

The best way to get started is to take on [issues labeled "Good first issue"]([https://github.com/sobbd/artemis-discord-bot/issues](https://github.com/sobbd/artemis-discord-bot/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)), as these issues are aimed towards beginners.

Here's a step-by-step guide on how to proceed after you've found an issue that you're interested on working:
1. After reading the issue details and what needs to be done, if you feel like you'd like to give it a try, comment on the issue declaring that you will be working on it!
2. Then, it will be assigned to you by a collaborator of the project.
3. Fork the project (fork button is located at top right, on the main page of the project), so that you have a copy in your GitHub account for which you can make changes to. The reason being that only collaborators have direct push permission into the repository.
4. Once a fork has been created in your account, clone that fork using Git or a Git UI application such as [GitHub Desktop](https://desktop.github.com/). It will be downloaded to your local machine, so that you can actually start coding your changes.
5. Open the downloaded fork folder on your code editor of choice, and begin writing code for the issue! Note that you will __not__ need to fork and download the forked repository again in the future; you can make all future commits with the copy on your local machine.
6. Once you have made changes, make commits. The commit messages should always include the issue number in the format of `#X`, where `X` is the issue number. For example, if the issue that you worked on was issue `#2`, then you would include that at the end of your commit message (ex. `"Implemented new functionality #2"`, or `"Added clear command, minor refactoring #3"`). The reason for this is that it will tell GitHub to automatically reference your commit on the issue, and it will essentially create a log of what commits have been made in relation to that specific issue.
7. When making a final commit (say, the commit that will close and complete the issue), you would instead include `fixes #X` or `closes #X` at the end of the commit message. This will instruct GitHub to both reference the commit, and automatically close the issue for you! Here's one example commit message that fixes issue `#3`: `"Fixed bug with clear command, closes #3"`.

## Code design requirements

Here are some guidelines to follow and keep in mind when writing good code for the project. Don't worry if you think you've missed any, during the code review process, it may be simply asked for you to implement them!

* Types should be used whenever possible. For example, all function parameters, and return types should have a corresponding type: `def get(amount: int) -> int`
* All names should be meaningful. For example, variable and function names should be named in accordance to what they are, and not simply a random letter:
  * Bad: `x`, `a`, `b`, `bb`, `thing`, etc.
  * Good: `amount`, `size`, `age`, `name`, `github_link`, `calculate_age`, `update_task`, `complete_task`.
* Comments should only be used when the context surrounding the code segment in question is complex by nature, and they should explain __why__ something is done, not __what__ something is.
  * Explaining what something __is__ is often redundant, because most competent programmers can determine what something is by simply glancing at it.
  * Avoiding the overuse of comments is good because comments have overhead; they require maintenance and that means that for each comment added, it needs to be kept updated and correct, otherwise it would risk lying to the programmers, especially if the codebase is rapidly changing.

## Coding style

TODO
