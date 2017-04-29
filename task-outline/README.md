# Frontend task

## Outline

Build a single page that will provide information and photos of the different room types of a property based on the [desktop](#file-desktop-png) and [mobile](#file-mobile-png) wires.

## Criteria

- The page should be functional and presentable in modern browsers and devices but feel free to use your favorite modern tools and tech. Feel free to experiment a bit.
- The provided wires are to be used *as a guideline* of functionality only. We encourage you to make design changes that improve the user experience.
- Please make your test available as a git repo we can clone it locally to look at the code and run it.
- Please include an explanation that talks about your technology decisions and anything else you want us to know about your task.
- The room types are expanded in desktop but collapsed in mobile. There should be transitions when navigating between the room types in mobile. You are free to come up with what this transition looks like.
- Please satisfy the following "Dynamic Content" user story:

### Dynamic Content

As a user I want to be encouraged by how many friends of mine have stayed in a room I'm viewing. I don't need to see all my friends, just a summary.

Provided is [friends.json](#file-friends-json) which includes an object of rooms with lists of friend who stayed in each room. Based on the data per room, you will need to show the information to the user sorted by *name ascending*. For example:

- if 0 friends, then don't show any message
- if 1 friend, then show "Jane Doe has stayed here"
- if 2 friends, then show "Jane Doe and John Doe have stayed here"
- if 3 friends, then show "Jane Doe, John Doe, and 1 other friend have stayed here"
- if 4 or more friends, then show "Jane Doe, John Doe, and 2 other friends have stayed here"

## Questions

Feel free to email any questions to mike.cravey@overseasstudentliving.com.
