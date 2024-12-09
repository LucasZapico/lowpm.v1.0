

## Document is added to Board 


This is where lowpm starts to deviate from standard markdown documents. 

```md:file=foo.board.md
// frontmatter 

## todo 

- [project bar](project-bar.page.md)
  - title: project bar 
  - description: I'm a project associated with project foo
  - tags: ["zap", "gip"]
   

```

If you added the above to the board lowpm will create 

```md:file=project-bar.page.md
---
title: project bar
description: I'm a project associated with project foo
status: todo
boards: ["foo"]
tags: ["zap", "gip"]
type: page
---

```

<!-- 
TODO: list added to board
TODO: list in board syntax 
TODO: table added to board
TODO: table in board syntax

 -->


