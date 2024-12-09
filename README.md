# Lowpm 

Lowpm is project management app that works where you work. 

It is meant to work alongside our text editor of choice. Allowing management of our projects where we are working.   

## Philosophy 

Regardless of how you nomenclature around projects, calling large objective epics, children or epics projects, children of projects task etc. My conclusion of this is a project management system needs to be dynamic because a task might upon discovery be a project and a project might become a epic. Regardless of how we label these objective our tool needs to handle these developments. 

## Fundamentals  

### Documents

The premise that this project is build on is that any project big or small can be managed by a few core building blocks;

- boards
- pages
- list
- tables

### Frontmatter (metadata)

The frontmatter is how we associated our documents 

[Lowpm Behavior](docs/behavior.md) 

#### Boards 

Board are our catch alls

```md:file=foo.board.md 
# frontmatter (our metadata)
---
title: foo
date_created: 01/01/3039
type: board
---

## todo 

## inprogress

## done 

```

These elements can be associated with each other. 

### Influence 

Since the introduction of the Kanban board we have see many evolutions of this and a few feature sets that seem to be the most effective.

## RoadMap 

### Version 1

- cli 

### Version 2 

- API
- database

### Dreams 

Stretch (discovery required) 

- GUI 
- Integrations with Github issues 
- Trello 
- Notion??
