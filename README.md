# Frontend task

Just a bit of showcasing.

## Setup
0. Setup a new node v5.10.0 environment with [nvm](https://github.com/creationix/nvm)
1. `git clone git@github.com:lvisintini/frontend-task.git`
2. `cd frontend-task`
3. `npm install`
4. `node server`
5. Demo site will be running on `http://localhost:3000`


## Some notes

The initial aim was to use [react-grid-layout](https://github.com/STRML/react-grid-layout).
You may see a commit where I experimented with it, but there was an issue with layout height not adjusting
to it's context and I could not find an straightforward way to resolve it.

When the approach above failed, I proceeded to go for a more conventional approach.

There was also an attempt to write tests for the dynamic component, but setting up a tests suite that would
play nicely with webpack proved too difficult for a tired brain.
There is a `tests.jsx` that you are welcome to review.


## Tech:
* *Foundation*:

    It provides me with a simple grid system I can use to handle reponsiveness.
    I also don't want to deal with the minutiae of styling buttons and inputs.
    This lib's CSS is loaded via a cdn into the page.

* *SASS*:

    Decided to use it because Foundation is written in SASS.
    Altough it is loaded as CSS into the page, the ideal scennario would be to have it alongside
    the project and use SASS to pick and choose only whats required for the project.

    I feel like that could have been a huge investemnt of time for a small benefit.
    Thus, I decided to cut some corners and copy a few scss files from the foundation lib into the project.
    This is only to have access to a few utilities i'm going to need, but it is not something that
    I would 'enjoy' doing in a production environment.

* *React*:

    I like react because it allows me to model the frontend as a system of components.
    Along with a flux lib, it allows for the interface to always match the state of the application.
    I have not used a flux lib on this project and the state is handled by the react componets, but
    I am aware that it all could look much nicer if I used redux or fluxxor

* *BEM styles*:

    This format "mixes" nicely with react components and makes the styles more readable.

* *Webpack*:

    This is certainly a new tech for me and this is may first time using it first hand.
    Really enjoyed the development server.
    I use it to bundle the styles and javascript and to allow me to write jsx, es6 and sass.
    It is a bit of a resource hog, but not for the scale of this project.

* *Stylesheets via JS*:

    Webpack orchestrates the build process and it makes it available to the page via a bundle.js.
    The stylesheets are there too.
    Some people seem to be doing this and I felt like guiving it a try. I'm still at odds with it.


## Suggestions for the wires

I feel a some of the real estate available on the screen is unused or empty in the desktop version.
As a user, I would expect to see a few pictures for each of the rooms to get a sense of what they look like.

Sadly, I was not able to flesh out in any of this opinions into the work.
