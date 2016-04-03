# Frontend task

Just a bit of showcasing.

The initial aim was to use [react-grid-layout](https://github.com/STRML/react-grid-layout).
You may see a commit where I experimented with it, but there was an issue with layout height not adjusting
to it's context and I could not find an straightforward way to resolve it.


## Tech:
* *Foundation*:

    It provides me with a simple grid system I can use to handle reponsiveness.
    I also don't want to deal with the minutiae of styling buttons and inputs.
    This lib's CSS/JS is loaded via a cdn into the page.

* *SASS*:

    Decided to use it because Foundation is written in SASS.
    Altough it is loaded as CSS into the page, the ideal scennario would be to have it alongside
    the project and use SASS to pick and choose what we need of it.

    I would also have access to the mixins and utilities provided,.

    For this project tough, I dont wan't add all those files to the repo.
    Thus, I decided to copy a few scss files from foundation to have access to an utility I'm going
    to need: the breakpoint mixins.

* *React*:

    I like react because it I like that it allow me to model the frontend as a system of components.
    Along with flux, it allows for the interface to always match the state of the application.

* *BEM styles*:

    This format "mixes" nicely with react components and makes the styles more readable.


* *Webpack*:

    Used for the development server and to bundle the styles and javascript.
    Allows me to write jsx, es6 and sass.
    It is a bit of a resource hog, but not for the scale of this project.

