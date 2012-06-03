## DjangoCMS Embedded Menu

This simple extension allows you to place menus in placeholders via the
administration interface.


## Requirements

* django-cms
* And all the requirements the above project(s) depend on.


## Installation

1. make sure you are using a python virtual environment
    `mkdir -p ~/Dev/virtualenv && virtualenv ~/Dev/virtualenv/projectname && . ~/Dev/virtualenv/projectname/bin/activate && mkdir -p ~/Dev/projects/projectname/ && cd ~/Dev/projects/projectname; `

2. install it from pypi

    `pip install cmsplugin-embedded-menu`

3. or, install it from github

    `pip install git+https://github.com/airtonix/cmsplugin-embedded-menu`

## Configuration

1. add `cmsplugin_embeddedmenu` to your `INSTALLED_APPS`

2. perform a `./manage.py migrate` (for south users), or `./manage.py syncdb`

3. There is no step three!


## Override Template

Choosing a template in the administration interface means that you
populate the following two relative paths (to any of your app template dirs)
with templates you desire to be made available.

* cmsplugin_embeddedmenu/layouts

Any .html file that doesn't contain the word 'base' will be presented in
the template selector combo dropdown in the admin interface.

For example, if your django project was at :

    `~/Dev/Django/MyProjectName/`

And you had a django application named `SomethingSomethingSomething` at :

    `~/Dev/Django/MyProjectName/SomethingSomethingSomething/`

Then templates for this plugin could be found at :

    `~/Dev/Django/MyProjectName/SomethingSomethingSomething/templates/cmsplugin_embeddedmenu/layouts/*.html`

In fact, anywhere django looks for templates, you can place the following tree :

    /cmsplugin_embeddedmenu
        /layouts
            /*.html

### Purpose of Templates

#### Containers

These are the top most elements in any menuplugin that exists in a placeholder. 

By default it contains a H3 element and DIV element with the following attribtues : 

*H3*

 * Text: `MenuTitle`, input from plugin settings
 * Text: `MenuSubtitle`, input from plugin settings

*DIV*

 * `id='cms-menu-{{ plugin.id }}'`, where plugin.id matches the instance of the settings model for that menu.
 * `class='cms-plugin cms-menuplugin'`
 * `data-plugin-position={{ plugin.position}}`, sorted position within the placeholder.

#### Menus

These wrap each branch in a menu, they pull in each menu item node with the template selected from the 
next template group `cmsplugin_embeddedmenu/layouts/items/*.html`

By default, menu branchs are displayed as un-orderded lists (UL) with no attributes.

#### Items

Renders each menu item node as a list-item(LI) with the following attributes:

*LI*

 * `class='selected ancestor sibling descendant'`
    * `selected` applies if the node matches the page being viewed
    * `ancestor`  applies if it contains a menu branch.
 * `data-node-depth={{item.level}}`, how deep in the tree this node is.

If this node is a parent to other pages, then it will include the chosen `Menus` template inside the `LI` after the `A`


### Customising Templates

Templates in all groups are provided the context :

a CMSPlugin has many useful attributes for you to use, the main one
is `plugin.instance` a reference to the settings model.


    plugin' :
        An instance of CMSPlugin, which itself provides reference 
        to either of the settings models as outlined below.


#### base.html

base.html in the `cmsplugin_embeddedmenu` directory is used to load the
selected template chosen in the administration interface.


#### ./layouts/*.html

templates here are provided the context :


    plugin.instance
        template
            Chosen template.


## Contributions

anyone is free to contribute, simply submit a merge request at
github : http://github.com/airtonix/cmsplugin-embedded-menu


## Todo

provide option to manipulate menu choices:

* Look at reducing queries.
* Look at caching options.
